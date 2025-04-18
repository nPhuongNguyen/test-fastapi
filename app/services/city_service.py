from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.city_repository import CityRepository
from app.schemas.city_schema import CityResponse

class CityService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.city_repo = CityRepository(db)

    async def get_cities(self) -> list[CityResponse]:  
        try:
            cities = await self.city_repo.get_all()
            return [CityResponse.model_validate(city) for city in cities]
        except Exception as e:
        # Log lỗi hoặc raise custom exception tùy theo yêu cầu
            raise Exception(f"Failed to fetch or validate cities: {str(e)}")

    async def get_city_by_id(self, city_id: int) -> CityResponse:  
        city = await self.city_repo.get_by_id(city_id)  # Đảm bảo phương thức trong repository là async
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"City with id {city_id} not found"
            )
        return CityResponse.model_validate(city)
