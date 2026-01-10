from .database import Base, engine, get_db
from . import models

# Import all models to ensure they are registered with SQLAlchemy
from .models import User, Quiz, Question, QuizRating, QuizReport

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
