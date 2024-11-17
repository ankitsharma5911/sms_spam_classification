import streamlit as st
import joblib

# Load your trained model
model = joblib.load("artifacts/model.pkl")  # Replace with your actual model path
vectorizer = joblib.load("artifacts/vectorizer.pkl")  # Replace with your vectorizer


# Streamlit app
st.title("📩 SMS Spam Detection")

st.image(
    "static/sms_image.png",
    caption="Is your message spam or not?",
    use_column_width=True,
)

st.subheader("Enter the SMS message below:")
sms_text = st.text_area("Type your message here...")

if st.button("Detect Spam"):
    if sms_text.strip():
        # Preprocess and predict
        transformed_text = vectorizer.transform([sms_text])
        prediction = model.predict(transformed_text)[0]
        result = "Spam" if prediction == 1 else "Not Spam"

        # Display the result
        st.success(f"The message is classified as: **{result}**")
    else:
        st.error("Please enter a valid SMS message.")
