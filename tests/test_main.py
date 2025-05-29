from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_load_and_search():
    ads_data = """\
Яндекс.Директ:/ru
Крутая реклама:/ru/svrd
Ревдинский рабочий:/ru/svrd/revda
"""

    # Donwload virtual file
    response = client.post('/load', files={'file': ('ads.txt', ads_data, 'text/plain')})
    assert response.status_code == 200

    # Check seacrching
    response = client.get('/search', params={'location': '/ru/svrd/revda'})
    assert response.status_code == 200
    ads = response.json()['ads']
    assert 'Яндекс.Директ' in ads
    assert 'Крутая реклама' in ads
    assert 'Ревдинский рабочий' in ads
