from fastapi import FastAPI
from api import fighters


app = FastAPI()
app.include_router(fighters.router)

# !!!!make prefix api/v1/

@app.get("/health")
async def health():
	return {
		"status": "OK"
	}