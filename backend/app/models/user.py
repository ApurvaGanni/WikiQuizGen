from sqlalchemy import Column, String, Boolean, Text
from .base import Base, BaseModel

class User(Base, BaseModel):
    __tablename__ = "users"

    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    profile_picture = Column(Text, nullable=True)
    bio = Column(Text, nullable=True)

    # Relationships will be added after creating related models
    quizzes = None
    quiz_ratings = None
    quiz_reports = None

    # Relationships
    quizzes = relationship("Quiz", back_populates="owner")
    quiz_ratings = relationship("QuizRating", back_populates="user")
    quiz_reports = relationship("QuizReport", back_populates="user")
