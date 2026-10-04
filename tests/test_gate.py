from fastapi.testclient import TestClient
from policy.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'image': 'api:1.0.0', 'privileged': False}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'image': 'api:1.0.0', 'privileged': True}).json()
    assert bad["passed"] is False
    assert "privileged" in bad["failed"]
