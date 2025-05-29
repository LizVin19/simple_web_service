from ad_service import AdService

def create_sample_service():
    ads = [
        "Яндекс.Директ:/ru",
        "Крутая реклама:/ru/svrd",
        "Ревдинский рабочий:/ru/svrd/revda"
    ]
    service = AdService()
    for line in ads:
        name, locs = line.strip().split(':', 1)
        for loc in locs.split(','):
            service.data[loc.strip()].append(name)
    return service

def text_exact_match():
    service = create_sample_service()
    result = service.get_ads('/ru/svrd/revda')
    assert sorted(result) == sorted(["Ревдинский рабочий", "Крутая реклама", "Яндекс.Директ"])

def test_prefix_match():
    service = create_sample_service()
    result = service.get_ads('/ru/svrd')
    assert sorted(result) == sorted(["Крутая реклама", "Яндекс.Директ"])

def test_no_match():
    service = create_sample_service()
    result = service.get_ads('/unknown/path')
    assert result == []

