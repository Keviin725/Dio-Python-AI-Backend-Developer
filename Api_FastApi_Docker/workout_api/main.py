from fastapi import FastAPI

app = FastAPI(title="Workout API")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True)





#Comando para rodar o server
#uvicorn workout_api.main:app --reload

#Comando para ativar ambiente virtual
# .\Scripts\activate.bat