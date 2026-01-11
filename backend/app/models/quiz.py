from sqlalchemy import Column, String, Text, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

class Quiz(Base, BaseModel):
    __tablename__ = "quizzes"

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    source_url = Column(String(512), nullable=False)
    difficulty = Column(String(20), default="medium")  # Will be updated to use Enum later
    is_public = Column(Boolean, default=True)
    thumbnail_url = Column(String(512), nullable=True)
    estimated_duration = Column(Integer, comment="Estimated duration in minutes")
    views_count = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)
    report_count = Column(Integer, default=0)

    # Relationships
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan")
    ratings = relationship("QuizRating", back_populates="quiz", cascade="all, delete-orphan")
    reports = relationship("QuizReport", back_populates="quiz", cascade="all, delete-orphan")
