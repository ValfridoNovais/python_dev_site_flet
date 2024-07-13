import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Diretório onde os arquivos serão armazenados
UPLOAD_DIR = "uploads"

# Cria o diretório de uploads se não existir
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app = FastAPI()

# Serve arquivos estáticos da pasta de uploads
app.mount(f"/{UPLOAD_DIR}", StaticFiles(directory=UPLOAD_DIR), name="uploads")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
