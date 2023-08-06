from motor.motor_asyncio import AsyncIOMotorClient

from ..logging import LOGGER
from config import MONGO_DB_URI


LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database. Please check your MONGO_DB_URI and try again.")
    exit()
