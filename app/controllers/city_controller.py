from fastapi import HTTPException, status
from app.services.city_service import CityService
from app.schemas.city_schema import CityResponse

async def get_cities(service: CityService) -> list[CityResponse]:
    """
    Lấy danh sách tất cả thành phố.
    """
    return await service.get_cities()  # Đảm bảo gọi await để nhận dữ liệu bất đồng bộ

async def get_city(city_id: int, service: CityService) -> CityResponse:
    """
    Lấy thông tin chi tiết thành phố theo ID.
    """
    city = await service.get_city_by_id(city_id)  # Đảm bảo gọi await để nhận dữ liệu bất đồng bộ
    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with id {city_id} not found"
        )
    return city
