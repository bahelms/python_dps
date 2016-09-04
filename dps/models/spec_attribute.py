from dps.models import Base, Model
from sqlalchemy import Column, String, Integer, Sequence, PrimaryKeyConstraint

class SpecAttribute(Base, Model):
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
