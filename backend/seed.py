import database
import models
from datetime import datetime, timedelta

def seed_db():
    database.Base.metadata.create_all(bind=database.engine)
    db = database.SessionLocal()
    
    if db.query(models.User).count() == 0:
        # Create user
        admin = models.User(name="Admin", email="admin@store.com", password="password", role="admin")
        db.add(admin)
        
        # Create products
        p1 = models.Product(name="Wireless Mouse", stock=5, price=29.99)
        p2 = models.Product(name="Mechanical Keyboard", stock=50, price=89.99)
        p3 = models.Product(name="Gaming Monitor", stock=2, price=299.99)
        db.add_all([p1, p2, p3])
        
        # Create customers
        c1 = models.Customer(name="John Doe", email="john@example.com", cart_active=True, cart_last_updated=datetime.utcnow() - timedelta(minutes=45))
        c2 = models.Customer(name="Jane Smith", email="jane@example.com", cart_active=False)
        db.add_all([c1, c2])
        
        # Create a rule
        r1 = models.AutomationRule(
            rule_name="Low Stock Alert",
            trigger_type="threshold",
            condition="stock < 10",
            action_type="notify_admin",
            parameters="{'email': 'admin@store.com'}",
            status=True
        )
        r2 = models.AutomationRule(
            rule_name="Abandoned Cart Reminder",
            trigger_type="behavior",
            condition="cart inactive 30 min",
            action_type="send_email",
            parameters="{'template': 'abandoned_cart'}",
            status=True
        )
        db.add_all([r1, r2])
        
        db.commit()
        print("Database seeded successfully.")
    else:
        print("Database already seeded.")
        
    db.close()

if __name__ == "__main__":
    seed_db()
