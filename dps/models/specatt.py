from sqlalchemy import Column, String, Integer, DateTime, PrimaryKeyConstraint, Sequence
from dps.models import Base

class Specatt(Base):
    __tablename__ = "specatt"
    __table_args__ = (
        PrimaryKeyConstraint('sacode', 'sadiv', name="specatt_pk"),
        {"schema": "source"}
        )

    id = Column(
        Integer,
        Sequence("specatt_id_seq"),
        server_default=Sequence("specatt_id_seq").next_value(),
        nullable=False,
        index=True
        )

    sadlcd     = Column(String)
    sacode     = Column(String)
    sadiv      = Column(String)
    sadesc     = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
