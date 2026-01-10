from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

class QuizRating(Base, BaseModel):
    __tablename__ = "quiz_ratings"

    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=True)

    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    user = relationship("User", back_populates="quiz_ratings")
    quiz = relationship("Quiz", back_populates="ratings")

    # Ensure one rating per user per quiz
    __table_args__ = (UniqueConstraint('user_id', 'quiz_id', name='_user_quiz_uc'),)
