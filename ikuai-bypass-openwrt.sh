#!/bin/sh
# openwrt/immortalwrt 24.12 内核6.12 amd64 x86 测试通过，项目源于https://github.com/joyanhui/ikuai-bypass
# 下面的脚本只支持ash sh bash zsh 不兼容fishshell 
# 更新或者下载最新版到 /opt/注意修改版本号CPU架构以及路径  =================================== start
# 最好逐行运行
#软件包获取更新 opkg update
#安装下载解压模块 opkg install wget unzip 

# 配置github代理 如果不可用请自行更换如果已经有直连github环境也可以去掉这行
export GhProxy=https://ghp.ci/

#创建切换到opt目录
mkdir -p /opt/ && cd  /opt/

#下载ikuai-bypass文件，v4.2是支持爱快3.7系统上限，爱快4.0及以上请使用V4.3以上版本.
wget -O ikuai-bypass-linux-amd64.zip "${GhProxy}https://github.com/joyanhui/ikuai-bypass/releases/download/v4.2.0/ikuai-bypass-linux-amd64.zip"
# 解压文件，删除无关文件
unzip ikuai-bypass-linux-amd64.zip && rm -rf ikuai-bypass-linux-amd64.zip && rm -rf README.md

# 自己上传config.yml到/opt, 给ikuai-bypass
加权限chmod +x /opt/ikuai-bypass

# 在线获取最新的演示配置，可能不兼容
wget ${GhProxy}https://raw.githubusercontent.com/joyanhui/ikuai-bypass/main/config.yml -O config.yml

# 更新或者下载最新版到 /opt/注意修改版本号CPU架构以及路径  =================================== end

# 手动执行一次 检查执行结果(需要注意自己配置的模式，下面这条是混合模式，默认运营商模式)
/opt/ikuai-bypass -c /opt/config.yml -r once -m ii

# 计划任务运行，计划任务添加命令
0 7 * * * /opt/ikuai-bypass -c /opt/config.yml -r cron -m ii

# 创建服务脚本运行，这段代码请整体复制后粘贴，或者使用vim nano编辑  ================================= start
cat > /etc/init.d/ikuai-bypass << \EOF
#!/bin/sh /etc/rc.common
START=99
start(){
        /opt/ikuai-bypass -r cron -m ii -c /opt/config.yml > /dev/null 2>&1 &
        echo "ikuai-bypass  is start"
}
 
stop(){
       killall -q -9  ikuai-bypass
       echo "ikuai-bypass  is stop"
}
EOF
# 创建服务脚本，这段代码请整体复制后粘贴，或者使用vim nano编辑  ================================= end

# 添加执行权限
chmod +x /etc/init.d/ikuai-bypass

# 服务设定为开机启动
service ikuai-bypass enable
# 手动启动 并查看进程是否存在
service ikuai-bypass start && ps |grep ikuai-bypass
# 手动停止
# service ikuai-bypass stop && ps |grep ikuai-bypass

# 卸载 清理
# service ikuai-bypass stop
# service ikuai-bypass disable
# rm -rf /etc/init.d/ikuai-bypass 
# rm -rf /opt/ikuai-bypass
# rm -rf /opt/config.yml
