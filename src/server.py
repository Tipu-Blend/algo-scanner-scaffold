# src/server.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn

app = FastAPI(
    title="BSE Alfa Scanner Infrastructure Engine",
    description="Public structural plumbing for multi-threaded market data routing.",
    version="1.0.0"
)

# Enable CORS so your mobile application can securely fetch data from this Mac server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your mobile app's network origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model to guarantee strict structural data formatting for API communications
class ScannerStatus(BaseModel):
    server_status: str
    active_threads: int
    processed_tickers_count: int
    latest_signals: List[Dict[str, Any]]

@app.get("/", tags=["Root"])
def read_root():
    """
    Server Health Check Endpoint.
    Verifies the network pipeline is active on your Mac.
    """
    return {"status": "ONLINE", "message": "Infrastructure core running smoothly."}

@app.get("/api/scanner-status", response_model=ScannerStatus, tags=["Mobile API"])
def get_scanner_status():
    """
    PUBLIC SAFE API ENDPOINT FOR MOBILE COMMUNICATIONS
    
    Your mobile app calls this endpoint to get the latest scanned data.
    Notice how this controller contains ZERO trading math. It simply reads
    pre-filtered results from memory/cache or data engines.
    """
    try:
        # STRUCTURAL SCAFFOLDING PLACEHOLDER
        # In execution, this reads from your engine's multi-threaded cache layer.
        mock_data = {
            "server_status": "SCANNING_ACTIVE",
            "active_threads": 8,
            "processed_tickers_count": 0,
            "latest_signals": []  # Your local backend populates this; public repository stays clean.
        }
        return mock_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    # Runs the local development server on port 8000
    uvicorn.run("src.server:app", host="0.0.0.0", port=8000, reload=True)

