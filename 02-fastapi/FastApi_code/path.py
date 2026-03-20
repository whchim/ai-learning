# 路径参数和Path类型注解

from fastapi import FastAPI,Path
# 创建 FastAPI实例
app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

# 访问 /hello 响应结果 msg: 你好 FastAPI
@app.get("/hello")
async def get_hello():
    return {"msg": "你好 FastAPI"}

# 访问时id栏默认为必填项，即提示：required
@app.get("/book/{id}")
async def get_book(id: int):
    return {"id": id,"title": f"这是第{id}本书"}

# 练习：
# 需求：以用户 id 为路径参数设计 URL，要求响应结果包含用户 id 和名称（普通用户 id）
@app.get("/account/{id}")
async def get_account(id: str):
    return {"id": id,"title": f"普通用户{id}"}

# Path案例
@app.get("/book/{id}")
async def get_book(id: int = Path(...,gt = 0,lt = 101,description = "书籍ID，取值范围1-100")):
    return {"id": id,"title": f"这是第{id}本书"}

# 需求：查找书籍的作者，路径参数 name，长度范围 2-10
@app.get("/author/{name}")
async def get_name(name: str = Path(..., min_length=2, max_length=10)):
    return {"msg": f"这是{name}的信息"}

# 需求：定义两个接口，携带路径参数，并使用 Path 来实现类型注解
# 具体如下：
# 接口1：以 新闻分类 id 为参数设计 URL，id 范围为 1 ~ 100
# 接口2：以 新闻分类名称为参数设计 URL，分类名称长度为 2 ~ 10
@app.get("/journalism/{id}")
async def get_port1(id : int = Path(...,gt = 0,lt = 101,description = "id 范围为 1 ~ 100")):
    return {"id" : id}

@app.get("/journalism/{name}")
async def get_port2(id : int = Path(...,min_length = 2,max_length = 10,description = "分类名称长度为 2 ~ 10")):
    return {"name" : name}