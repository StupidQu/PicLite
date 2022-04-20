# main.py
这是 PicLite 的主程序位置。

# command.py
这是命令执行的文件。

# config.py
这个文件用于操作 `{path}/settings.conf` 文件。该文件是 PicLite 的配置文件。

## get_config(section: string, key: string): string
根据 `section, key` 查找对应的值。
## set_config(section: string, key: string, text: string): void
将 `section` 下的 `key` 设置为 `text`。
## is_exist(section: string): bool 
判断 `section` 是否存在。
## create_section(section: string): void
新建 `section`。