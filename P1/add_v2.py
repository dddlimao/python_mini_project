"""
python小项目1：加法
有疑问可添加微信：limao3000
"""

"""
用法 ： python batch_file_rename.py work_dir old_ext new_ext
示例： python batch_file_rename.py test .txt .pdf
"""

import argparse
import os
from typing import Any


def print_add(num1, num2):
    """
    计算a+b结果
    """
    print("{} + {} = {}".format(num1, num2, num1 + num2))


def get_args() -> tuple[Any, Any]:
    """
    创建并配置ArgumentParser对象
    """

    # 使用help时的帮助信息
    parser = argparse.ArgumentParser(description="加法计算器")
    parser.add_argument("num1", metavar="NUM1", type=float, nargs=1, help="第一个加数")
    parser.add_argument("num2", metavar="NUM2", type=float, nargs=1, help="第二个加数")
    args = vars(parser.parse_args())
    num1 = args["num1"][0]
    num2 = args["num1"][0]
    return num1, num2


def main():
    # 获取参数
    num1, num2 = get_args()
    # 运算并打印结果
    print_add(num1, num2)


if __name__ == "__main__":
    main()
