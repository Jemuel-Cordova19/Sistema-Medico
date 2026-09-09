from fastapi import FastAPI

# Creamos la instancia de la aplicación
app = FastAPI(title="Sistema Médico API")

# Ruta principal de prueba
@app.get("/")
def inicio():
    return {
        "mensaje": "Servidor del Sistema Médico funcionando correctamente desde la subrama"
    }