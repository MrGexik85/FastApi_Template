from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/v1')

@router.get(
    path='/',
)
async def root():
    return JSONResponse({ "message": "Not implemented" }, status_code=400)