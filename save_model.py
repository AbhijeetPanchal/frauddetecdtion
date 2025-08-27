import pickle

# Dummy model (simple function jaisa hi behave karega)
class DummyModel:
    def predict(self, X):
        # Bas ek dummy rule: agar amount > 10000 toh Fraud, warna Not Fraud
        return ["Fraud" if x[0] > 10000 else "Not Fraud" for x in X]

# Model object
model = DummyModel()

# Model ko pickle file me save karna
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Dummy model saved as model.pkl")
