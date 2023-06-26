from fastapi import FastAPI
from logging_monitor.routers import api

app = FastAPI(title="logging-monitor-api")
app.include_router(api.router, prefix="/api")
