from enum import Enum

class DifficultyLevel(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class ReportReason(str, Enum):
    INCORRECT_CONTENT = "incorrect_content"
    INAPPROPRIATE = "inappropriate"
    OFFENSIVE = "offensive"
    COPYRIGHT = "copyright"
    OTHER = "other"
