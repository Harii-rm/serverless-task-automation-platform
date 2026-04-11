from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="admin")

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    stock = Column(Integer, default=0)
    price = Column(Float, default=0.0)

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    last_active = Column(DateTime, default=datetime.datetime.utcnow)
    cart_active = Column(Boolean, default=False)
    cart_last_updated = Column(DateTime, default=datetime.datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AutomationRule(Base):
    __tablename__ = "automation_rules"
    rule_id = Column(Integer, primary_key=True, index=True)
    rule_name = Column(String)
    trigger_type = Column(String) # time, event, threshold, behavior
    condition = Column(String) # JSON or simple string expressions
    action_type = Column(String)
    parameters = Column(String)
    status = Column(Boolean, default=True) # active / inactive
    last_executed = Column(DateTime, nullable=True)

class ExecutionLog(Base):
    __tablename__ = "execution_logs"
    log_id = Column(Integer, primary_key=True, index=True)
    rule_id = Column(Integer, ForeignKey("automation_rules.rule_id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String) # success, error
    message = Column(String)
