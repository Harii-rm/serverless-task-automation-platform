import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_valid():
    r = client.post(
        "/api/auth/login",
        json={"email": "admin@store.com", "password": "password"}
    )
    assert r.status_code == 200


def test_create_rule():
    rule = {
        "rule_name": "Test Rule",
        "trigger_type": "time",
        "condition": "daily",
        "action_type": "notify",
        "parameters": "none",
        "status": True
    }

    r = client.post("/api/rules", json=rule)
    assert r.status_code == 201