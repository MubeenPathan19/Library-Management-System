from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import MemberCreate
from app.models import Member
from app.database import get_db

router = APIRouter()

@router.post("/add-member")
def add_member(member: MemberCreate, db: Session = Depends(get_db)):
    new_member = Member(user_id=member.user_id)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member
