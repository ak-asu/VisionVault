# VisionVault – AI-Powered Face Blurring with Cryptographic Access  


## 📌 Overview  
VisionVault is an advanced computer vision application that automatically blurs faces in videos to help individuals with scopophobia while allowing authorized users to unblur them using a secure cryptographic key. This system ensures privacy, security, and controlled access to sensitive visual content, making it ideal for personal safety, surveillance, and content moderation.  


## 🔥 Key Features  
✅ **Real-Time Face Blurring** – AI-powered face detection for instant, seamless blurring.  
✅ **Adjustable Blur Intensity** – Users can modify the blur level based on preference.  
✅ **Selective & Context-Aware Blurring** – Choose specific faces or apply smart scene-based blurring.  
✅ **Hierarchical Access Control** – Role-based permissions allow different access levels (e.g., managers vs. public users).  
✅ **Cryptographic Blurring & Reversible Encryption** – Secure facial encryption, allowing only authorized users to decrypt and view unblurred faces.  
✅ **Crowd Density Detection** – Automatically adjusts blurring based on the number of faces detected.  
✅ **Scalability & Integration** – Cloud-based or edge-computing deployment with API support for third-party applications.  


## 🛠️ Tech Stack  
- **Programming Language**: Python  
- **AI/ML Models**: Convolutional Neural Networks (CNNs) for face detection  
- **Computer Vision**: OpenCV, MediaPipe  
- **Cryptography**: AES-based reversible blurring  
- **Frameworks**: PyTorch  


## 📌 Use Cases
- **Scopophobia Support** – Helps individuals by obscuring distressing facial visuals.
- **Privacy & Security** – Protects identities in videos while allowing authorized access.
- **Corporate & Government Use** – Enables controlled access to surveillance footage or sensitive video content.


## 🏗️ Future Enhancements
- 🚀 **Advanced Face Recognition** – Improve face detection accuracy with additional deep learning models.
- 🔐 **Enhanced Security** – Add stronger encryption methods for face blurring and deblurring.
- 📱 **Mobile Support** – Expand usability with mobile apps for real-time video processing.
    

## 📂 Project Structure  

VisionVault/
│── data/                   # Directory to store input videos and encryption key
│   ├── 855565-hd_1920_1080_24fps.mp4
│   ├── encryption_key.npy
│
│── output/                 # Directory to store processed videos
│   ├── processed_video.mp4
│
│── src/                    # Source code directory
│   ├── process_video.py    # Main script for face detection and video processing
│
│── requirements.txt        # List of dependencies
│── README.md               # Project documentation
│── .gitignore              # Files to ignore in version control


## Requirements
Ensure you have the following dependencies installed:
- OpenCV (`cv2`)
- NumPy (`numpy`)
- RetinaFace (`retinaface`)

You can install them using:
```sh
pip install opencv-python numpy retinaface
```


## Usage
1. Place your video file in the working directory.
2. Ensure you have an encryption key file (`encryption_key.npy`), or modify the script accordingly.
3. Run the script with:
   ```sh
   python process_video.py
   ```


## Code Breakdown
- **Loading Encryption Key**: The script attempts to load an encryption key from a `.npy` file.
- **Reading the Video**: It opens the given video file and extracts frame properties such as width, height, and frames per second (FPS).
- **Face Detection**: Using RetinaFace, faces in each frame are detected, and bounding boxes and landmarks are drawn.
- **Saving the Processed Video**: The annotated frames are written to a new video file named `processed_video.mp4`.


## Output
The processed video with face annotations is saved as `processed_video.mp4` in the working directory.


## Example
To run the script on a sample video:
```sh
python process_video.py 855565-hd_1920_1080_24fps.mp4 encryption_key.npy
```


## Notes
- The encryption key functionality is currently a placeholder and does not encrypt/decrypt the video.
- RetinaFace detects faces in RGB format, so frames are converted before processing.
- The script assumes valid input files; ensure the paths are correct.


## License
This project is open-source and available for modification and improvement.


## Custom Dataset
https://drive.google.com/drive/folders/1wfgyXzWDGkPZoZpFUNPdrNgyCPUq9KHE


