import cv2
import mediapipe as mp

# Initialize Mediapipe face detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Provide the file path to your input video
video_path = '6574256-hd_1280_720_25fps.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the video frame width, height, and frames per second (FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object to save the output video
output_path = 'output_video.mp4'  # Set the output file name
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Initialize face detection model
with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to RGB for Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        results = face_detection.process(frame_rgb)

        if results.detections:
            for detection in results.detections:
                # Get the bounding box for the face
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                # Extract the region of interest (ROI) for the face
                face_roi = frame[y:y+h, x:x+w]

                # Apply Gaussian blur to the face ROI
                blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 20)

                # Place the blurred face back into the original frame
                frame[y:y+h, x:x+w] = blurred_face

        # Write the frame with blurred faces to the output video
        out.write(frame)

        # Display the result (optional)
        cv2.imshow('Blurred Faces', frame)

        # Exit the loop when the ENTER key is pressed
        if cv2.waitKey(1) == 13:
            break

# Release the video capture and writer objects and close the window
cap.release()
out.release()
cv2.destroyAllWindows()
