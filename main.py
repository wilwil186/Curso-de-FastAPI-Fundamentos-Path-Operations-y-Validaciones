from fastapi import FastAPI # impotar FastAPI

app = FastAPI() #instancia

@app.get("/") #path operations
def home():
    return {"Hello": "World"}