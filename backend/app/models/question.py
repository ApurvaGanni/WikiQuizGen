from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

class Question(Base, BaseModel):
    __tablename__ = "questions"

    question_text = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # Stored as JSON array
    correct_answer = Column(String(255), nullable=False)
    explanation = Column(Text, nullable=True)
    difficulty = Column(String(50), nullable=True)
    question_type = Column(String(50), default="multiple_choice")
    order = Column(Integer, default=0)
    points = Column(Integer, default=1)
    tags = Column(JSON, nullable=True)  # For categorizing questions

    # Relationships
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    quiz = relationship("Quiz", back_populates="questions")
