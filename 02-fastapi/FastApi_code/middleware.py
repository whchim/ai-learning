# 中间件

from fastapi import FastAPI

app = FastAPI()

@app.middleware("http")
async def middleware2(requset,call_next):
	print('中间件2开始处理 -- start')
	response = await call_next(requset)
	print('中间件2处理完成 -- end')
	return response

@app.middleware("http")
async def middleware1(requset,call_next):
	print('中间件1开始处理 -- start')
	response = await call_next(requset)
	print('中间件1处理完成 -- end')
	return response

@app.get("/")
async def root():
    return {"message" : "Hello World"}
