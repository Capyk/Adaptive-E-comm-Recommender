from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func  # Used for default timestamp

# Base class for all model definitions
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    join_date = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to interactions (defines the 'user.interactions' property)
    interactions = relationship("Interaction", back_populates="user")


class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=False)
    price = Column(Numeric, nullable=False)

    # Relationship to interactions
    interactions = relationship("Interaction", back_populates="item")


class Interaction(Base):
    __tablename__ = 'interactions'

    # Primary Key
    interaction_id = Column(Integer, primary_key=True, autoincrement=True)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)

    # Interaction Data
    rating = Column(Numeric(precision=3, scale=2), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships (defines the 'interaction.user' and 'interaction.item' properties)
    user = relationship("User", back_populates="interactions")
    item = relationship("Item", back_populates="interactions")