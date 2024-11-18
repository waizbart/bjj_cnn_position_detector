import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.analyze import router as analyze_router
from api.routes.websocket import router as websocket_router

from api.config.logging import setup_logging
from api.services.pose_service import PoseService

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="BJJ Pose Analysis API", version="1.0.0")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pose_service = PoseService()

app.state.pose_service = pose_service


@app.get("/", summary="Verificar status da api")
def hello():
    return {
        "message": "Hello from bjj IA api"
    }


app.include_router(analyze_router)
app.include_router(websocket_router)
