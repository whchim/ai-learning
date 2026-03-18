from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# 同步-需要消耗10s
@app.get("/sync")
def fun_sync():
    start = time.time()
    for i in range(10):
        time.sleep(1)
    end = time.time()
    return {"time": f'{end-start:.2f}s'}

# 异步-需要消耗1s
@app.get("/async")
async def fun_async():
    start = time.time()
    tasks = [asyncio.sleep(1) for i in range(10)]
    await asyncio.gather(*tasks)
    end = time.time()
    return {"time": f'{end-start:.2f}s'}
