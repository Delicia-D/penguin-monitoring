from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Penguin(Base):
    __tablename__ = 'penguins'
    id = Column(Integer, primary_key=True, index=True)
    rfid = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="normal")  #
    visits = relationship("Visit", back_populates="penguin")


class Visit(Base):
    __tablename__ = 'visits'
    id = Column(Integer, primary_key=True, index=True)
    penguin_id = Column(Integer, ForeignKey('penguins.id'), nullable=False)
    weight = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    image_path = Column(String(255))

    penguin = relationship("Penguin", back_populates="visits")
