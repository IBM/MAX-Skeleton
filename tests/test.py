import pytest
import requests


def test_swagger():

    model_endpoint = 'http://localhost:5000/swagger.json'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200
    assert r.headers['Content-Type'] == 'application/json'

    json = r.json()
    assert 'swagger' in json
    assert json.get('info') and json.get('info').get('title') == 'Model Asset Exchange Server'


def test_metadata():

    model_endpoint = 'http://localhost:5000/model/metadata'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200

    metadata = r.json()
    assert metadata['id'] == 'ADD IN MODEL ID'
    assert metadata['name'] == 'ADD MODEL NAME'
    assert metadata['description'] == 'ADD MODEL DESCRIPTION'
    assert metadata['license'] == 'ADD MODEL LICENSE'


def test_response():
    model_endpoint = 'http://localhost:5000/model/predict'
    file_path = 'assets/SAMPLE_FILE.jpg'

    with open(file_path, 'rb') as file:
        file_form = {'image': (file_path, file, 'image/jpeg')}

    r = requests.post(url=model_endpoint, files=file_form)

    assert r.status_code == 200
    response = r.json()

    assert response['status'] == 'ok'

    # add sanity checks here


if __name__ == '__main__':
    pytest.main([__file__])
