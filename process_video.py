import cv2
import numpy as np
from retinaface import RetinaFace

# Function to process the video and apply blur/unblur
def process_video(video_path, encryption_key_path, decrypt=False):
    # Load encryption key
    try:
        encryption_key = np.load(encryption_key_path, allow_pickle=True)
    except FileNotFoundError:
        print(f"Error: Encryption key file '{encryption_key_path}' not found.")
        return
    
    # Convert the encryption key to a deterministic number (like a seed)
    key_seed = sum(ord(char) for char in encryption_key.item())  # Example of converting string to integer seed
    
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Prepare the output video writer
    output_path = "./output/processed_video.mp4"
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
                
                # Calculate the blur strength using the key_seed (encryption key influence)
                blur_strength = ((key_seed % 10) * 4 + 5)  # Increase the multiplier and base value
                
                # Apply blur or unblur based on decrypt flag
                if decrypt:
                    # Instead of blurring, we may choose to apply a "reverse" effect (e.g., sharpness enhancement).
                    # This is just a simulation since exact unblurring is not possible.
                    unblurred_face = cv2.fastNlMeansDenoisingColored(frame[y1:y2, x1:x2], None, 10, 10, 7, 21)
                    frame[y1:y2, x1:x2] = unblurred_face
                else:
                    # Apply Gaussian blur to the face ROI
                    blurred_face = cv2.GaussianBlur(frame[y1:y2, x1:x2], (blur_strength, blur_strength), 20)
                    frame[y1:y2, x1:x2] = blurred_face

                # Draw bounding box and landmarks (same as before)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                for key, value in landmarks.items():
                    if isinstance(value, tuple):
                        cv2.circle(frame, value, 3, (0, 0, 255), -1)

        # Write the processed frame to the output video
        out.write(frame)

    # Release the video capture and writer objects
    video_capture.release()
    out.release()
    print(f"Processed video saved to {output_path}")

# Example usage
video_path = "./data/sample.mp4"  # Path to your video file
encryption_key_path = "./data/encryption_key.npy"  # Path to your encryption key (if applicable)

# Call the process_video function
process_video(video_path, encryption_key_path, decrypt=False)  # Set decrypt=True for unblurring
