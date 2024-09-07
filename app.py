from fastapi import FastAPI
import uvicorn
import os
import json

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from src.finetunningDistilBertner.pipeline.prediction import PredictonPipeline


app = FastAPI()

@app.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')


@app.get('/train')
async def train():
    try:
        os.system('python main.py')
    except Exception as e:
        return Response(f'error :: {e}')

@app.get('/predict')
async def predict(text):

    try:
        obj = PredictonPipeline()
        output = obj.predict(text)
        return output
    except Exception as e:
        return Response(f'error :: {e}')
    


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8006)