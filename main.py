from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
from fastapi.exceptions import RequestValidationError
from app.notes.router import router as router_notes
from typing import Optional

app = FastAPI()


class RBNote:
    def __init__(self, amount: Optional[int]):
        self.amount = amount


app.include_router(router_notes)


@app.exception_handler(RequestValidationError)
async def cust(request: RequestValidationError, exc: RequestValidationError):
    if request.url.path == "/notes/":
        return HTMLResponse(
            status_code=502,
            content=json.dumps({"detail": exc.errors(), "body": exc.body}),
        )
    else:
        return HTMLResponse(
            status_code=422,
            content=json.dumps({"detail": exc.errors(), "body": exc.body}),
        )
