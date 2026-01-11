from sqlalchemy import Column, Integer, ForeignKey, Text, String
from sqlalchemy.orm import relationship
from .base import Base, BaseModel

class QuizReport(Base, BaseModel):
    __tablename__ = "quiz_reports"

    reason = Column(String(50), nullable=False)  # Will be updated to use Enum later
    details = Column(Text, nullable=True)
    status = Column(String(50), default="pending")  # pending, reviewed, resolved, rejected

    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    user = relationship("User", back_populates="quiz_reports")
    quiz = relationship("Quiz", back_populates="reports")
