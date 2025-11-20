from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import plotly.graph_objs as go
import plotly.offline as pyo
import os

app = Flask(__name__)

# ----------------------------
# LOAD MODELS & SCALERS
# ----------------------------
# Path to 'models' folder
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")

# Load models
clf_model = load_model(os.path.join(MODEL_PATH, "clf_model.keras"))
reg_model = load_model(os.path.join(MODEL_PATH, "reg_model_log.keras"))

# Load scalers
with open(os.path.join(MODEL_PATH, "scaler_clf.pkl"), "rb") as f:
    scaler_clf = pickle.load(f)
with open(os.path.join(MODEL_PATH, "scaler_reg.pkl"), "rb") as f:
    scaler_reg = pickle.load(f)

# ----------------------------
# HELPER FUNCTION
# ----------------------------
def predict_fire_and_area(sample):
    """
    Predicts fire occurrence probability and burned area (log-transformed model).
    """
    # Convert dict → DataFrame
    sample_df = pd.DataFrame([sample])
    sample_df = pd.get_dummies(sample_df, columns=["month", "day"], drop_first=True)

    # Align with training columns
    sample_df = sample_df.reindex(columns=scaler_clf.feature_names_in_, fill_value=0)

    # 🔥 Fire occurrence (Classification)
    sample_scaled_clf = scaler_clf.transform(sample_df)
    fire_prob = clf_model.predict(sample_scaled_clf, verbose=0)[0][0]
    fire_flag = fire_prob > 0.5

    burned_area = None
    burned_area_graph = None

    # 🔥 Burned area (Regression, log-transformed)
    if fire_flag:
        sample_scaled_reg = scaler_reg.transform(sample_df)
        log_pred = reg_model.predict(sample_scaled_reg, verbose=0)[0][0]
        burned_area = np.expm1(log_pred)  # reverse log1p transform (no +1 added)

        # Simple Plotly bar chart
        fig = go.Figure([
            go.Bar(
                x=["Predicted Burned Area (hectares)"],
                y=[burned_area],
                marker_color="firebrick"
            )
        ])
        fig.update_layout(
            title="🔥 Predicted Burned Area",
            yaxis_title="Hectares",
            template="plotly_white"
        )
        burned_area_graph = pyo.plot(fig, output_type='div', include_plotlyjs=False)

    return fire_prob, fire_flag, burned_area, burned_area_graph


# ----------------------------
# FLASK ROUTES
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    graph = None

    if request.method == "POST":
        try:
            sample = {
                "temperature": float(request.form["temperature"]),
                "humidity": float(request.form["humidity"]),
                "wind": float(request.form["wind"]),
                "rain": float(request.form["rain"]),
                "FFMC": float(request.form["FFMC"]),
                "DMC": float(request.form["DMC"]),
                "DC": float(request.form["DC"]),
                "ISI": float(request.form["ISI"]),
                "month": request.form["month"],
                "day": request.form["day"]
            }

            fire_prob, fire_flag, burned_area, burned_area_graph = predict_fire_and_area(sample)

            result = {
                "fire_probability": round(fire_prob * 100, 2),
                "fire_occurred": fire_flag,
                "burned_area": round(burned_area, 2) if burned_area is not None else None
            }
            graph = burned_area_graph

        except Exception as e:
            result = {"error": f"❌ Error: {str(e)}"}

    return render_template("index.html", result=result, graph=graph)


# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
