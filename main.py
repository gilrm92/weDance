from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api import router as api_router

app = FastAPI()

origins = ["http://localhost:8000", ""]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

@app.get("/health")
async def ImAlive():
    return "I'm alive"

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8005, log_level="info", reload=True)
    print("running")