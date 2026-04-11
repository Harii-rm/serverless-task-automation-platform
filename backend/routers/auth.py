from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database, models, schemas

router = APIRouter()

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    # Mock login logic since auth was kept simple
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    if not user or user.password != user_credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    return {"access_token": user.email, "token_type": "bearer"}
