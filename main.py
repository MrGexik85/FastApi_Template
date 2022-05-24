from fastapi import FastAPI
import uvicorn

from core.settings import PORT, DEBUG
from v1.api import router

app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)