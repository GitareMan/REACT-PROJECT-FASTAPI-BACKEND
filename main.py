
import uvicorn
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from router import router as api_router

app = FastAPI(debug=True)

origins = [
    "http://localhost:8080",
    # Add more origins here
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)