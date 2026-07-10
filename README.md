# 14.3-helper

[English](README.en.md)

`14.3-helper` 是一个 World of Warships 战斗内辅助 UI mod。它会读取你当前选中的弹种、锁定目标、双方舰船数据和本地装甲数据库，显示这发炮弹对目标关键装甲区域的碾压或击穿判断。

当前发布包是独立包。把 zip 放进 Aslain 的 `Custom_mods` 后，不需要额外安装 TTaro、PnFMods 或其他前置 mod。

## 功能

- AP 碾压：先按 `口径 / 14.3` 判断是否可以碾压。能碾压就视为可以击穿。
- AP 穿深：不能碾压时，使用本地 AP 弹参数和预计算穿深表，结合当前距离、落弹角、相对航向角、装甲倾角和主装横向弯曲角，按弹道方向穿深与弹道路径等效厚度判断是否能击穿。
- 主装判断：目标可见且锁定时，实时读取己方和目标 `mapPosition.position/yaw` 计算相对航向角，再换算主装入射角。
- 主装数据：战列舰、巡洋舰、航母等使用提取出的主装带厚度和倾角范围；缺失时会回退侧板作为估算。驱逐舰没有独立主装带时，使用侧板作为主装参与 AP 判断。
- 潜艇目标：目标是潜艇时不显示面板。
- HE / SAP：按当前炮弹穿深判断是否可以击穿目标装甲。
- `My gun` / `Enemy gun`：`My gun` 显示我方当前弹种打目标；`Enemy gun` 显示目标主炮能否威胁我方装甲。
- `Enemy gun` 模式规则：目标有 SAP 时优先显示 SAP 穿深；没有 SAP 时，目标主炮口径小于 `283 mm` 显示 HE 穿深，`283 mm` 及以上显示 AP 碾压。
- AP 显示规则：根据落弹角和相对航向角，只显示当前最相关的甲板/侧板、主装，或艏艉/延伸带碾压结果。
- 结果符号：`√` 表示可以击穿，`×` 表示不能击穿，`△` 表示临界或部分可击穿，`?` 表示缺少数据。
- AP 临界区：穿深判断保留约 `5%` 误差余量，避免把经验公式边界值显示得过于绝对。
- 面板文本：主文本保持固定白色，用 `ATK` / `DEF` 区分攻击和防御视角；结果符号使用紧凑颜色区分。
- 支持中文和英文 UI，语言选项显示为 `ZH` / `EN`。
- 支持拖动、缩放、锁定位置、重置位置、调整背景透明度和默认关闭的加载诊断指示器。

这个 mod 只读取当前战斗目标、当前弹种和本地数据库。不提供自动瞄准，不显示隐藏敌人，不注入游戏进程。

## 设置

战斗中悬浮窗口左侧有一个 `CFG` 小按钮，可以打开 `14.3-helper` 自带设置页。这个入口不依赖 TTaro，TTaro 文件缺失或被其他 mod 覆盖时，主面板仍应照常显示。

可调项目：

- 语言：`ZH` / `EN`
- 显示模式：`My gun` / `Enemy gun`
- Alt 临时切换：按住 Alt 反转当前显示模式，松开后恢复，不会改写保存的默认模式
- 界面缩放
- 是否锁定拖动
- 重置窗口位置
- 背景透明度
- 加载诊断指示器：默认关闭，排查“mod 未加载”与“没有可用目标”时再打开

如果左上角 TTaro 设置面板可见，也可以从里面选择 `14.3-helper`。

## 安装

### Aslain Custom Mods

1. 下载 GitHub Releases 里的 Aslain zip，例如 `14.3-helper_v0.5.1_Aslain-patch15.5.zip`。
2. 把这个 zip 原样放进：

```text
World of Warships\Aslain_Modpack\Custom_mods
```

3. 运行 Aslain Modpack 安装器。
4. 进战斗测试悬浮窗口、设置按钮和目标锁定后的显示。

zip 内部结构从 `res_mods\...` 开始，直接放入 `Custom_mods` 即可一次安装正确。

如果旧版本已安装但战斗中没有浮窗，安装 `0.5.1` 会强制 ModsInstaller 重新补 UI 入口。快速排查可以检查游戏目录下的 `res_mods\gui\battle_elements.xml` 是否包含 `elementName="OA_APOvermatchAssistant"`。

### 本地测试安装

在仓库根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\install-local.ps1 -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

脚本会复制到最新的数字版本目录 `bin\<版本号>\res_mods`。如果该目录下已经有 `gui\battle_elements.xml`，脚本会直接补上 `OA_APOvermatchAssistant` battle UI 入口；否则内置的 `ModsInstaller_4_3_1` 会在游戏启动时补入口。

## 构建

完整检查：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test.ps1
```

只跑规则回归：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
```

构建 Aslain 包：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1
```

构建时会提示输入游戏 patch 版本；直接回车会使用项目里的 target 游戏版本 `15.5`。也可以显式指定：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1 -PatchVersion 15.5
```

输出示例：

```text
dist\14.3-helper_v0.5.1_Aslain-patch15.5.zip
```

构建并直接复制到 Aslain `Custom_mods`：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1 -PatchVersion 15.5 -AslainCustomModsDir "S:\SteamLibrary\steamapps\common\World of Warships\Aslain_Modpack\Custom_mods"
```

## 更新装甲数据库

装甲数据库在：

```text
src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json
```

普通更新推荐使用统一入口：

```text
tools\update-armor-db-and-build.exe
```

双击后会打开命令行窗口，菜单包含：

- 更新数据库并构建 zip
- 手动编辑装甲数据
- 提取并分析主装带
- 退出

更新流程会：

1. 从当前游戏版本生成候选数据库。
2. 提取 AP 弹参数、HE/SAP 穿深、装甲厚度、主装倾角和横向角范围。
3. 列出新增、删除和变化的船只字段。
4. 等待 `Y` / `N` 确认。
5. 输入 `Y` 后覆盖当前数据库，并把旧数据库备份到 `tools\armor_snapshots`。
6. 同步 Python 数据库和 Unbound 内嵌数据库。
7. 运行测试。
8. 构建 zip 到 `dist`。

如果只想看 diff、不覆盖数据库，输入 `N` 退出。候选文件和 diff 会保留在：

```text
build\armor-update
```

需要自定义参数时，可以直接运行 PowerShell 脚本。例如复用已有 GameParams JSON：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db-and-build.ps1 -GameParamsJson "C:\tmp\GameParams_ASIA.json"
```

底层报告脚本是 `tools\update-armor-db.ps1`。不加 `-Apply` 时只生成报告；加 `-Apply` 才会覆盖数据库。`-ExtractGameParams` 会从游戏文件重新提取数据，内存占用较高，建议只在同步新游戏版本时使用。

### Steam 版本自动检查

`tools\check-steam-wows-update.ps1` 用于无人值守检查 Steam 安装状态、更新装甲数据库、运行完整测试并打包。它只在干净的 `develop` 上修改并本地提交允许的生成文件，不会推送。

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\check-steam-wows-update.ps1 -Mode SelfTest
powershell -ExecutionPolicy Bypass -File .\tools\check-steam-wows-update.ps1 -Mode DryRun
powershell -ExecutionPolicy Bypass -File .\tools\check-steam-wows-update.ps1 -Mode CheckAndBuild
```

运行状态保存在忽略 Git 的 `build\automation\wows-release-state.json`。发布成功或失败后，Codex 分别使用 `MarkPublished` 或 `MarkPublishFailed` 更新状态，防止重复回复。

## 准确性说明

AP 穿深使用解包 AP 弹参数和经验公式生成的近似穿深表，用于游戏内快速判断，不是官方逐像素弹道系统复刻。

装甲数据库结合了自动提取、几何筛选、主装倾角分析和人工修正规则。复杂船体仍可能误判，尤其是多段主装、弯曲装甲带、穹甲、内层装甲、炮塔、局部甲板、水线以下命中路径和航母多层侧板。

当前 AP 主装判断只判断目标主装甲带的弹道路径等效厚度，不处理穹甲、甲板下内层装甲、炮塔和复杂水下弹道。

如果你发现错误，请提交 issue 并带上：

- 船名和游戏客户端语言
- 弹种、炮口径和距离
- 目标相对角度或截图
- 游戏内装甲截图
- mod 显示的结果

## 仓库结构

```text
src\
  res_mods\
    PnFMods\
      APOvermatchAssistant\      # 主逻辑、辅助模块和装甲数据库
      ModsInstaller_4_3_1\       # 独立安装所需 UI patcher
    gui\
      unbound2\
        PnFMods\                 # 悬浮窗口和设置面板
        mods\                    # 拖动组件
tools\                           # 构建、安装、数据库更新和主装分析工具
dist\                            # 本地发布产物，不提交
```
