from fastapi.testclient import TestClient

from core.domain.user import User
from infrastructure.api.v1.controller.dependencies.token import get_user_by_token
from main import app


class TestDummyEndpoint:
    def setup_method(self):
        self.client = TestClient(app)
        mock_user = User(
            id=1, username="mock_user", email="mock@example.com", hashed_password="1234"
        )
        app.dependency_overrides[get_user_by_token] = lambda: mock_user

    def test_dummy_endpoint(self):
        response = self.client.get("/api/v1/dummy/dummy")
        assert response.status_code == 200
        assert response.json() == {"response": "scheduller dummy endpoint, current_user=mock_user"}
