#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import pyttsx3
print("please choose one service:")
print("detected face and blurface or background")

print('''1.blur the face
2.blur the background 
''')
engine = pyttsx3.init()
engine.setProperty('rate', 120)  # Speed of speech. Default is 200.
engine.setProperty('volume', 0.9)  # Volume level. Range is from 0.0 to 1.0.
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Voice selection.

engine.say("please enter the service press one for blur the face press two for blur the background  ")
engine.runAndWait()
choice=int(input("enter what do you want:"))
if choice == 1:
    # Load the pre-trained Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Open the video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Blur and replace the detected faces
        for (x, y, w, h) in faces:
            # Extract the region of interest (face)
            face = frame[y:y+h, x:x+w]

            # Apply Gaussian blur to the face
            blurred_face = cv2.GaussianBlur(face, (99, 99), 30)

            # Replace the detected face with the blurred version
            frame[y:y+h, x:x+w] = blurred_face

        # Display the resulting frame
        cv2.imshow("Blurred Faces", frame)

        # Check for the 'enter' key to exit
        if cv2.waitKey(10) ==13:
            break

    # Release the video capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()
    
if choice == 2:
    # Load the Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('myhaarcascade_frontalface_default.xml')

    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Apply a blur effect to the background
        blurred = cv2.GaussianBlur(frame, (99, 99), 0)

        # Process each detected face
        for (x, y, w, h) in faces:
            # Extract the region of interest (face) from the frame
            face = frame[y:y+h, x:x+w]
        
            # Replace the face region with the original, unblurred face
            blurred[y:y+h, x:x+w] = face

        # Display the result
        cv2.imshow('Background Blur with Visible Face', blurred)

        # Exit the loop if the 'enter' key is pressed
        if cv2.waitKey(10)==13:
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()
    


# In[ ]:




