import cv2
import pyautogui as p
import os

def AuthenticateFace():
    """
    Attempts face authentication. Returns 0 to skip if trainer not found.
    """
    # Use absolute path
    base_path = os.path.dirname(os.path.abspath(__file__))
    trainer_path = os.path.join(base_path, 'trainer', 'trainer.yml')
    
    # Check if trainer file exists before attempting
    if not os.path.exists(trainer_path):
        print(f"⚠ Face recognition model not found at {trainer_path}. Skipping authentication.")
        print("  To enable: Run assist\\Engine\\auth\\sample.py then trainer.py")
        return 0  # Skip authentication
    
    # Load the trained LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    try:
        recognizer.read(trainer_path)
    except Exception as e:
        print(f"⚠ Error loading face recognizer: {e}")
        print("  Skipping face authentication.")
        return 0

    # Load Haar Cascade for face detection
    cascade_path = os.path.join(base_path, 'haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier(cascade_path)

    font = cv2.FONT_HERSHEY_SIMPLEX

    names = ['', 'Raj']

    print("Opening camera for face authentication...")
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    
    if not cam.isOpened():
        print("⚠ Cannot open camera. Skipping face authentication.")
        p.alert("Camera not available. Skipping face authentication.", "Face Auth")
        return 0

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    auth_count = 0  # Counter for consistent recognition
    frame_count = 0  # Add frame counter for timeout
    max_frames = 600  # 60 seconds timeout (increased)
    
    print("Camera opened successfully. Looking for face...")

    while True:
        ret, img = cam.read()
        
        if not ret:
            print("⚠ Failed to read from camera.")
            break
            
        frame_count += 1
        if frame_count > max_frames:
            print("⚠ Face authentication timeout. Skipping.")
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            accuracy = round(100 - confidence)

            if accuracy > 35:  # Even lower threshold for easier recognition
                name = names[id]
                auth_count += 1
                label = f"{name} {accuracy}%"
            else:
                name = "unknown"
                auth_count = 0
                label = f"{name} {accuracy}%"

            cv2.putText(img, label, (x + 5, y - 5), font, 1, (255, 255, 255), 2)

        # Add frame counter on screen
        cv2.putText(img, f"Frame: {frame_count}/{max_frames}", (10, 30), font, 0.6, (255, 255, 255), 1)

        cv2.imshow('Face Authentication - Buddy', img)
        
        # Set window to always on top
        cv2.setWindowProperty('Face Authentication - Buddy', cv2.WND_PROP_TOPMOST, 1)

        k = cv2.waitKey(10) & 0xff
        if k == 27:  # ESC key
            break

        # Require 2 consistent recognitions to return success
        if auth_count >= 2:
            cam.release()
            cv2.destroyAllWindows()
            return 1  # Authenticated

    cam.release()
    cv2.destroyAllWindows()
    return 0  # Not authenticated

