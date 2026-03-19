# 字面量的写法
print(100) # 整数(int)
print(3.14) # 浮点数/小数(float)
print(True) # 布尔(bool)
print(False) # 布尔(bool)
print("Hello Python") # 字符串(str)
print("---------------------") # 字符串(str)
print(None) # 空值(NoneType)

# 布尔类型本质也是整数类型(True - 1 ; False - 0)
print(True + 1) # 2
print(Fales - 1) # -1

# 变量 
# 案例：
base = 20.7  # 基础播放量
incr = 50    # 每一个月的新增播放量

print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)

# 进阶：
base,incr = 20.7,50 # 同时赋值  

print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)