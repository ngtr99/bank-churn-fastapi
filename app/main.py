from fastapi import FastAPI
from fastapi import HTTPException
import numpy as np
import os

from app.schemas import ChurnFeatures
from app.model_loader import model

from fastapi import Request
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Customer Churn Prediction API",
              description="An API that predicts customer churn using a pre-trained model.",
              version="1.0.0")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Handle favicon requests to prevent 404/500 errors"""
    try:
        return Response(status_code=204, headers={"Content-Type": "image/x-icon"})
    except Exception:
        # Fallback to ensure no errors are raised
        return Response(status_code=204)


# Use absolute path for static files to work correctly on Vercel
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory="app/templates")
@app.get("/", response_class=HTMLResponse)
def web(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})




@app.post("/predict/")
def predict(payload: ChurnFeatures):
    X = np.array([[
        payload.customer_id,
        payload.credit_score,
        payload.country,
        payload.gender,
        payload.age,
        payload.tenure,
        payload.balance,
        payload.products_number,
        payload.credit_card,
        payload.active_member,
        payload.estimated_salary
        ]], dtype=object)

    try: 
        pred = model.predict(X)[0]
    except Exception as e:
        raise HTTPException (
            status_code = 400,
            detail=f"Prediction error: {e}"
        )
    
    proba = None
    if hasattr(model, "predict_proba"):
        try:
            proba = float(model.predict_proba(X)[0][1])
        except Exception:
            proba = None
    
    return {
        "churn_prediction": int(pred),
        "churn_probability": None if proba is None else round(proba, 4)
    }

