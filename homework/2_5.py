"""
5. 实现PYTHON版本的TREE

在之前的学习中大家都见到我用tree命令，它以树状图列出目录的内容：
```
❯ tree -L 1
.
├── setup.py
├── token.pkl
├── venv
└── zhuanlan.py

1 directory, 3 files

~/test2 t*
❯ tree -L 2
.
├── setup.py
├── token.pkl
├── venv
│   ├── bin
│   ├── include
│   ├── lib
│   └── pip-selfcheck.json
└── zhuanlan.py
```
使用Python实现tree命令，只支持--help(显示帮助信息)和-L参数即可(如果不指定-L参数则打印该目录前所有深度的目录和文件)。下面是帮助信息的输出：
```
❯ python3 5.py --help
usage: 5.py [-h] [-L LEVEL] PATH

list contents of directories in a tree-like format.

positional arguments:
  PATH                  directory path name

optional arguments:
  -h, --help            show this help message and exit
  -L LEVEL, --level LEVEL
                        Descend only level directories deep.
```
提示：os、argparse模块，要忽略.开头的文件和目录
"""
import os
import click


@click.command()
@click.option("--level", default=1, help="Descend only level directories deep")
@click.option("--path", help="directory path name")
def main(level, path):
    """list contents of directories in a tree-like format."""
    list_file(level, path)


def list_file(level, path, pos=0):
    path = "." if path is None else path
    dirs = os.listdir(path)
    for dir in dirs:
        click.echo("   " * pos + "|--" + dir)
        if os.path.isdir(dir) and level > 0:
            list_file(level - 1, dir, pos + 1)


main()
