from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.routes import router

settings = Settings()

def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(**settings.fastapi_kwargs)

    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

    app.include_router(router)

    return app


server = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(server, host="127.0.0.1", port=8000)