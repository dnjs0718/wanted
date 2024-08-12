from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from uvicorn import run


app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)


@app.get("/")
async def root():
    return {"message": "Health Check Success"}


if __name__ == "__main__":
    run(app="main:app", host="0.0.0.0", port=8001, reload=True)