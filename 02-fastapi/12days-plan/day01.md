## 一.FastAPI框架简介
### 1.PythonWeb对比图
| 对比维度 |       FastAPI        |     Flask     |    Django    |
| :------: | :------------------: | :-----------: | :----------: |
|   性能   |    高（异步支持）    |      中       | 较低（同步） |
| 异步支持 |  ✔ 内置 async/await  |   ❌ 需扩展    |   ❌ 不原生   |
| 数据验证 | ✔ Pydantic 自动校验  |  ❌ 手动处理   | ✔ ORM 级验证 |
| 自动文档 |      ✔ 自动生成      |   ❌ 需插件    |   ❌ 需扩展   |
| 适用场景 | API、微服务、AI 推理 | 小型 web 项目 |   大型网站   |
### 2.同步与异步
[点击这里查看 FastAPI 示例代码](./FastApi/main.py)
## 第一个Fast小程序
    ### from fastapi import FastAPI

    ### app = FastAPI()

    ### @app.get("/")
    ### def read_root():
    ###     return {"Hello": "World"}

    ### @app.get("/items/{item_id}")
    ### def read_item(item_id: int, q: str | None = None):
    ###     return {"item_id": item_id, "q": q}    