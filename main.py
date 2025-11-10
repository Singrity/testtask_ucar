import logging
from contextlib import asynccontextmanager
from databasemanager import DatabaseManager
from utils.setup_logger import setup_logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.create_incident import router as create_incident_router
from routers.get_incident import router as get_incident_router
from routers.update_incident import router as update_incident_router

setup_logger()
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Incident Management API",
    description="API for managing incidents",
    version="1.0.0",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_incident_router)
app.include_router(get_incident_router)
app.include_router(update_incident_router)


