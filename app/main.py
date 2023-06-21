import uvicorn
from app import CONF, app


if __name__ == '__main__':
    PORT = CONF("DATA_SERVICE_PORT", cast=int, default=8000)
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=PORT,
        reload=True,
        proxy_headers=True)


@app.get("/")
def read_root():
    return {"hello": "world"}





