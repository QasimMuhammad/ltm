from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment or use default
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///ltm.db')

# Create engine
engine = create_engine(DATABASE_URL)

# Create session factory
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Base class for models
Base = declarative_base()


def init_db() -> None:
    """Initialize the database by creating all tables."""
    # Import models here to avoid circular imports
    from src.backend.models.models import (  # noqa: F401
        User, Couple, CoupleUser, Question, CoupleResponse, ParentResponse
    )
    Base.metadata.create_all(engine)
    
    # Add initial questions if the questions table is empty
    session = Session()
    try:
        if session.query(Question).count() == 0:
            add_initial_questions(session)
    finally:
        session.close()


def add_initial_questions(session) -> None:  # type: ignore
    """Add initial questions to the database."""
    from src.backend.models.models import Question
    
    # Couple questions organized by sections
    couple_questions = [
        # Section: Understanding Self and Marriage
        Question(
            text="Why should we marry?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="Why are you getting married to this particular man/woman?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What in your view is to be a \"woman\"?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What in your view is to be a \"man\"?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is the role of a husband in married life?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is the role of a wife in married life?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What are your expectations from your wife or husband?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is an ideal husband for you?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is an ideal wife for you?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What makes you happy?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is a happy married life for you?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is relaxing for you?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is respect for you? How will you show respect to your husband/wife?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        Question(
            text="What will make you feel that you are respected by your wife/husband?",
            category="Understanding Self and Marriage",
            question_type="couple",
            options=None
        ),
        
        # Section: Families and In-laws
        Question(
            text="How will you feel that you get respect from in-laws and how will you show respect to your in-laws?",
            category="Families and In-laws",
            question_type="couple",
            options=None
        ),
        Question(
            text="What should be the role of your in-laws in your married life?",
            category="Families and In-laws",
            question_type="couple",
            options=None
        ),
        Question(
            text="Do you want to live with your parents-in-law after marriage? If yes, why? If not, why?",
            category="Families and In-laws",
            question_type="couple",
            options=None
        ),
        Question(
            text="Do you have any fears about living with your parents-in-law?",
            category="Families and In-laws",
            question_type="couple",
            options=None
        ),
        Question(
            text="Do you want your spouse to work after marriage or be a housewife, and why?",
            category="Families and In-laws",
            question_type="couple",
            options=None
        ),
        
        # Section: Cultural and Emotional Expectations
        Question(
            text="What is culture for you?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        Question(
            text="How do you express that you are offended or angry?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        Question(
            text="How do you behave to show that something is serious or very important for you?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is being religious in your opinion?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is being a practicing Muslim in your opinion?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        Question(
            text="What if you are not able to get a baby after marriage?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        Question(
            text="How will you handle if your spouse does not agree with you on a specific issue?",
            category="Cultural and Emotional Expectations",
            question_type="couple",
            options=None
        ),
        
        # Section: Conflict and Boundaries
        Question(
            text="What is the best way to resolve a conflict with your husband or with your mother-in-law?",
            category="Conflict and Boundaries",
            question_type="couple",
            options=None
        ),
        Question(
            text="In your view, whose role is to adjust: the bride or the in-laws?",
            category="Conflict and Boundaries",
            question_type="couple",
            options=None
        ),
        Question(
            text="You are happy that your son is getting married. Are you ready to share him with another person? How will you share your son with your daughter-in-law?",
            category="Conflict and Boundaries",
            question_type="parent",  # This seems more like a parent question
            options=None
        ),
        Question(
            text="Do you know your boundaries as a wife, husband, father-in-law, or mother-in-law?",
            category="Conflict and Boundaries",
            question_type="couple",
            options=None
        ),
        Question(
            text="What are your boundaries that in-laws should not cross, and what are the boundaries you will not cross toward in-laws?",
            category="Conflict and Boundaries",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is a red line for you — that your in-laws, including your husband or wife, should not cross?",
            category="Conflict and Boundaries",
            question_type="couple",
            options=None
        ),
        
        # Section: Duties and Opinions
        Question(
            text="Is it a wife's duty to serve the parents-in-law?",
            category="Duties and Opinions",
            question_type="couple",
            options=None
        ),
        Question(
            text="If there is a need, how will the wife contribute in taking care of the parents-in-law?",
            category="Duties and Opinions",
            question_type="couple",
            options=None
        ),
        Question(
            text="What is your opinion about dowry/Jahez?",
            category="Duties and Opinions",
            question_type="couple",
            options=None
        ),
        
        # Section: Final Thoughts
        Question(
            text="What are the major causes of married couple problems in Pakistan?",
            category="Final Thoughts",
            question_type="couple",
            options=None
        ),
        Question(
            text="Please add a comment if you found this form useful.",
            category="Final Thoughts",
            question_type="couple",
            options=None
        ),
        Question(
            text="Please add a suggestion for what you would have liked to have in the form.",
            category="Final Thoughts",
            question_type="couple",
            options=None
        ),
    ]
    
    # Parent questions
    parent_questions = [
        # Add parent-specific questions here
        Question(
            text="You are happy that your son/daughter is getting married. Are you ready to share them with another person?",
            category="Boundaries",
            question_type="parent",
            options=None
        ),
        Question(
            text="What role do you expect to play in your child's married life?",
            category="Expectations",
            question_type="parent",
            options=None
        ),
        Question(
            text="What are your expectations from your child's spouse?",
            category="Expectations",
            question_type="parent",
            options=None
        ),
        Question(
            text="What family traditions do you hope your child will continue in their marriage?",
            category="Family Culture",
            question_type="parent",
            options=None
        ),
        Question(
            text="How do you feel about your child's choice of partner?",
            category="Relationship",
            question_type="parent",
            options=None
        ),
    ]
    
    # Add all questions to the session
    for question in couple_questions + parent_questions:
        session.add(question)
    
    # Commit the changes
    session.commit()