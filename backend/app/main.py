from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Content Engine Backend is running"}