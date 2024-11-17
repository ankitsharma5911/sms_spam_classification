from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load("artifacts/model.pkl")  # Replace with your actual model path
vectorizer = joblib.load("artifacts/vectorizer.pkl")  # Replace with your vectorizer

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        sms_text = request.form.get("sms-text")
        if sms_text:
            transformed_text = vectorizer.transform([sms_text])
            prediction = model.predict(transformed_text)[0]
            prediction = "Spam" if prediction == 1 else "Not Spam"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
