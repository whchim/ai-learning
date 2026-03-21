# 字符串案例
# 需求：
# 根据个人实际情况，输出一段自我介绍字符串，格式如下：
# "大家好，我是东哥，今年18岁，学习的专业是软件工程，爱好Python、C++"

# 字符串拼接 --> str(int数字) --> 将int类型的数字转为字符串
name = "东哥"
age = 18
pro = "软件工程"
hobby = "Python、C++"
message = "大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro + "，爱好" + hobby

print(message)

# 字符串格式化 --> %s 占位符
name = "东哥"
age = 18
pro = "软件工程"
hobby = "Python、C++"
message = "大家好，我是 %s,今年 %s岁,学习的专业是 %s,爱好 %s" % (name,age,pro,hobby)

print(message)

# 字符串格式化 --> f".. {变量名/表达式} .."
name = "东哥"
age = 18
pro = "软件工程"
hobby = "Python、C++"
message = f"大家好，我是 {name},今年 {age}岁,学习的专业是 {pro},爱好 {hobby}"

print(message)