from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB
from database import Base


class BoggieForm(Base):
    __tablename__ = "bogie_form"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, index=True, unique=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)

    bmbcChecksheet = Column(JSONB)
    boggieChecksheet = Column(JSONB)
    boggieDetail = Column(JSONB)


class wheel_Form(Base):
    __tablename__ = "wheel_form"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, index=True, unique=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)

    fields = Column(JSONB)
