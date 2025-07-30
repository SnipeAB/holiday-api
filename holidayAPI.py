from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI()

# Load holidays from JSON file once
holiday_file = Path("data/holidays.json")
with holiday_file.open() as f:
    holidays = json.load(f)

@app.get("/")
def root():
    return {"message": "Welcome to the Obscure Holiday API!"}

@app.get("/holiday")
def get_holiday(date: str = Query(..., pattern=r"^\d{2}-\d{2}$")):
    if date in holidays:
        return {
            "date": date,
            "holidays": holidays[date]
        }
    return JSONResponse(status_code=404, content={
        "message": f"No holidays found for {date}."
    })

@app.get("/today")
def get_today_holiday():
    from datetime import datetime
    today = datetime.now().strftime("%d-%m")
    if today in holidays:
        return {
            "date": today,
            "holidays": holidays[today]
        }
    return JSONResponse(status_code=404, content={
        "message": f"No holidays found for today ({today})."
    })