# Handwritten Digit Recognition

This project implements a handwritten digit recognition system using Python and Scikit-learn. The system processes custom images of handwritten digits, trains a Support Vector Machine (SVM) model on the Scikit-learn `digits` dataset, and predicts the digits from new images.

## Features

- **Image Preprocessing**: Resize and normalize custom images to 8x8 pixels.
- **Model Training**: Train an SVM classifier using Scikit-learn's `digits` dataset.
- **Prediction**: Classify digits from preprocessed images using the trained model.

## Demo Video

https://github.com/user-attachments/assets/76f3ef5f-d52d-4615-98ae-4867ea490571



## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/handwritten-digit-recognition.git
   cd handwritten-digit-recognition
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Train the Model**:
   ```bash
   python train_model.py
   ```

2. **Predict Digits**:
   ```bash
   python predict.py --image path_to_your_image.png
   ```

## Project Structure

- `train_svm.py`: Script to train and save the SVM model.
- `load_model.py`: Script to load the model and predict digits from custom images.
- `preprocessing.py`: Contains functions to preprocess images for the model.

## Dependencies

- OpenCV
- Numpy
- Scikit-learn

## License

This project is licensed under the MIT License.

## Acknowledgements

- Scikit-learn for the `digits` dataset and machine learning tools.
- OpenCV for image preprocessing.

## Contact

For questions or suggestions, please open an issue or contact me.
