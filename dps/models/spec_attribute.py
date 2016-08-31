from sqlalchemy import Column, String, Integer, DateTime
from dps.models import Base

class SpecAttribute(Base):
    __tablename__ = "spec_attributes"

    id = Column(Integer, primary_key=True)
    division = Column(String)
    code = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
