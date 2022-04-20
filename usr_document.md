# Pic Lite 使用教程

首先，您需要注册一个 sm.ms 账号，你可以前往 [sm.ms 官网](https://sm.ms/) 注册账号。

## 1. 设置 Token
运行 PicLite 后，使用 `token` 命令可以设置用户 token.

请输入 `token (username) (password)`，我们会自动获取 token。

```example
token ZhangSan 123456
your token is AbCdefGHIjklMNOpQRSTuvwxYZ123456(using now)
```

此时，我们会自动获取您的 token 并设置。

## 2. 上传图片
可以使用 `upload` 命令来上传图片。

用法：`upload (path)`。

你可以直接将文件拖入终端，会自动获取路径。

![](https://s2.loli.net/2022/04/20/bLVrPNeASmJdnXa.png)

当看到出现 `Upload Success` 字样的时候，说明图片上传完毕，否则请耐心等待。

图片会自动以 Markdown 格式复制，如 `![](https://s2.loli.net/2022/04/20/bLVrPNeASmJdnXa.png)`。

## 3. 更改图片复制格式
使用 `setformat (format)` 命令来更改复制的格式。

目前有两种格式：`markdown` 与 `plain`，其中 `markdown` 代表复制 `markdown` 格式链接，`plain` 表示仅复制链接。