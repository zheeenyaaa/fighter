from fastapi import FastAPI
from pydantic import BaseModel

class FighterModel(BaseModel):
   id: int
   speed: int

class FighterInput(BaseModel):
   speed: int

app = FastAPI()

# make prefix api/v1/

@app.get("/health")
async def health():
  return {
    	"status": "200 OK"
  }

fighter1 = FighterModel(id = 1, speed = 100)
fighter2 = FighterModel(id = 2, speed = 200)

fighters = [fighter1, fighter2]

@app.get("/fighters")
def get_fighters() -> list[FighterModel]:
  return fighters

@app.get("/fighters/{fighter_id}")
def get_fighter(fighter_id: int) -> FighterModel:
  for fighter in fighters:
    if fighter["id"] == fighter_id:
      return fighter
  # ERROR

@app.post("/fighters/")
def create_fighter(fighter: FighterInput) -> FighterModel:
	new_fighter_id = len(fighters) + 1
	new_fighter = FighterModel(id = new_fighter_id, speed = fighter.speed)
	fighters.append(new_fighter)
	print(fighters)
	return new_fighter


# @app.put()

@app.delete("/fighters/{fighter_id}")
def delete_fighter(fighter_id: int) -> FighterModel:
	for fighter in fighters:
		if fighter.id == fighter_id:
			fighters.remove(fighter)
			return fighter
    # ERROR