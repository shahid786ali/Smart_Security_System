import tkinter as tk
from tkinter import filedialog
import cv2

def emp_video():
    window = tk.Tk()  # Create the main window
    window.title("Video Upload and Save")

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        if file_path:
            video_path_entry.delete(0, tk.END)
            video_path_entry.insert(0, file_path)

    def save_video():
        video_path = video_path_entry.get()
        video_name = video_name_entry.get()

        if video_path and video_name:
            try:
                cap = cv2.VideoCapture(video_path)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                output_path = f"output/{video_name}.avi"  # Change the output folder as needed
                out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    out.write(frame)

                cap.release()
                out.release()
                cv2.destroyAllWindows()
                result_label.config(text=f"Video '{video_name}' saved successfully.")
            except Exception as e:
                result_label.config(text=f"Error: {str(e)}")
        else:
            result_label.config(text="Please select a video and enter a video name.")

    # Create and pack instruction label
    instruction_label = tk.Label(window, text="The Employee face is clearly in the video and not greater than three minutes.")
    instruction_label.pack(pady=10)

    # Create widgets
    browse_button = tk.Button(window, text="Browse Video", command=browse_file)
    video_path_entry = tk.Entry(window, width=40)
    video_name_label = tk.Label(window, text="Enter Video Name:")
    video_name_entry = tk.Entry(window, width=40)
    save_button = tk.Button(window, text="Save Video", command=save_video)
    result_label = tk.Label(window, text="")

    # Pack widgets
    browse_button.pack(pady=10)
    video_path_entry.pack()
    video_name_label.pack(pady=10)
    video_name_entry.pack()
    save_button.pack(pady=10)
    result_label.pack()

    window.mainloop() 