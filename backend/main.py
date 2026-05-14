from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import ccxt
import numpy as np
import uvicorn
import asyncio

app = FastAPI(title="Aegis Intelligence")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return {"status": "Aegis Live 🟢", "btc_price": 43250}

@app.get("/api/markets")
async def markets():
    return {
        "BIST100": 10234.5,
        "NASDAQ": 15234.2,
        "BTC": 43250.0,
        "GOLD": 1987.3
    }

@app.post("/api/risk")
async def risk(data: dict):
    var = abs(np.percentile(np.random.normal(0, 0.02, 10000), 5)) * 100
    return {"VaR95": f"{var:.2f}%", "montecarlo": "+12.4%"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)