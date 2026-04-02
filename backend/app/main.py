from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.database import check_db_connection

app = FastAPI(title="CashFriend API", version="0.1.0")


@app.get("/health")
def health():
    db_ok = check_db_connection()
    status = "ok" if db_ok else "degraded"
    return JSONResponse(
        status_code=200 if db_ok else 503,
        content={"status": status, "database": "connected" if db_ok else "unreachable"},
    )
