from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas

router = APIRouter()

@router.get("/rules", response_model=List[schemas.AutomationRuleOut])
def get_rules(db: Session = Depends(database.get_db)):
    rules = db.query(models.AutomationRule).all()
    return rules

@router.post("/rules", response_model=schemas.AutomationRuleOut, status_code=status.HTTP_201_CREATED)
def create_rule(rule: schemas.AutomationRuleCreate, db: Session = Depends(database.get_db)):
    new_rule = models.AutomationRule(**rule.dict())
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)
    return new_rule

@router.put("/rules/{rule_id}", response_model=schemas.AutomationRuleOut)
def update_rule(rule_id: int, rule_update: schemas.AutomationRuleUpdate, db: Session = Depends(database.get_db)):
    rule_query = db.query(models.AutomationRule).filter(models.AutomationRule.rule_id == rule_id)
    rule = rule_query.first()
    
    if not rule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rule not found")
        
    update_data = rule_update.dict(exclude_unset=True)
    rule_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(rule)
    return rule

@router.delete("/rules/{rule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rule(rule_id: int, db: Session = Depends(database.get_db)):
    rule = db.query(models.AutomationRule).filter(models.AutomationRule.rule_id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rule not found")
        
    db.delete(rule)
    db.commit()
    return

@router.get("/logs", response_model=List[schemas.ExecutionLogOut])
def get_logs(db: Session = Depends(database.get_db)):
    logs = db.query(models.ExecutionLog).order_by(models.ExecutionLog.timestamp.desc()).all()
    return logs

@router.get("/dashboard-stats", response_model=schemas.DashboardStats)
def get_dashboard_stats(db: Session = Depends(database.get_db)):
    total_rules = db.query(models.AutomationRule).count()
    active_rules = db.query(models.AutomationRule).filter(models.AutomationRule.status == True).count()
    recent_executions = db.query(models.ExecutionLog).count() # simplistic, maybe limit to recent
    
    # For simplicity, alerts count could be low stock products
    alerts = db.query(models.Product).filter(models.Product.stock < 10).count()
    
    return {
        "total_rules": total_rules,
        "active_rules": active_rules,
        "recent_executions": recent_executions,
        "alerts": alerts
    }
