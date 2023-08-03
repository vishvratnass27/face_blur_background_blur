
# Face Blurring with OpenCV

This repository contains a Python script that demonstrates two functionalities for blurring faces in images or webcam video using OpenCV and Haar Cascade classifiers.

## Features

1. Blur the Face:
   - The script captures video from the webcam.
   - It detects faces in real-time using a pre-trained Haar Cascade classifier.
   - The detected faces are then replaced with a Gaussian blur effect, obscuring the identity while preserving the surrounding background.

2. Blur the Background with Visible Face:
   - The script captures video from the webcam.
   - It detects faces in real-time using a custom Haar Cascade classifier.
   - The background of the video is blurred using a Gaussian blur effect, while the detected faces remain visible and unblurred.

## Dependencies

- Python
- OpenCV
- pyttsx3 (optional, for text-to-speech)

## How to Use

1. Clone the repository to your local machine.
2. Make sure you have Python installed along with the required dependencies listed above.
3. Run the "face_blurring.py" script.
4. Choose one of the provided services (1 or 2) by entering the corresponding number.
5. If you select option 1, the webcam will be activated, and the faces will be blurred in real-time.
6. If you select option 2, the webcam will be activated, and the background will be blurred while the detected faces remain visible.

## Explanation of the Code

1. For the "Blur the Face" functionality, the script utilizes the Haar Cascade classifier to detect faces in each frame of the webcam video. It then applies a Gaussian blur to the detected face region and replaces it with the blurred version.

2. For the "Blur the Background with Visible Face" functionality, the script again uses a Haar Cascade classifier to detect faces in each frame. However, this time, it applies a Gaussian blur to the entire background while preserving the detected faces, resulting in a more privacy-focused effect.

## Note

- The script uses Haar Cascade classifiers for face detection. You can experiment with different classifiers or fine-tune the parameters for better face detection performance.

Feel free to modify the script, add more functionalities, or use it as a starting point for other computer vision projects! Enjoy blurring faces while maintaining privacy and exploring the world of OpenCV. 🎭🎥

# Author

The script was created by Vishvratna Shegaonkar.

