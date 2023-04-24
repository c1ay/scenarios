import ast

# 目标函数名
target_function = "eval"

filename = "/home/labex/project/basic_functionality.py"

# 解析代码并遍历语法树
with open(filename, "r") as file:
    tree = ast.parse(file.read())
    # 遍历所有函数调用节点
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and hasattr(node.func, "id"):
            if node.func.id == target_function:
                assert False
