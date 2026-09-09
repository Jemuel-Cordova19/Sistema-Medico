import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Cargar variables de entorno si existen (.env)
load_dotenv()

app = FastAPI(title="Sistema Médico API")

# Configurar CORS para permitir que el frontend se comunique con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estructura esperada de los datos del formulario de login
class LoginRequest(BaseModel):
    correo: str
    password: str

@app.get("/")
def home():
    return {"status": "online", "mensaje": "Servidor Médico Backend Funcionando"}

@app.post("/api/login")
def login(datos: LoginRequest):
    # Verificación de credenciales de prueba
    if datos.correo == "admin@test.com" and datos.password == "123456":
        return {
            "status": "success", 
            "message": "Inicio de sesión exitoso",
            "usuario": {"correo": datos.correo, "rol": "administrador"}
        }
    else:
        raise HTTPException(
            status_code=401, 
            detail="Credenciales incorrectas. Verifique correo y contraseña."
        )