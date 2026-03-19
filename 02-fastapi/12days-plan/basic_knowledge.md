## 一、FastAPI框架简介
FastAPI是一个基于 Python 的高性能 Web 框架，专门用于快速构建 API 接口服务

### 1.PythonWeb对比图

| 对比维度 |       FastAPI        |     Flask     |    Django    |
| :------: | :------------------: | :-----------: | :----------: |
|   性能   |    高（异步支持）    |      中       | 较低（同步） |
| 异步支持 |  ✔ 内置 async/await  |   ❌ 需扩展    |   ❌ 不原生   |
| 数据验证 | ✔ Pydantic 自动校验  |  ❌ 手动处理   | ✔ ORM 级验证 |
| 自动文档 |      ✔ 自动生成      |   ❌ 需插件    |   ❌ 需扩展   |
| 适用场景 | API、微服务、AI 推理 | 小型 web 项目 |   大型网站   |
### 2.同步与异步
[点击这里查看 FastAPI 示例代码](https://github.com/whchim/ai-learning/blob/main/02-fastapi/FastApi_code/main1.py)

## 二、第一个Fast小程序

```python
from fastapi import FastAPI  # 导入 FastAPI 框架，用于创建 Web API

app = FastAPI()  # 创建一个 FastAPI 应用实例

@app.get("/")  # 定义一个 GET 请求路由，路径为根路径 "/"
def read_root():  # 定义处理根路径请求的函数
    return {"Hello": "World"}  # 返回一个 JSON 响应，内容为 {"Hello": "World"}

@app.get("/items/{item_id}")  # 定义一个 GET 请求路由，路径包含动态参数 {item_id}
def read_item(item_id: int, q: str | None = None):  # 定义处理该路径请求的函数，接收两个参数：
    # item_id: 路径参数，类型为整数（int）
    # q: 查询参数，类型为字符串或 None，默认值为 None
    return {"item_id": item_id, "q": q}  # 返回一个包含 item_id 和 q 的 JSON 响应
```

## 三、路由

路由就是 URL 地址和处理函数之间的映射关系，它决定了当用户访问某个特定网址时，服务器应该执行哪段代码来返回结果。

FastAPI的路由定义基于 Python 的装饰器模式

![image_01](D:\ai-learning\02-fastapi\.img\image_01.png)

