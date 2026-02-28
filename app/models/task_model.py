from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    priority: int # Del 1 al 5, por ejemplo