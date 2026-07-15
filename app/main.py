from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.api.routes import router


app = FastAPI(
    title="Swiss Ephemeris Integration",
    description="Swiss Ephemeris REST API",
    version="1.0.0",
)


@app.get("/", include_in_schema=False)
def home():
    return FileResponse("app/static/index.html")


app.include_router(router)