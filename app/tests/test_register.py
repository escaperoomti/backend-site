import dns.resolver
from app.main import app
from app.src.schemas.email import EmailSchema
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

client = TestClient(app)


class TestRegister:

    email = EmailSchema(email="enlabe@gmail.com")

    def test_register_email_recruiter_with_mx_record(self, mocker: MockerFixture) -> None:
        mock_resolve = mocker.patch("dns.resolver.resolve")
        mock_resolve.return_value = [mocker.Mock()]
        json = jsonable_encoder(self.email)
        response = client.post("/api/v1/recruiter/register/email", json=json)
        assert response.status_code == 200
        assert response.json() == {"data": "enlabe@gmail.com"}

    def test_register_email_recruiter_without_mx_record(self, mocker: MockerFixture) -> None:
        mocker.patch("dns.resolver.resolve", side_effect=dns.resolver.NoAnswer)
        email = "enlabe@nonexistentdomain.com"
        json = {"email": email}
        response = client.post("/api/v1/recruiter/register/email", json=json)
        assert response.status_code == 422
        assert "Domain does not have a MX record" in str(response.content)
