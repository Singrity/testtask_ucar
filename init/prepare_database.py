from databasemanager import DatabaseManager
from db_models.incident_table import Incident


async def init_db():
    db_manager = DatabaseManager()
    await db_manager.create_tables()