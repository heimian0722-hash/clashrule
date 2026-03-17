**Clash防DNS泄漏 DNS配置、分流规则 全平台完整方案IOS\MAC\Android\Windows\Linux\Openwrt**

**1、clash-防DNS泄漏.yaml**
----clash多端共用配置文件模板（理论上适用于所有mihomo(clash.meta) 开发的软件 ）


**2、meta-rule.ini**
----**openclash软件免费，首选**
----
----openwrt/istoreos openclash 配置在线订阅转换模板，直接食用https://raw.githubusercontent.com/heimian0722-hash/clashrule/main/meta-rule.ini
<img width="951" height="320" alt="image" src="https://github.com/user-attachments/assets/011d9e6e-559a-4408-a260-c811f0b79944" />
<img width="956" height="719" alt="image" src="https://github.com/user-attachments/assets/c67a6bfb-dd7f-45dd-87c4-538201328d0f" />
<img width="750" height="257" alt="image" src="https://github.com/user-attachments/assets/f7220e03-2ced-4c1d-9590-f17c19e03cdc" />
<img width="992" height="238" alt="image" src="https://github.com/user-attachments/assets/33b139c2-8dab-42b5-8243-24058e58ca5d" />
GEO数据库、大陆白名单 全部开启订阅
<img width="935" height="805" alt="image" src="https://github.com/user-attachments/assets/b7bc6534-a9f7-4ca1-bc79-45da5ab6ddff" />
<img width="918" height="822" alt="image" src="https://github.com/user-attachments/assets/a289b37f-5968-431b-95b5-09d64209fd23" />
<img width="952" height="758" alt="image" src="https://github.com/user-attachments/assets/5dcb0c99-dd67-491d-a68c-58d415b6df22" />
三个DNS服务器组全部取消
<img width="1611" height="676" alt="image" src="https://github.com/user-attachments/assets/cc5651c5-cd86-4119-8ffb-bb5eb002a39f" />
订阅添加设置
<img width="629" height="777" alt="image" src="https://github.com/user-attachments/assets/fcd6c579-c95c-4bb8-b1b8-3375c8357e45" />
然后没有了，就以上

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
