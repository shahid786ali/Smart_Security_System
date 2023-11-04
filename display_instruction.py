
import tkinter as tk
from tkinter import messagebox

def display_instructions():
    instructions = """
    **Recording Video Instructions:**

    1. Click the "Record" button to start recording video using your system's camera.
    2. A window will open displaying the live video feed from your camera.
    3. The video is saved as an AVI file in the "recordings" folder of the system.
    4. The filename will be in the format "HH-MM-SS.avi" to represent the time of the recording.
    5. You can stop the recording at any time by pressing the 'Esc' key.
    6. The recorded video will be automatically saved in the "recordings" folder when you stop the recording.
    7. To view the recorded video, you can access it in the "recordings" folder.
    8. Enjoy capturing and recording moments with your smart security system!

    **Motion Detection Instructions:**

    1. Click the "Focused" button to enable motion detection using your system's camera.
    2. A new window will open displaying the live video feed from your camera.
    3. In this window, you can select a specific region of interest (ROI) for motion detection. Click the left mouse button to set the top-left corner of the ROI and the right mouse button to set the bottom-right corner.
    4. The system will continuously monitor the selected region for any motion.
    5. If motion is detected in the selected region, the system will highlight the moving object with a green rectangle and play a sound alert.
    6. If no motion is detected, the system will display "NO-MOTION" on the screen.
    7. To exit the motion detection mode, press the 'Esc' key.
    8. Enjoy monitoring and detecting motion in your selected area with your smart security system!

    **Access Control Instructions:**

    1. Click the "Access Control" button to activate the access control feature using your system's camera.
    2. A new window will open, displaying the live video feed from your camera.
    3. The system will continuously monitor the area for any unauthorized individuals.
    4. If an unauthorized person is detected in the camera's view, the system will trigger an alarm.
    5. The alarm can be a sound alert or a visual indicator, depending on your system configuration.
    6. You can set the parameters and criteria for what constitutes an "unauthorized person." This may include face recognition, object detection, or other criteria.
    7. To exit the access control mode, you can press the 'Esc' key.
    8. Ensure that your camera is correctly positioned and that the system is properly configured to detect unauthorized individuals.
    9. Access Control is a powerful security feature to help protect your premises and ensure only authorized individuals have access.
    10. Enjoy the enhanced security and peace of mind provided by your smart security system!

    **Add Video Instructions:**

    1. Click the "Add Video" button to upload and save a video of an authorized person. This video will be used as a reference for authorized individuals.
    2. A new window will open for video upload and saving.
    3. Follow these steps to upload and save the video:
       - Click the "Browse Video" button to select the video file.
       - Enter a name for the video in the "Enter Video Name" field.
       - Make sure the video contains a clear face of the authorized person and is not greater than three minutes in duration.
    4. Once you've selected the video and provided a name, click the "Save Video" button.
    5. The system will process and save the video as a reference for authorized individuals. The saved video will be used for comparison during access control.
    6. You will receive a confirmation message once the video is successfully saved.
    7. Enjoy the enhanced security provided by your smart security system with the added reference video!

    **Note:** Ensure that the uploaded video accurately represents an authorized person, and that it is not greater than three minutes in duration. Properly configure your access control criteria for accurate comparison with the saved video.
    """
    messagebox.showinfo("Instructions", instructions)
