import os
import sys
import json
import ctypes
import subprocess
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

CONFIG_FILE = "config.json"

# 默认初始配置（自动适配 Windows 的 WLAN 网卡名称）
DEFAULT_CONFIG = {
    "网卡名称:": "WLAN",
    "静态 IP:": "192.168.3.36",
    "子网掩码:": "255.255.255.0",
    "默认网关:": "192.168.3.5",
    "首选 DNS:": "192.168.3.5",
    "备用 DNS:": "114.114.114.114"
}

class IPSwitcherWinApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("网络方案一键切换器 (Windows)")
        self.geometry("480x560")
        self.resizable(False, False)
        
        # 加载本地配置
        self.config_data = self.load_config()
        
        self.title_label = ctk.CTkLabel(self, text="⚡️ IP 自动/静态一键切换", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=15)
        
        self.status_frame = ctk.CTkFrame(self, width=440, height=80)
        self.status_frame.pack(pady=10, padx=20, fill="both")
        
        self.status_title = ctk.CTkLabel(self.status_frame, text="当前网络模式:", font=ctk.CTkFont(size=12))
        self.status_title.pack(pady=(10, 2))
        
        self.status_text = ctk.CTkLabel(self.status_frame, text="检测中...", font=ctk.CTkFont(size=16, weight="bold"), text_color="#FFCC00")
        self.status_text.pack(pady=(0, 10))
        
        self.config_frame = ctk.CTkFrame(self)
        self.config_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.tip_label = ctk.CTkLabel(self.config_frame, text="⚙️ 方案 B 静态参数手动配置", font=ctk.CTkFont(size=13, weight="bold"))
        self.tip_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(15, 5), sticky="w")
        
        self.entries = {}
        self.create_input_field("网卡名称:", self.config_data.get("网卡名称:", "WLAN"), 1)
        self.create_input_field("静态 IP:", self.config_data.get("静态 IP:", "192.168.3.36"), 2)
        self.create_input_field("子网掩码:", self.config_data.get("子网掩码:", "255.255.255.0"), 3)
        self.create_input_field("默认网关:", self.config_data.get("默认网关:", "192.168.3.5"), 4)
        self.create_input_field("首选 DNS:", self.config_data.get("首选 DNS:", "192.168.3.5"), 5)
        self.create_input_field("备用 DNS:", self.config_data.get("备用 DNS:", "114.114.114.114"), 6)
        
        self.action_btn = ctk.CTkButton(self, text="检查中...", width=220, height=45, font=ctk.CTkFont(size=14, weight="bold"), command=self.toggle_ip)
        self.action_btn.pack(pady=20)
        
        self.check_current_status()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return DEFAULT_CONFIG
        return DEFAULT_CONFIG

    def save_config(self):
        current_config = {key: entry.get().strip() for key, entry in self.entries.items()}
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(current_config, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存配置文件失败: {e}")

    def create_input_field(self, label_text, default_value, row_idx):
        lbl = ctk.CTkLabel(self.config_frame, text=label_text, font=ctk.CTkFont(size=12))
        lbl.grid(row=row_idx, column=0, padx=(20, 10), pady=8, sticky="w")
        
        entry = ctk.CTkEntry(self.config_frame, width=240, font=ctk.CTkFont(size=12))
        entry.insert(0, default_value)
        entry.grid(row=row_idx, column=1, padx=(40, 20), pady=8, sticky="e")
        self.entries[label_text] = entry

    def get_current_interface(self):
        return self.entries["网卡名称:"].get().strip()

    def check_current_status(self):
        interface = self.get_current_interface()
        gateway = self.entries["默认网关:"].get().strip()
        try:
            # 通过 netsh 检查网卡配置中是否包含当前静态网关
            result = subprocess.check_output(f'netsh interface ip show config name="{interface}"', shell=True, creationflags=subprocess.CREATE_NO_WINDOW).decode('gbk', errors='ignore')
            if gateway in result and "DHCP:" in result and "否" in result:
                self.current_mode = "B"
                self.status_text.configure(text="方案 B (手动指定静态 IP)", text_color="#3498DB")
                self.action_btn.configure(text="👉 一键切换为 方案 A (自动获取)")
            else:
                self.current_mode = "A"
                self.status_text.configure(text="方案 A (自动获取 DHCP)", text_color="#2ECC71")
                self.action_btn.configure(text="👉 一键切换为 方案 B (静态 IP)")
        except Exception:
            self.status_text.configure(text="未检测到网卡，请确认网卡名称（如 WLAN、以太网）", text_color="#E74C3C")
            self.action_btn.configure(text="刷新重试", command=self.check_current_status)

    def toggle_ip(self):
        self.save_config()
        
        interface = self.get_current_interface()
        static_ip = self.entries["静态 IP:"].get().strip()
        subnet = self.entries["子网掩码:"].get().strip()
        gateway = self.entries["默认网关:"].get().strip()
        dns1 = self.entries["首选 DNS:"].get().strip()
        dns2 = self.entries["备用 DNS:"].get().strip()
        
        self.action_btn.configure(state="disabled", text="正在配置...")
        self.update()
        
        try:
            if self.current_mode == "A":
                # 切换到 B (静态 IP)
                subprocess.run(f'netsh interface ip set address name="{interface}" source=static addr={static_ip} mask={subnet} gateway={gateway}', shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run(f'netsh interface ip set dns name="{interface}" source=static addr={dns1} register=primary', shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                if dns2:
                    subprocess.run(f'netsh interface ip add dns name="{interface}" addr={dns2} index=2', shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                # 切换到 A (DHCP)
                subprocess.run(f'netsh interface ip set address name="{interface}" source=dhcp', shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.run(f'netsh interface ip set dns name="{interface}" source=dhcp', shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            self.check_current_status()
        except subprocess.CalledProcessError:
            self.action_btn.configure(text="配置失败，请确保以管理员身份运行")
            
        self.action_btn.configure(state="normal")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    # 如果不是管理员权限，自动弹窗请求管理员权限重新拉起
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        app = IPSwitcherWinApp()
        app.mainloop()
