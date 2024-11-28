from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from functioncall import ModelInference

# FastAPI-Instanz erstellen
app = FastAPI()

# Modell laden (globaler Kontext für die API)
model_path = 'NousResearch/Hermes-2-Pro-Llama-3-8B'  # Oder Pfad zu deinem Modell
inference = ModelInference(model_path, "chatml", load_in_4bit="False")

# Pydantic-Schema für die API-Eingaben
class QueryRequest(BaseModel):
    query: str
    max_depth: int = 5
    num_fewshot: int = 0

# API-Endpoint: Root
@app.get("/")
async def root():
    return {"message": "Welcome to the LLM Function Calling API"}

# API-Endpoint: Anfrage an das Modell
@app.post("/query/")
async def process_query(request: QueryRequest):
    try:
        # Anfrage an das Modell weiterleiten
        output = inference.generate_function_call(
            query=request.query,
            chat_template="chatml",
            num_fewshot=request.num_fewshot,
            max_depth=request.max_depth,
        )
        return {"status": "success", "response": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
