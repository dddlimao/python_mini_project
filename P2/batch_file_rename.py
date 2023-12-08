"""
python小项目1：批量重命名文件
有疑问可添加微信：limao3000
"""

"""
用法 ： python batch_file_rename.py [-h] WORK_DIR OLD_EXT NEW_EXT
示例： python batch_file_rename.py test .txt .pdf
"""

import argparse
import os
from typing import Any


def batch_rename(work_dir, old_ext, new_ext):
    # 遍历work_dir文件夹下的所有文件
    for filename in os.listdir(work_dir):
        # 分离文件名和扩展名，如：abc.pdf，会返回abc和.pdf
        root_name, file_ext = os.path.splitext(filename)

        # 找到需要修改的旧文件
        if old_ext == file_ext:
            # 构造新文件名
            newfile = root_name + new_ext

            # 重命名
            os.rename(
                src=os.path.join(work_dir, filename),
                dst=os.path.join(work_dir, newfile),
            )
    print("重命名完成")
    # 打印更新后的文件列表
    print(os.listdir(work_dir))


def get_args() -> tuple[Any, Any, Any]:
    # 创建并配置ArgumentParser对象
    parser = argparse.ArgumentParser(description="批量修改文件扩展名的工具")

    # 添加命令行参数，work_dir表示用来接收这个参数的变量名
    # metavar：用于在帮助消息中显示参数的名称。这里参数的名称为"WORK_DIR"。
    # type：指定参数的类型，这里是字符串类型。
    # nargs：指定参数的数量，这里设置为1，表示只接收一个参数值。
    # help：提供关于参数的描述和使用说明的帮助消息。
    parser.add_argument(
        "work_dir",
        metavar="WORK_DIR",
        type=str,
        nargs=1,
        help="the directory where to change extension",
    )
    parser.add_argument(
        "old_ext", metavar="OLD_EXT", type=str, nargs=1, help="old extension"
    )
    parser.add_argument(
        "new_ext", metavar="NEW_EXT", type=str, nargs=1, help="new extension"
    )

    # 获取命令行参数,将命令行参数以字典的形式返回
    args = vars(parser.parse_args())

    # 获取命令行参数，并进行预处理
    # 拿到目录路径
    work_dir = args["work_dir"][0]
    # 拿到旧扩展名
    old_ext = args["old_ext"][0]
    # 如果不是以点开头，添加点
    if old_ext and old_ext[0] != ".":
        old_ext = "." + old_ext
    # 拿到新扩展名
    new_ext = args["new_ext"][0]
    # 如果不是以点开头，添加点
    if new_ext and new_ext[0] != ".":
        new_ext = "." + new_ext

    return work_dir, old_ext, new_ext


def main():
    # 拿到处理后的命令行参数
    work_dir, old_ext, new_ext = get_args()

    # 批量重命名
    batch_rename(work_dir, old_ext, new_ext)


if __name__ == "__main__":
    main()
