# HTML 格式

from fastapi import FastAPI
# 导入 FastAPI 提供的 HTMLResponse 响应类，用于返回 HTML 内容
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

# 接口 -> 响应 HTML 代码
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题</h1>"