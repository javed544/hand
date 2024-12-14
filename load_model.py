import joblib
from preprocessing import preprocess_image

# Load
model = joblib.load('svm_digit_recognizer.pkl')

# Preprocess
image_path = "assets\handwritten_numbers.png"
preprocessed_image = preprocess_image(image_path)

# Predict
predicted_digit = model.predict(preprocessed_image)
print(f"Predicted digit: {predicted_digit}")