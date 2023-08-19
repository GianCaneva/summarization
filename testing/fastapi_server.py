from fastapi import FastAPI

app = FastAPI()

@app.post('/api/receive/fast')
async def receive_text(text: str):
    print("Texto recibido:", text)
    return {"message": "Texto recibido exitosamente."}
