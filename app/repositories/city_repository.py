from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.city_model import City
import asyncio
class CityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self)-> list[City]:
        try:
            result = await self.db.execute(select(City))
            # query = select(City.city_id, City.city)
            # result = await self.db.execute(query)
            await asyncio.sleep(1)
            return result.scalars().all()
            # return [City(city_id=row.city_id, city=row.city) for row in result]
        except Exception as e:
        # Log lỗi hoặc raise custom exception tùy theo yêu cầu
            raise Exception(f"Failed to fetch cities: {str(e)}")
    async def get_by_id(self, city_id: int):
        try:
            result = await self.db.execute(select(City).filter(City.city_id == city_id))
            return result.scalar_one_or_none()
        except Exception as e:
            print(f"Error in get_by_id: {e}")
            raise
