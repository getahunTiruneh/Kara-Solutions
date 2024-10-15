import sys
sys.path.append('../')
from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class DetectionResult(Base):
    __tablename__ = 'detection_results'

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    confidence_score = Column(Float)
    class_name = Column(String)
    bbox_coordinates = Column(String)  # Store as a string
    result_image_path = Column(String)
    detection_time = Column(DateTime)
