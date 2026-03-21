# FastAPI框架基础

## 一、FastAPI框架简介

FastAPI是一个基于 Python 的高性能 Web 框架，专门用于快速构建 API 接口服务

- PythonWeb对比图

| 对比维度 |       FastAPI        |     Flask     |    Django    |
| :------: | :------------------: | :-----------: | :----------: |
|   性能   |    高（异步支持）    |      中       | 较低（同步） |
| 异步支持 |  ✔ 内置 async/await  |   ❌ 需扩展    |   ❌ 不原生   |
| 数据验证 | ✔ Pydantic 自动校验  |  ❌ 手动处理   | ✔ ORM 级验证 |
| 自动文档 |      ✔ 自动生成      |   ❌ 需插件    |   ❌ 需扩展   |
| 适用场景 | API、微服务、AI 推理 | 小型 web 项目 |   大型网站   |
- 同步与异步

[点击这里查看 FastAPI 示例代码](https://github.com/whchim/ai-learning/blob/main/02-fastapi/FastApi_code/case1.py)

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

![image_01](D:\ai-learning\02-fastapi\img\image_01.png)

## 四、参数简介

同一段接口逻辑，根据参数不同返回不同的数据

![image_02](D:\ai-learning\02-fastapi\img\image_02.png)

参数就是客户端发送请求时附带的额外信息和指令

参数的作用是让同一个接口能根据不同的输入，返回不同的输出，实现动态交互

- **参数分类**

  - 路径参数：

    位置：URL 路径的一部分 /look/{id}

    作用：指向唯一的，特定的资源

    方法：GET

  - 查询参数：

    位置：URL？ 之后 k1=v1&k2=v2

    作用：对资源集合进行过滤、排序、分页等操作

    方法：GET

  - 请求体：

    位置：HTTP 请求的消息体（body）中

    作用：创建、更新资源 携带大量数据，如：JSON

    方法：POST、PUT 等

## 五、路径参数_Path类型注解

FastAPI 允许为参数声明额外的信息和校验

| Path 参数             | 说明                        |
| --------------------- | --------------------------- |
| ...                   | 必填                        |
| gt/ge lt/le           | 大于/大于等于 小于/小于等于 |
| description           | 描述                        |
| min_length max_length | 长度限制                    |

## 六、查询参数_Query类型注解

声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数

参数形式与Path相同

| Query 参数            | 说明                        |
| --------------------- | --------------------------- |
| ...                   | 必填                        |
| gt/ge lt/le           | 大于/大于等于 小于/小于等于 |
| description           | 描述                        |
| min_length max_length | 长度限制                    |

## 七、请求体参数_Field类型注解

在HTTP协议中，一个完整的请求由三部分组成：

① 请求行：包含方法、URL、协议版本
② 请求头：元数据信息（Content-Type、Authorization等）
③ 请求体：实际要发送的数据内容

请求体参数的作用：创造、更新资源

| Field 参数  | 说明          |
| ----------- | ------------- |
| ...         | 必填          |
| gt/ge       | 大于/大于等于 |
| lt/le       | 小于/小于等于 |
| default     | 默认值        |
| description | 描述          |
| min_length  | 最小长度限制  |
| max_length  | 最大长度限    |

##  八、响应类型      

- 请求响应

  ![image_03](D:\ai-learning\02-fastapi\img\image_03.png)

- 响应类型

  默认情况下，FastAPI 会**自动**将路径操作函数返回的 **Python 对象**（字典、列表、Pydantic 模型等），经由 `jsonable_encoder` 转换为 **JSON** 兼容格式，并包装为 `JSONResponse` 返回。这省去了手动序列化的步骤，让开发者能更专注于业务逻辑。

  如果需要返回非 JSON 数据（如 HTML、文件流），FastAPI 提供了丰富的响应类型来返回不同数据。

  | 响应类型          | 用途                   | 示例                                |
  | ----------------- | ---------------------- | ----------------------------------- |
  | **JSONResponse**  | 默认响应，返回JSON数据 | `return {"key": "value"}`           |
  | **HTMLResponse**  | 返回HTML内容           | `return HTMLResponse(html_content)` |
  | PlainTextResponse | 返回纯文本             | `return PlainTextResponse("text")`  |
  | **FileResponse**  | 返回文件下载           | `return FileResponse(path)`         |
  | StreamingResponse | 流式响应               | 生成器函数返回数据                  |
  | RedirectResponse  | 重定向                 | `return RedirectResponse(url)`      |

- 响应类型设置方式

  - 装饰器中指定响应类

    场景：固定返回类型（HTML、纯文本等）

    ```python
    @app.get("/html", response_class=HTMLResponse)
    async def get_html():
        return "<h1>这是标题</h1>"
    ```

  - 返回响应对象

    场景：文件、图片、流式响应

    ```python
    @app.get("/file")
    async def get_file():
        file_path = "./files/1.jpeg"
        return FileResponse(file_path)
    ```

- 响应 HTML 格式

  设置响应类为 HTMLResponse，当前接口即可返回 HTML 内容

  ```python
  from fastapi.responses import HTMLResponse
  
  @app.get("/html", response_class=HTMLResponse)
  async def get_html():
      return "<h1>Hello World</h1>"
  ```

- 响应文件格式

  FileResponse 是 FastAPI 提供的专门用于高效返回文件内容（如图片、PDF、Excel、音视频等）的响应类。它能够智能处理文件路径、媒体类型推断、范围请求和缓存头部，是服务静态文件的推荐方式。

  ```python
  from fastapi.responses import FileResponse
  
  @app.get("/file")
  async def get_file():
      file_path = "./files/1.jpeg"
      return FileResponse(file_path)
  ```


## 九、自定义响应数据格式

**response_model** 是**路由操作装饰器**（如 @app.get 或 @app.post）的关键参数，它通过一个 **Pydantic 模型来严格定义和约束 API 端点的输出格式**。这一机制在提供自动数据验证和序列化的同时，更是保障数据安全性的第一道防线。

```python
from pydantic import BaseModel
class News(BaseModel):
    id: int
    title: str
    content: str

@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
	return {
		"id": id,
		"title": f"这是第{id}本书",
		"content": "这是一本好书"
}
```

注意：设定好的数据格式，响应的数据就必须是这个格式，否则会报错

## 十、异常处理

对于客户端引发的错误（4xx，如资源未找到、认证失败），应使用 fastapi.HTTPException 来中断正常处理流程，并返回标准错误响应。

```python
from fastapi import FastAPI, HTTPException

@app.get('/news/{id}')
async def get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="当前id不存在")
    return {"id": id}
```

