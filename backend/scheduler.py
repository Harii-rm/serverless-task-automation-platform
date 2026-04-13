from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from database import SessionLocal
import models
import json

def log_execution(db, rule_id, status, message):
    log = models.ExecutionLog(rule_id=rule_id, status=status, message=message)
    db.add(log)
    
    # Update last_executed on the rule
    rule = db.query(models.AutomationRule).filter(models.AutomationRule.rule_id == rule_id).first()
    if rule:
        rule.last_executed = datetime.datetime.now(datetime.timezone.utc)
        
    db.commit()

def evaluate_rules():
    db = SessionLocal()
    try:
        rules = db.query(models.AutomationRule).filter(models.AutomationRule.status == True).all()
        for rule in rules:
            try:
                # Basic parsing simulation
                # In a real engine, we'd use a safe evaluator or regex to parse "condition"
                
                # Rule 1 Example: Low stock alert
                # Condition: "stock < 10" or similar
                if "stock" in rule.condition.lower() and rule.trigger_type == "threshold":
                    # Check products
                    try:
                        threshold = int(''.join(filter(str.isdigit, rule.condition)))
                    except:
                        threshold = 10
                        
                    low_stock_products = db.query(models.Product).filter(models.Product.stock < threshold).all()
                    if low_stock_products:
                        msg = f"Alert! {len(low_stock_products)} products have low stock."
                        log_execution(db, rule.rule_id, "success", msg)
                        continue
                
                # Rule 2: Abandoned cart
                if rule.trigger_type == "behavior" and "cart" in rule.condition.lower():
                    inactive_customers = db.query(models.Customer).filter(
                        models.Customer.cart_active == True
                    ).all()
                    # In real app verify time against cart_last_updated
                    if inactive_customers:
                        msg = f"Sent reminders to {len(inactive_customers)} users."
                        log_execution(db, rule.rule_id, "success", msg)
                        continue
                        
                # Rule 3: Time based
                if rule.trigger_type == "time":
                    msg = "Executed time-based rule action: " + rule.action_type
                    log_execution(db, rule.rule_id, "success", msg)
                    continue

                # Dummy fallback
                if rule.trigger_type == "event":
                    msg = "Evaluated event loop conditions but no matches."
                    # Optional: avoid flooding logs with "no matches", 
                    # but for demonstration we'll log it occasionally or skip
                    pass
                    
            except Exception as e:
                log_execution(db, rule.rule_id, "error", str(e))
                
    finally:
        db.close()

scheduler = BackgroundScheduler()

def start_scheduler():
    # Evaluate rules every 30 seconds for demonstration purposes
    scheduler.add_job(evaluate_rules, 'interval', seconds=30)
    scheduler.start()

if __name__ == "__main__":
    import time
    print("Starting background scheduler...")
    start_scheduler()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        pass
