import pytest
from fastapi.testclient import TestClient
from fastapi import status
from HTTP_REST_service import schemas
from HTTP_REST_service.main import app


client = TestClient(app)


@pytest.fixture
def mock_db_session(mocker):
    session = mocker.Mock()
    session.commit.return_value = None
    session.flush.return_value = None
    session.refresh.return_value = None
    session.add.return_value = None
    return session


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World!"}


def test_get_all_aquapods():

    response = client.get("/aquapods")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)

    for aquapod in data:
        # assert each element in the list is an Aquapod
        assert 'id' in aquapod
        assert 'name' in aquapod

        # check the type of each property
        assert isinstance(aquapod['id'], int)
        assert isinstance(aquapod['name'], str)


def test_get_aquapod_by_name():

    response = client.get("/aquapods/Pula")

    assert response.status_code == status.HTTP_200_OK

    aquapod = response.json()

    assert 'id' in aquapod
    assert 'name' in aquapod
    assert 'latest_data' in aquapod

    assert isinstance(aquapod['id'], int)
    assert isinstance(aquapod['name'], str)
    assert isinstance(aquapod['latest_data'], list)

    for component_data in aquapod['latest_data']:
        # assert each element in the latest_data list is a dict with "component" and "data" keys
        assert 'component' in component_data
        assert 'data' in component_data

        # assert the type of the "component" and "data" values
        assert isinstance(component_data['component'], str)


test_aquapod = "Porec"


def test_create_aquapod(mock_db_session, mocker):
    mocker.patch('HTTP_REST_service.main.get_db',
                 return_value=mock_db_session)
    payload = schemas.AquaPodCreate(
        name=test_aquapod,
    )

    response = client.post("/aquapods/", json=payload.dict())
    assert response.status_code == 201
