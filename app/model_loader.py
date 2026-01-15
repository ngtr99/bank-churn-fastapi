import joblib

MODEL_PATH = "model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()



