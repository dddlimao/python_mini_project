"""
python小项目1：加法
有疑问可添加微信：limao3000
"""

"""
用法 ： python add_v1.py NUM1 NUM2
示例： python add_v1.py 3 NUM2
"""

import sys
from typing import Any


def print_add(num1, num2):
    """
    计算a+b结果
    """
    print("{} + {} = {}".format(num1, num2, num1 + num2))


def get_args() -> tuple[Any, Any]:
    # 检查是否输入了正确数量的参数
    if len(sys.argv) != 3:
        print("用法: python add_v1.py <a> <b>")
        # 程序异常终止
        exit(code=1)
    # 第一个参数
    num1 = float(sys.argv[1])
    # 第二个参数
    num2 = float(sys.argv[2])
    return num1, num2


def main():
    # 获取参数
    num1, num2 = get_args()
    # 运算并打印结果
    print_add(num1, num2)


if __name__ == "__main__":
    main()
