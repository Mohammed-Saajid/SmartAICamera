import cv2
import numpy as np

def is_camera_blocked(frame, threshold=10):
    """
    Detects if the camera is blocked by checking the brightness variance of the frame.
    :param frame: The current frame from the video feed.
    :param threshold: Variance threshold to detect if the camera is blocked (lower values indicate blockage).
    :return: True if the camera is blocked, False otherwise.
    """
    # Convert the frame to grayscale (to simplify brightness checking)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the variance of pixel intensities in the grayscale image
    variance = np.var(gray)

    # If the variance is below the threshold, we assume the camera is blocked
    if variance < threshold:
        return True
    return False

# Start the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Check if the camera is blocked
    if is_camera_blocked(frame):
        cv2.putText(frame, "Camera Blocked!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "Camera Clear", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the current frame
    cv2.imshow('Camera Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()