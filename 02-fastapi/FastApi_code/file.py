# 文件格式

from fastapi import FastAPI,Path
# 导入 FastAPI 提供的 FileResponse 响应类，用于返回 File 内容
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/img")
async def get_file():
    file_path = r"D:\ai-learning\02-fastapi\img\text1.jpeg"
    return FileResponse(file_path)
