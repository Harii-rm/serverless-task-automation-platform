from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas

router = APIRouter()
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

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
