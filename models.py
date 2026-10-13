from pydantic import BaseModel

# class FighterModel(BaseModel):
#    id: int
#    name: str
#    max_speed: int
#    country: str
#    length: int
#    wingspan: int

class FighterModel(BaseModel):
   id: int
   speed: int

class FighterInput(BaseModel):
   speed: int

class FighterUpdate(BaseModel):
   speed: int