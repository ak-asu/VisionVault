import cv2
import numpy as np
from retinaface import RetinaFace

# Function to process the video
def process_video(video_path, encryption_key_path, decrypt=False):
    # Load encryption key
    try:
        encryption_key = np.load(encryption_key_path)
    except FileNotFoundError:
        print(f"Error: Encryption key file '{encryption_key_path}' not found.")
        return

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Prepare the output video writer
    output_path = "processed_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert the frame to RGB (since RetinaFace expects RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces using RetinaFace
        faces = RetinaFace.detect_faces(rgb_frame)

        if faces:
            for face in faces.values():
                # Extract bounding box and landmarks
                x1, y1, x2, y2 = face['facial_area']
                landmarks = face['landmarks']
                
                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Draw landmarks
                for key, value in landmarks.items():
                    if isinstance(value, tuple):  # Ensure value is a tuple (x, y)
                        cv2.circle(frame, value, 3, (0, 0, 255), -1)

                # Optionally, add confidence score (RetinaFace doesn't directly return confidence, 
                # but you can add custom logic to determine confidence)

        # Write the frame to the output video
        out.write(frame)

    # Release the video capture and writer objects
    video_capture.release()
    out.release()
    print(f"Processed video saved to {output_path}")

# Example usage
video_path = "855565-hd_1920_1080_24fps.mp4"  # Path to your video file
encryption_key_path = "encryption_key.npy"  # Path to your encryption key (if applicable)

# Call the process_video function
process_video(video_path, encryption_key_path)
