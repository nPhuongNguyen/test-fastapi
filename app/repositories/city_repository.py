from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.city_model import City

class CityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        # Sử dụng session trực tiếp mà không cần async with
        result = await self.db.execute(select(City))
        return result.scalars().all()

    async def get_by_id(self, city_id: int):
        # Thực thi truy vấn với filter để lấy thành phố theo ID
        result = await self.db.execute(select(City).filter(City.city_id == city_id))
        return result.scalar_one_or_none()