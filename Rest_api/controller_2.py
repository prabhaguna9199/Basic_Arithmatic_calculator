from fastapi import FastAPI, HTTPException
from Rest_api.Arithmatic_operations import Arithmatic_operators
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Numbers(BaseModel):
    a: float
    b: float


@app.post("/numbers/add")
def addition(request: Numbers):
    return {"result": Arithmatic_operators(a=request.a, b=request.b).add()}


@app.post("/numbers/sub")
def subraction(request: Numbers):
    return {"result": Arithmatic_operators(a=request.a, b=request.b).sub()}


@app.post("/numbers/multiplication")
def multiplication(request: Numbers):
    return {"result": Arithmatic_operators(a=request.a, b=request.b).multiple()}


@app.post("/numbers/division")
def division(request: Numbers):
    try:
        return {"result": Arithmatic_operators(a=request.a, b=request.b).divide()}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="cannot divide by zero")




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)