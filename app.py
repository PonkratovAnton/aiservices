import os

import httpx
import uvicorn
from fastapi import FastAPI, HTTPException, Depends

from initialize import initialize
from models import RequestModel, ResponseModel
from openai_client import get_openai_response
from token_service import verify_token

app = FastAPI()
ai_token = os.getenv('AI_TOKEN')


@app.post("/chat/", response_model=ResponseModel, dependencies=[Depends(verify_token)])
async def chat(request: RequestModel):
    try:
        answer = get_openai_response(ai_token, request.user_input)
        return ResponseModel(response=answer)
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @app.get("/token/{service_name}", response_model=TokenResponseModel)
# async def get_token(service_name: str):
#     token = get_token_by_service_name(service_name)
#     if token is None:
#         raise HTTPException(status_code=404, detail="Service not found")
#     return TokenResponseModel(token=token)


if __name__ == "__main__":
    print("я тут")
    initialize()

    uvicorn.run(app, host="0.0.0.0", port=8000)
