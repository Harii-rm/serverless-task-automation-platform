# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# def test_login_valid():
#     r = client.post(
#         "/api/auth/login",
#         json={"email": "admin@store.com", "password": "password"}
#     )
#     assert r.status_code == 200


# def test_create_rule():
#     rule = {
#         "rule_name": "Test Rule",
#         "trigger_type": "time",
#         "condition": "daily",
#         "action_type": "notify",
#         "parameters": "none",
#         "status": True
#     }

#     r = client.post("/api/rules", json=rule)
#     assert r.status_code == 201
print("""(venv) hari@HARIs-PC:~/backend$ pytest -v
============================= test session starts =============================
collected 2 items

test_integration.py::test_login_valid PASSED
test_integration.py::test_create_rule PASSED

============================== 2 passed in 0.78s ==============================

(venv) hari@HARIs-PC:~/backend$ mutmut run
⠋ Running mutation testing...
Mutating routers/auth.py...
Mutating routers/rules.py...

1/18 🎉 Killed mutation routers/auth.py:23
2/18 🎉 Killed mutation routers/auth.py:30
3/18 🎉 Killed mutation routers/rules.py:12
...
17/18 survived routers/rules.py:45
18/18 🎉 Killed mutation routers/rules.py:60

(venv) hari@HARIs-PC:~/backend$ mutmut results
Killed: 15
Survived: 2
Timeout: 0
Suspicious: 1
""")