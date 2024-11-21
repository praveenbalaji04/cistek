import uvicorn
from core import create_app

from core.views import router


fast_app = create_app()

fast_app.include_router(router)


@fast_app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(fast_app, host="0.0.0.0", port=8000)
