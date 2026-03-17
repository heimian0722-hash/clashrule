**Clash防dns泄漏 DNS配置、分流规则**

**1、clash-防DNS泄漏.yaml**
----clash多端共用配置文件模板（理论上适用于所有mihomo(clash.meta) 开发的软件 ）


**2、meta-rule.ini**
----**openclash软件免费，首选**
----openwrt/istoreos openclash 配置在线转换，直接食用https://raw.githubusercontent.com/heimian0722-hash/clashrule/main/meta-rule.ini

**3、全局扩展脚本防DNS泄露-xiaolin007.js**
----**clash verge软件免费，首选**
----Windows/MAC-clash verge 全局扩展脚本  .js脚本文件
----优先用xiaolin007分地区版本，acrtion版本需要开启严格路由，xiaolin007版本可直接使用
----代理-规则-全局扩展脚本，右键编辑，直接粘贴替换原来的，保存即可

**4、Stash-防DNS泄露.ini**
----**Stash软件收费**，ios美区5.99刀，mac端更贵188，但是确实功能强大
----iOS/MAC-stash自行复制代码，需要添加机场信息，改成yaml导入Stash，选用更新，启动

**5、karing（支持IOS\MAC\Android\Windows\Linux**
----**karing软件免费，首选**
----设置好DNS及分流即可达成效果，开发项目地址https://github.com/KaringX
----karing Android/ios/Windows测试通过没问题，但mac端存在dns泄露（可能我mac系统版本太老的问题，目前设备较老，就只能到13），mac/linux自行测试使用；
