from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from src.backend.models.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Will store hashed password
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_type = Column(String(20), nullable=False)  # 'couple_member' or 'parent'
    
    # Relationships with explicit foreign_keys
    couple_responses = relationship("CoupleResponse", back_populates="user")
    parent_responses = relationship("ParentResponse", 
                                   foreign_keys="ParentResponse.user_id",
                                   back_populates="user")
    
    def __repr__(self) -> str:
        return f"<User {self.email}>"

class Couple(Base):
    __tablename__ = 'couples'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    members = relationship("CoupleUser", back_populates="couple")
    
    def __repr__(self) -> str:
        return f"<Couple {self.id}>"

class CoupleUser(Base):
    __tablename__ = 'couple_users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    couple_id = Column(Integer, ForeignKey('couples.id'), nullable=False)
    role = Column(String(20), nullable=False)  # 'partner_1' or 'partner_2'
    
    # Relationships
    user = relationship("User")
    couple = relationship("Couple", back_populates="members")
    
    def __repr__(self) -> str:
        return f"<CoupleUser {self.user_id} in couple {self.couple_id}>"

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)
    question_type = Column(String(20), nullable=False)  # 'couple' or 'parent'
    options = Column(Text, nullable=True)  # JSON string for multiple choice options
    
    def __repr__(self) -> str:
        return f"<Question {self.id}: {self.text[:30]}...>"

class CoupleResponse(Base):
    __tablename__ = 'couple_responses'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="couple_responses")
    question = relationship("Question")
    
    def __repr__(self) -> str:
        return f"<CoupleResponse {self.id} by user {self.user_id}>"

class ParentResponse(Base):
    __tablename__ = 'parent_responses'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    related_to_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # The couple member this parent is related to
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    user = relationship("User", foreign_keys=[user_id], back_populates="parent_responses")
    related_to_user = relationship("User", foreign_keys=[related_to_user_id])
    question = relationship("Question")
    
    def __repr__(self) -> str:
        return f"<ParentResponse {self.id} by user {self.user_id}>"