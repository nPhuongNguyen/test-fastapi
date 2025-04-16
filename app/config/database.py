from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+aiomysql://root:12345@localhost/sakila"

# Tạo engine bất đồng bộ
engine = create_async_engine(DATABASE_URL, pool_recycle=3600, echo=False)

# Tạo async session
async_session = sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

# Base dùng như bình thường
Base = declarative_base()

# Hàm lấy session async
async def get_async_db():
    async with async_session() as session:
        yield session
