from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
  return {
    	"status": "200 OK"
  }


obj = {
  "test": "test"
}

fighters = []

@app.get("/fighters")
def get_fighters():
  return fighters

@app.get("/fighters/{fighter_id}")
def get_fighter(fighter_id: int):
  for fighter in fighters:
    if fighter.id == fighter_id:
      return fighter
  # ERROR
/api/v1/fighters
/api/v1/fighters/{fighter_id}



# @app.post()


# @app.put()


# @app.delete()