# 请求体参数和Field类型注解

# 导入 FastAPI 和 Pydantic 的核心类
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

# 注册: 用户名和密码 ——> str
app = FastAPI()

# 定义数据模型 (Pydantic Model)
# 这个类用于定义请求体（Request Body）的数据结构和类型校验规则
class User(BaseModel):
    # 定义用户名字段，类型为字符串 (str)
    # FastAPI 会自动校验传入的 JSON 中是否包含此字段且为字符串
    username: str
    
    # 定义密码字段，类型为字符串 (str)
    # 如果传入的不是字符串（例如数字或布尔值），FastAPI 会返回 422 验证错误
    password: str
    
    # 【可选】如果你需要添加验证规则（如最小长度、描述等），可以使用 Field
    # 例如：
    # username: str = Field(..., min_length=3, description="用户名至少3个字符")
    # password: str = Field(..., min_length=6, description="密码至少6个字符")

# 定义路由接口
# @app.post("/register") 表示这是一个处理 POST 请求的接口，路径为 /register
# POST 通常用于创建新资源（如注册新用户）
@app.post("/register")
async def register(user: User):
    """
    用户注册接口   
    参数:
        user: User 模型实例。
              FastAPI 会自动从请求体 (JSON) 中提取数据，
              并尝试将其解析为 User 对象。
              如果数据不符合 User 定义的类型，会自动返回 422 错误。
    返回:
        返回接收到的 user 对象。
        FastAPI 会自动将 Pydantic 模型转换为 JSON 格式响应给客户端。
    """
    # 当前代码直接原样返回接收到的数据，用于测试接口连通性
    return user    

# 需求：设计接口新增图书，图书信息包含：书名、作者、出版社、售价
class Book(BaseModel):
    bookname: str
    author: str
    press: str
    price: float

@app.post("/add_library")
async def add_book(book: Book):
    return {"message": "图书添加成功", "data": book}        

# 注册: 用户名和密码  用户名默认值为 张三 
class User(BaseModel):
    username: str = Field(...,default = "张三",min_length = 2,max_length = 10,description = "字符长度为2-10")
    password: str

@app.post("/register")
async def register(user: User):
    return user    