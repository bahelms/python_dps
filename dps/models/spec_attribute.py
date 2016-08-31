from sqlalchemy import Column, String, Integer
from dps.models import Base

class SpecAttribute(Base):
    __tablename__ = "spec_attributes"

    id = Column(Integer, primary_key=True)
    division = Column(String)
    code = Column(String)
    description = Column(String)
