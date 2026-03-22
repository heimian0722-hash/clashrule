#!/bin/sh
# openwrt/immortalwrt 24.10.5 内核6.6.122 x64 测试通过
# 下面的脚本只支持ash sh bash zsh 不兼容fishshell 
# 更新或者下载最新版到 /opt/注意修改版本号CPU架构以及路径  =================================== start
# 最好逐行运行
#软件包更新 opkg update
#安装下载解压模块 opkg install wget unzip 
export GhProxy=https://ghp.ci/  # 配置github代理 如果不可用请自行更换如果已经有直连github环境也可以去掉这行

# 切换到opt目录
mkdir -p /opt/ && cd  /opt/
#下载ikuai-bypass文件，v4.2是支持爱快3.7系统上限，爱快4.0请使用最新版本的，去github找最新版本
wget ${GhProxy}https://github.com/joyanhui/ikuai-bypass/releases/download/v4.2.0/ikuai-bypass-linux-amd64.zip

# 解压可能会报错未找到文件，因为下载的文件名字没有改成对应名字，通过文件管理工具找到/opt目录刚下载的文件，改名字为ikuai-bypass-linux-amd64.zip
unzip ikuai-bypass-linux-amd64.zip && rm -rf ikuai-bypass-linux-amd64.zip && rm -rf README.md

# 使用版本内的配置文件config.yml 改名为ikuai-bypass.yml ，或者自己写好配置文件直接上传/opt
mv config.yml  ikuai-bypass.yml 
# 或者用最新的演示配置
rm -rf ikuai-bypass.yml && rm -rf config.yml
wget ${GhProxy}https://raw.githubusercontent.com/joyanhui/ikuai-bypass/main/config.yml -O ikuai-bypass.yml
# 更新或者下载最新版到 /opt/注意修改版本号CPU架构以及路径  =================================== end

# 手动执行一次 检查执行结果
#   /opt/ikuai-bypass -r 1 -c /opt/ikuai-bypass.yml

# 创建服务脚本，这段代码请整体复制后粘贴，或者使用vim nano编辑  ================================= start
cat > /etc/init.d/ikuai-bypass << \EOF
#!/bin/sh /etc/rc.common
START=99
start(){
        /opt/ikuai-bypass -r cronAft  -c /opt/ikuai-bypass.yml > /dev/null 2>&1 &
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
# rm -rf /opt/ikuai-bypass.yml

