import joblib
import os

# Get model path - works both locally and in Docker
# In Docker: /app/model.pkl
# Locally: ./model.pkl (from project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. "
            f"Current working directory: {os.getcwd()}. "
            f"Base directory: {BASE_DIR}"
        )
    return joblib.load(MODEL_PATH)

model = load_model()



