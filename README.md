# 14.3 Helper

**简体中文** | [English](README.en.md)

[![Version](https://img.shields.io/badge/version-0.2.26-blue.svg)](#发布)
[![World of Warships](https://img.shields.io/badge/World%20of%20Warships-battle%20UI-informational.svg)](https://worldofwarships.com/)
[![Aslain custom mod](https://img.shields.io/badge/Aslain-custom%20mod-orange.svg)](https://aslain.com/)

**14.3 Helper** 是一个 Aslain 的《战舰世界》战斗 UI 插件。它会在你锁定敌舰后，根据当前选择的 AP / HE / SAP，显示目标外部装甲是否能被当前炮弹击穿或碾压。


## 功能

- 只在使用主炮锁定目标时显示。
- AP 使用游戏内碾压规则：`口径 / 14.3 >= 装甲厚度`。
- HE 和 SAP 使用穿深规则，对同一组装甲区域进行判断。
- 战斗中显示符号：
  - `√` 表示可以碾压/击穿。
  - `×` 表示不可以碾压/击穿。
  - `△` 表示部分区域可以、部分区域不可以。
  - `?` 表示数据异常。
- 战斗面板显示四行：
  - `艏艉`：船头 / 船尾外板。
  - `甲板`：露天甲板 / 主要水平甲板。
  - `侧板`：主装甲带上方的上侧板。
  - `装甲延伸`：船头装甲延伸 / 破冰带类装甲。
- 面板可拖动，并可通过 PnFMods / TTaro 模组配置 UI 调整透明度。

## 合规边界

本项目按《战舰世界》官方模组政策的方向设计：

- 使用常规客户端模组结构：`res_mods`、`PnFMods` 和 Unbound UI。
- 只读取客户端 ModAPI / DataHub 路径暴露的玩家当前战斗状态。
- 使用从本地游戏客户端生成的版本化装甲参考数据库。
- 不计算提前量、瞄准点、弹道飞行预测或目标运动解。
- 不读取未点亮船只、隐藏位置或服务器端才有的信息。
- 不修改游戏二进制文件，不注入 DLL，不修改原始游戏文件。

相关政策：

- [Wargaming World of Warships Mod Policy](https://wargaming.net/support/en/products/wows/article/10720/)
- [Wargaming Prohibited Software Policy](https://wargaming.net/support/en/products/wows/article/10721/)

本项目与 Wargaming 无从属、认可或官方合作关系。

## 安装

### Aslain Custom Mods

推荐用这个方式测试和分发。

1. 下载发布 zip，例如 `14.3-Helper_Aslain_v0.2.26.zip`。
2. 不要解压。
3. 把 zip 放到：

```text
World of Warships\Aslain_Modpack\Custom_mods\
```

4. 重新运行 Aslain 安装器。
5. 启动游戏并进入战斗。

### 手动安装

只有不使用 Aslain 时才建议手动安装。

1. 把 zip 解压到当前游戏版本目录：

```text
World of Warships\bin\<current_build>\
```

2. 解压后应存在这些路径：

```text
World of Warships\bin\<current_build>\res_mods\gui\unbound2\PnFMods\APOvermatchAssistant.unbound
World of Warships\bin\<current_build>\res_mods\PnFMods\APOvermatchAssistant\Main.py
```

## 使用方式

1. 进入战斗。
2. 选择 AP、HE 或 SAP 主炮弹药。
3. 锁定或瞄准辅助锁定一艘敌舰。
4. 在准星附近读取四行结果。


## 构建

需求：

- Windows PowerShell
- Node.js，用于快速数据库生成和 Unbound 数据生成
- `wowsunpack`，仅在需要重新提取客户端数据时使用

运行规则测试并构建 Aslain zip：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\build.ps1
```

构建产物写入：

```text
dist\APOvermatchAssistant_Aslain.zip
```

## 本地开发安装

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\install-local.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

## 装甲数据更新

装甲数据库设计成可以在每次游戏更新后重新生成。原始客户端提取可能比较占内存，所以提取步骤默认不会自动运行。

只生成差异报告：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

生成报告并应用更新后的数据库：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -Apply
```

只有当前版本缺少缓存 `GameParams` 时，才显式提取新数据：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -ExtractGameParams `
  -Apply
```

差异报告写入：

```text
build\armor-update\
```

大型客户端提取缓存会被 git 忽略，不应提交到仓库。

## 项目结构

```text
src/res_mods/PnFMods/APOvermatchAssistant/Main.py
src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.json
src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.py
src/res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound
src/res_mods/PnFMods/ModsInstaller_4_3_1/mods/APOvermatchAssistant.xml
tools/build.ps1
tools/install-local.ps1
tools/update-armor-db.ps1
tools/generate-armor-db-fast.mjs
tools/normalize-deck-values.mjs
```

内部模块名仍为 `APOvermatchAssistant`，用于兼容现有 PnFMods 结构。公开项目名为 `14.3 Helper`。

## 反馈错误数据

反馈装甲或弹药判断错误时，请尽量提供：

- 游戏版本 / build。
- 你使用的船和当前弹药类型。
- 锁定的目标船。
- 插件面板截图。
- 游戏内装甲查看器截图或文字说明。
- 你认为 `艏艉`、`甲板`、`侧板` 或 `装甲延伸` 应该显示的结果。

有效的装甲修正应能从当前客户端数据或游戏内装甲查看器复现。

## 已知限制

- 《战舰世界》更新可能改变 UI API、船只 ID、装甲标签或弹药数据。大版本更新后应重新生成数据库。
- 不保证与所有其他 UI 模组兼容。
- 战斗面板的装甲分类经过简化，目标是快速阅读。精确几何结构仍以游戏内装甲查看器为准。
- `?` 表示本地数据库或实时战斗状态没有提供足够数据，无法可靠判断。

## 发布

当前测试版本：

```text
v0.2.26
```

推荐发布流程：

1. 为当前游戏版本重新生成或对比装甲数据。
2. 运行 `tools\test-rule.ps1`。
3. 运行 `tools\build.ps1`。
4. 将生成的 Aslain zip 上传为 GitHub Release 附件。
5. 在训练房用 AP、HE、SAP 和鱼雷状态测试。

## 许可证

目前还没有声明开源许可证。在添加 license 文件之前，仓库所有者保留全部权利。
