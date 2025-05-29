from fastapi import FastAPI, UploadFile, HTTPException
from ad_service import AdService

app = FastAPI()
service = AdService()


@app.post('/load')
async def load(file: UploadFile):
    if not file:
        raise HTTPException(status_code=400, detail='No file provided')
    lines = (await file.read()).decode('utf-8').splitlines()
    service.load_from_lines(lines)

    return {'status': 'ok'}

@app.get('/search')
def search(location: str, mode: str = 'up'):
    if not location:
        raise HTTPException(status_code=400, detail='Location required')
    return {'ads': service.get_ads(location, mode=mode)}
