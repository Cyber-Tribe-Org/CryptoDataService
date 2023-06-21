from starlette.config import Config
from starlette.datastructures import Secret

CONF = Config(".env")

# FastAPI Server
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title=CONF("DATA_SERVICE_NAME", default="Data Management Service"),
    version = CONF("DATA_SERVICE_VERSION", default='v0.0.0')
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)








