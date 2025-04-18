from fastapi import APIRouter, Depends, Query
from app.controllers.city_controller import get_cities, get_city
from app.schemas.city_schema import CityResponse
from app.dependencies import get_city_service
import asyncio

router = APIRouter(tags=["Cities"])

@router.get("/cities/", response_model=list[CityResponse])
async def list_cities(service=Depends(get_city_service)):
    await asyncio.sleep(1)
    return await get_cities(service)  # ✅ await để gọi hàm async

@router.get("/cities/{city_id}", response_model=CityResponse)
async def get_single_city(city_id: int, service=Depends(get_city_service)):
    return await get_city(city_id, service)  # ✅ await để gọi hàm async
