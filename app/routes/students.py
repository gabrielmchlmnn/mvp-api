from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado!"
        )

    return student


@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    existing_email = (
        db.query(Student)
        .filter(Student.email == student_data.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado!"
        )

    student = Student(
        name=student_data.name,
        email=student_data.email,
        phone=student_data.phone,
        zip_code=student_data.zip_code
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado!"
        )

    existing_email = (
        db.query(Student)
        .filter(
   Student.email == student_data.email,
            Student.id != student_id
        )
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado, utilize outro email!"
        )

    student.name = student_data.name
    student.email = student_data.email
    student.phone = student_data.phone
    student.zip_code = student_data.zip_code

    db.commit()
    db.refresh(student)

    return student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado!"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Aluno excluído com sucesso!"
    }