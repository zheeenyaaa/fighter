from fastapi import APIRouter, HTTPException, status
from models import FighterInput
from models import FighterModel

fighter1 = FighterModel(id = 1, speed = 100)
fighter2 = FighterModel(id = 2, speed = 200)

fighters_list = [fighter1, fighter2]

router = APIRouter(prefix = "/fighters", tags=["fighters"])

@router.get("/")
def get_fighters() -> list[FighterModel]:
  return fighters_list

@router.get("/{fighter_id}")
def get_fighter(fighter_id: int) -> FighterModel:
    for fighter in fighters_list:
        if fighter.id == fighter_id:
            return fighter
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Истребителдь не найден")

@router.post("//")
def create_fighter(fighter: FighterInput) -> FighterModel:
	new_fighter_id = len(fighters_list) + 1
	new_fighter = FighterModel(id = new_fighter_id, speed = fighter.speed)
	fighters_list.append(new_fighter)
	print(fighters_list)
	return new_fighter


# @app.put()

@router.delete("/{fighter_id}")
def delete_fighter(fighter_id: int) -> FighterModel:
	for fighter in fighters_list:
		if fighter.id == fighter_id:
			fighters_list.remove(fighter)
			return fighter
    # ERROR
    


