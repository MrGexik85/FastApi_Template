from fastapi import FastAPI
import uvicorn

from settings import PORT, DEBUG

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello world!" }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)