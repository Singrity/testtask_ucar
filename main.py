import logging


#from core.logger import setup_logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.create_incident import router as create_incident_router
from routers.get_incident import router as get_incident_router
from routers.update_incident import router as update_incident_router

#setup_logger()
logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware
)

app.include_router(create_incident_router)
app.include_router(get_incident_router)
app.include_router(update_incident_router)
