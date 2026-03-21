# FastAPI框架进阶

## 一、中间件

作用：使用中间件为每个请求前后添加统一的处理逻辑（记录日志、身份验证、跨域、设置响应头、性能监控等）

- 1.多个接口都需要验证用户身份
- 2.多个接口都需要记录日志、性能参数

中间件（Middleware）是一个在每次请求进入 FastAPI 应用时都会被执行的函数。
它在请求到达实际的路径操作（路由处理函数）之前运行，并且在响应返回给客户端之前再运行一次。

![image_04](D:\ai-learning\02-fastapi\img\image_04.png)

定义：函数的顶部使用装饰器 **@app.middleware("http")**

执行顺序：自下而上

```python
@app.middleware("http")
async def middleware(requset,call_next):
	# requset 请求
	# call_next 传递请求给路径处理函数
	print('中间件开始处理 -- start')
	response = await call_next(requset)
	print('中间件处理完成 -- end')
	return response
```

