# 14.3-helper

[English](README.en.md)

`14.3-helper` 是一个给 World of Warships 使用的战斗内辅助 UI mod。它会根据你当前选中的弹种和正在瞄准的目标，显示这发炮弹对目标不同部位的碾压或击穿结果。

当前包是独立包：放进 Aslain 的 `Custom_mods` 后不需要额外安装 TTaro、PnFMods 或其他依赖 mod。

## 功能

- AP：按 `口径 / 14.3` 判断是否可以碾压目标装甲。
- HE / SAP：按当前炮弹的穿深判断是否可以击穿目标装甲。
- 可在战斗中切换显示模式：`My gun` 显示我方当前炮弹打目标，`Enemy gun` 显示目标主炮能否伤到我的装甲部位。
- `Enemy gun` 模式下，目标有 SAP 时优先显示目标 SAP 穿深；没有 SAP 时，目标主炮口径小于 `283 mm` 显示 HE 穿深，`283 mm` 及以上显示 AP 碾压。
- 中文悬浮窗用 `攻` / `防` 前缀区分当前视角；防御视角下颜色按安全性显示，`×` 为绿色，`√` 为红色。
- 进战斗默认使用上一次保存的显示模式；按住 Alt 时临时切换到另一种模式，松开后恢复。
- 分开显示舰艏/舰艉、甲板、侧板、前后延伸装甲带。
- 延伸装甲带分别显示前后结果，例如 `Ext Bow √ Stern ×` / `延伸 前√ 后×`。
- 结果颜色按部位单独显示：可穿为绿色，不可穿为红色，临界或混合结果为黄色，无数据为灰色。
- 支持中文和英文界面，语言选项显示为 `ZH` / `EN`。
- 支持拖动、缩放、锁定位置、重置位置和调整背景透明度。

这个 mod 只读取游戏内已有的当前目标、当前弹种和本地装甲数据，不提供自动瞄准、不读取隐藏敌人、不注入游戏进程。

## 游戏内设置

战斗中悬浮窗口左侧有一个小齿轮按钮，可以打开 `14.3-helper` 的设置页。

可调项目包括：

- 语言：`ZH` / `EN`
- 显示模式：`My gun` / `Enemy gun`
- Alt 临时切换：按住 Alt 反转当前显示模式，不会改写保存的默认模式
- 界面缩放
- 是否锁定拖动
- 重置窗口位置
- 背景透明度

如果左上角的 TTaro 设置面板可见，也可以从里面选择 `14.3-helper`。

## 安装

### Aslain Custom Mods

1. 下载 release 里的 `14.3-helper_Aslain.zip`。
2. 放到：

```text
World of Warships\Aslain_Modpack\Custom_mods
```

3. 运行 Aslain Modpack 安装器。
4. 进战斗测试悬浮窗口和设置按钮。

### 本地测试

在仓库根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\install-local.ps1 -GameDir "S:\SteamLibrary\steamapps\common\World of Warships\bin\<当前版本号>"
```

安装后启动游戏一次，内置的 `ModsInstaller_4_3_1` 会把 battle UI 入口补进 `gui\battle_elements.xml`。

## 构建

先运行规则检查：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
```

然后构建 Aslain 包：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1
```

构建产物会生成在：

```text
dist\14.3-helper_Aslain.zip
```

## 更新装甲数据

装甲数据在：

```text
src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json
```

一键更新入口在：

```text
tools\update-armor-db-and-build.exe
```

双击它会在命令行窗口中生成候选数据库、列出新增/删除/变化 diff，输入 `Y` 后才会覆盖当前数据库，然后自动运行规则测试并打包到 `dist`。输出 zip 会带游戏版本后缀：

```text
dist\14.3-helper_Aslain-patch<游戏版本>.zip
```

底层生成和检查脚本在：

```text
tools\update-armor-db.ps1
```

手动流程：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 -Apply
```

如果需要从游戏参数重新提取数据，可以追加 `-ExtractGameParams`。这个步骤比较吃内存，建议只在需要同步新版本数据时运行。

## 准确性说明

整个程序是 vibe-coded。它经过了手动测试，但没有覆盖所有船、所有装甲块和所有版本变化，因此不承诺 100% 准确。

装甲数据库结合了自动提取、位置筛选和人工修正规则。但是对于复杂船体，尤其是分段装甲带延伸、局部甲板、水下无效装甲和航母多重侧板，仍然可能出现误判。

如果你发现错误，请带上以下信息提交 issue：

- 舰名和服务器语言
- 弹种和炮口径
- 游戏中实际显示的装甲截图
- mod 显示的结果

## 仓库结构

```text
src\
  res_mods\
    PnFMods\
      APOvermatchAssistant\      # 主逻辑和装甲数据库
      ModsInstaller_4_3_1\       # 独立安装所需的 UI patcher
    gui\
      unbound2\
        PnFMods\                 # 悬浮窗口和设置面板
        mods\                    # 拖动组件
tools\                           # 构建、安装和装甲数据脚本
dist\                            # 本地发布产物，不提交
```
