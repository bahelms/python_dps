from dps.models import Base, Model
from datetime import datetime
from sqlalchemy import Column, String, Integer, Sequence, PrimaryKeyConstraint

class Specatt(Base, Model):
    __tablename__ = "specatt"
    __table_args__ = (
        PrimaryKeyConstraint("saspec", "sadiv", name="specatt_pk"),
        {"schema": "source"}
        )

    id = Column(
        Integer,
        Sequence("specatt_id_seq"),
        server_default=Sequence("specatt_id_seq").next_value(),
        nullable=False,
        index=True)

    sadlcd = Column(String)
    saspec = Column(String)
    sadiv = Column(String)
    sadesc = Column(String)

    def transform_public(self) -> dict:
        """Transforms the data of this object into its public version dict"""
        return {
            "code": self.saspec,
            "division": self.sadiv,
            "description": self.sadesc,
            }
