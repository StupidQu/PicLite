# PicLite
## 1. 介绍
Pic Lite 是 Linux 系统下的 Pic Go 轻量化替代品，它具有简洁、低功耗等特点，由于使用 Python 语言编写，理论上支持 Windows 系统，如果不支持 Windows 系统，请提交 Issue。

Pic Lite 源代码采用 GPL-3.0 协议开源，如果您想要 Pic Lite 变得更好，可以提交 Issue 或 Pull-Request。
## 2. 安装流程
### 方法一
本方法适合 ubuntu 系统用户使用，测试环境 Ubuntu 20.04LTS。

点击左侧“发行版”，找到适合的版本中的 `PicLite-ubuntu-v(x.x.x)`，建议使用最新的 Release 版本或 Beta 版本，通常不要使用 Alpha 版本，除非你可以自行寻找错误并提交 Issue.

下载该文件。

打开终端并进入该文件所在目录（如下载至 `/home/PicLite-ubuntu-v(x.x.x)`）则输入 `cd /home/`。

使用 `./PicLite-ubuntu-v(x.x.x)` 运行 PicLite。

**注意，以上文件名中的 `(x.x.x)` 需要以实际的版本号替换。**
### 方法二
本方法适合 Windows 用户与其他无法使用上述方法的用户。

选择以 Zip 格式下载本仓库。

![](https://s2.loli.net/2022/04/20/ENnjMWl92QPGJYo.png)

下载后将源代码解压，进入解压后的目录，使用 `python main.py` 命令即可开启 PicLite。

## 3. 使用方法

可参见 [usr_document.md](usr_document.md) 文件。

## 4. 参与编辑
我们欢迎您参与到 Pic Lite 的编写！您可以 Fork 本项目并编辑，然后提交 Pull-Request。

您也可以使用本项目进行二次开发，但请注意，您编辑后的项目仍需要使用 GPL-3.0 协议开源，详情见 GPL-3.0 协议内容。