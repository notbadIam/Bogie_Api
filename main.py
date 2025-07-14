from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from schemas import *
from database import SessionLocal, Base, engine

# Base.metadata.create_all(bind=engine)
from fastapi.encoders import jsonable_encoder


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()


@app.get("/")               #Complete
def greet():
    return {"message": "Welcome to Bogie Form api"}


@app.post("/api/forms/bogie-checklist")
def submit_form(form: BogieFormCreate, db: Session = Depends(get_db)):
    try:
        db_form = models.BoggieForm(
            formNumber = form.formNumber,
            inspectionBy = form.inspectionBy,
            inspectionDate = form.inspectionDate,
            bmbcChecksheet = jsonable_encoder(form.bmbcChecksheet),
            boggieChecksheet = jsonable_encoder(form.bogieChecksheet),
            boggieDetail = jsonable_encoder(form.bogieDetails),
        )
        db.add(db_form)
        db.commit()
        db.refresh(db_form)
        return {
            "data": {
                "formNumber" : db_form.formNumber,
                "inspectionBy" : db_form.inspectionBy,
                "inspectionDate" : db_form.inspectionDate,
                "status": "Saved"
            },
            "message": "Boggie checklist submitted",
            "success": True
        }
    except Exception as e:
        print(e)
        return {
            "message": "Form submission failed",
            "success": False
        }
    finally:
        db.close()


@app.post("/api/forms/wheel-specifications")
def add_specification(form: WheelFormCreate, db: Session = Depends(get_db)):
    try:
        db_form = models.wheel_Form(
            formNumber = form.formNumber,
            submittedBy = form.submittedBy,
            submittedDate = form.submittedDate,
            fields = form.fields.model_dump()
        )
        db.add(db_form)
        db.commit()
        db.refresh(db_form)
        return {
            "data": {
                "formNumber" : db_form.formNumber,
                "status": "Saved",
                "submittedBy" : db_form.submittedBy,
                "submittedDate" : db_form.submittedDate,
            },
            "message": "Wheel specifications submitted successfully",
            "success": True
        }
    except:
        return {
            "message": "Wheel specifications submission failed",
            "success": False
        }
