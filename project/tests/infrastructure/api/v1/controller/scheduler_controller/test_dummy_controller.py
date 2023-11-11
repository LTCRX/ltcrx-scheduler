from fastapi.testclient import TestClient

from infrastructure.api.v1.controller.scheduler_controller.dummy_controller import router


class TestDummyEndpoint:
    def setup_method(self):
        self.client = TestClient(router)

    def test_dummy_endpoint(self):
        response = self.client.get("/dummy")
        assert response.status_code == 200
        assert response.json() == {"response": "scheduller dummy endpoint"}
