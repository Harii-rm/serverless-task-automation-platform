from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- Auth Schemas ---
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# --- Automation Rule Schemas ---
class AutomationRuleBase(BaseModel):
    rule_name: str
    trigger_type: str
    condition: str
    action_type: str
    parameters: str
    status: bool = True

class AutomationRuleCreate(AutomationRuleBase):
    pass

class AutomationRuleUpdate(BaseModel):
    rule_name: Optional[str] = None
    trigger_type: Optional[str] = None
    condition: Optional[str] = None
    action_type: Optional[str] = None
    parameters: Optional[str] = None
    status: Optional[bool] = None

class AutomationRuleOut(AutomationRuleBase):
    rule_id: int
    last_executed: Optional[datetime] = None

    class Config:
        from_attributes = True

# --- Log Schemas ---
class ExecutionLogOut(BaseModel):
    log_id: int
    rule_id: int
    timestamp: datetime
    status: str
    message: str

    class Config:
        from_attributes = True

# --- Dashboard & Report Schemas ---
class DashboardStats(BaseModel):
    total_rules: int
    active_rules: int
    recent_executions: int
    alerts: int
