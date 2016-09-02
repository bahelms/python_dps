from dps.models import Base
from sqlalchemy import (Column, String, Integer, DateTime, Sequence,
                        PrimaryKeyConstraint)

class SpecAttribute(Base):
    __tablename__ = "spec_attributes"
    __table_args__ = (
        PrimaryKeyConstraint("code", "division", name="spec_attributes_pk"),
        {}
        )

    id = Column(
        Integer,
        Sequence("spec_attributes_id_seq"),
        server_default=Sequence("spec_attributes_id_seq").next_value(),
        nullable=False,
        index=True)

    division = Column(String)
    code = Column(String)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
