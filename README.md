# AdService — Search Ads by Nested Locations (FastAPI)

This is a simple FastAPI web service that:

- Loads a list of advertising platforms from a text file (`ads.txt`)
- Allows searching for all relevant platforms for a given location

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the server:

```bash
uvicorn main:app --reload
```

3. Open Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Sample Requests

### Upload ads.txt

```http
POST /load
```

Send a file with format: `Platform Name:/location1,/location2,...`

Example contents:

```
Yandex.Direct:/ru
Cool Ads:/ru/svrd
Revda Media:/ru/svrd/revda
```

### Search

```http
GET /search?location=/ru/svrd/revda
```

Response:

```json
{
  "ads": [
    "Yandex.Direct",
    "Cool Ads",
    "Revda Media"
  ]
}
```

## Tests

```bash
pytest
```

## Project Structure

```
main.py             # FastAPI endpoints
ad_service.py       # Business logic
tests/              # Unit and integration tests
ads.txt             # Sample input
```
