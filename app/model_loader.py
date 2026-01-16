import joblib
import os

# Get model path - works both locally and in Docker
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()



