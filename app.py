from flask import Flask, request, render_template
import pickle

# Dummy model class (define karna zaroori hai pickle ke liye)
class DummyModel:
    def predict(self, X):
        return [1 if x[0] > 5000 else 0 for x in X]  # simple fraud logic

# Flask app
app = Flask(__name__)

# Model load karo
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    amount = float(request.form["amount"])
    txn_type = int(request.form["type"])  # credit/debit
    age = int(request.form["age"])

    result = model.predict([[amount, txn_type, age]])[0]
    output = "Fraud Transaction 🚨" if result == 1 else "Legit Transaction ✅"

    return render_template("index.html", prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
