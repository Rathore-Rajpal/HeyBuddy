import cv2
import numpy as np
from PIL import Image
import os

path = 'assist\\Engine\\auth\\samples'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("assist\\Engine\\auth\\haarcascade_frontalface_default.xml")

def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img, 'uint8')

        img_arr = cv2.equalizeHist(img_arr)

        try:
            id = int(os.path.split(imagePath)[-1].split(".")[1])
        except:
            print(f"Filename format incorrect: {imagePath}")
            continue

        faces = detector.detectMultiScale(img_arr, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))

        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y + h, x:x + w])
            ids.append(id)

    return faceSamples, ids

print("Training faces...")

faces, ids = Images_And_Labels(path)

if faces and ids:
    recognizer.train(faces, np.array(ids))
    recognizer.write('assist\\Engine\\auth\\trainer\\trainer.yml')
    print("Model trained successfully.")
else:
    print("No faces found or training data is empty.")
