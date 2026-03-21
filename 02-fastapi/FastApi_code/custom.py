# 自定义响应数据格式

from fastapi import FastAPI
from pyaudio import BaseMOdel

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

# 需求：新闻接口 -> 响应数据格式 id、title、content

class News(BaseMOdel):
    id : int
    tirle : str
    content : str

@app.get("/news/{id}",response_model=News)
async def get_news(id:int):
    return {
		"id": id,
		"title": f"这是第{id}本书",
		"content": "这是一本好书"
} 