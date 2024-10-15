from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DetectionResultBase(BaseModel):
    image_name: str
    confidence_score: float
    class_name: str
    bbox_coordinates: List[float] 
    result_image_path: str
    detection_time: datetime

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True
