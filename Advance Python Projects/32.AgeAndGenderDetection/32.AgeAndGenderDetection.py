import cv2
import numpy as np
from keras.models import load_model

# Load the pre-trained models
age_model_path = 'path_to_downloaded_weights/weights.28-3.73.hdf5'
gender_model_path = 'path_to_downloaded_weights/weights.28-3.73.hdf5'

age_model = load_model(age_model_path, compile=False)
gender_model = load_model(gender_model_path, compile=False)

# Ensure the path to the Haarcascade XML file is correct
haar_cascade_path = 'D:/60 Python Projects/Advance Python Projects/17.ComputerVisionProjects/Haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# Function to preprocess the input imagedd
def preprocess_input(img):
    img = cv2.resize(img, (64, 64))
    img = img.astype("float") / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Function to detect gender and age
def detect_gender_age(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        face = preprocess_input(face)

        gender_pred = gender_model.predict(face)[0]
        age_pred = age_model.predict(face)[0]

        print("Gender prediction:", gender_pred)  # Debugging print
        print("Age prediction:", age_pred)        # Debugging print

        # Extract the gender prediction
        gender = "Male" if gender_pred[0] > 0.5 else "Female"

        # Extract the age prediction
        age = int(np.argmax(age_pred))

        label = f"{gender}, {age}"
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    return img

# Load an example image
img = cv2.imread('path_to_image.jpg')
if img is None:
    raise ValueError("Image not found or unable to load")

output_img = detect_gender_age(img)

# Display the output
cv2.imshow('Gender and Age Detection', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
