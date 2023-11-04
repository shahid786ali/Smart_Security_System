
import tkinter as tk
import tkinter.font as font
from display_instruction import display_instructions
# from in_out import in_out
# from motion import noise
from rect_noise import rect_noise
from record import record
# from regemp import emp_video
from emp_video import emp_video
# from EmpRecord import emp_record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart System")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('950x720')

frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart Security System")
label_font = font.Font(size=34, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/spy.png')
# icon.thumbnail((150, 150), Image.ANTIALIAS)
icon = icon.resize((150,150), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/record1.png')   #lamp
btn1_image = btn1_image.resize((50,50), Image.Resampling.LANCZOS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/focus.png') #rectangle-of-cutted-line-geometrical-shape.png
btn2_image = btn2_image.resize((50,50), Image.Resampling.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.Resampling.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.Resampling.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)

# btn6_image = Image.open('icons/incognito.png')
# btn6_image = btn6_image.resize((50,50), Image.Resampling.LANCZOS)
# btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50,50), Image.Resampling.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/live_streaming_icon.png')
btn7_image = btn7_image.resize((60,60), Image.Resampling.LANCZOS)
btn7_image = ImageTk.PhotoImage(btn7_image)

btn8_image = Image.open('icons/vedio.png')
btn8_image = btn8_image.resize((50,50), Image.Resampling.LANCZOS)
btn8_image = ImageTk.PhotoImage(btn8_image)
 
btn9_image = Image.open('icons/model.png')
btn9_image = btn9_image.resize((50,50), Image.Resampling.LANCZOS)
btn9_image = ImageTk.PhotoImage(btn9_image) 

btn10_image = Image.open('icons/Help.png')
btn10_image = btn10_image.resize((50,50), Image.Resampling.LANCZOS)
btn10_image = ImageTk.PhotoImage(btn10_image)

# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='Record', height=90, width=200, fg='green', command=record, image=btn1_image, compound='left') # command=record,
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn2 = tk.Button(frame1, text='Focused', height=90, width=200, fg='Green', command=rect_noise, compound='left', image=btn2_image)#
btn2['font'] = btn_font
btn2.grid(row=4, pady=(20,10),  padx=(20,5)) #column=3

btn_font = font.Font(size=25)
# btn3 = tk.Button(frame1, text='Noise', height=90, width=200, fg='green', command=noise, image=btn3_image, compound='left')
# btn3['font'] = btn_font
# btn3.grid(row=5, pady=(20,10))

# btn4 = tk.Button(frame1, text='Record', height=90, width=200, fg='orange', command=record, image=btn4_image, compound='left')
# btn4['font'] = btn_font
# btn4.grid(row=6, pady=(20,10), ) #column=3


# btn6 = tk.Button(frame1, text='In Out', height=90, width=200, fg='green', command=in_out, image=btn6_image, compound='left')
# btn6['font'] = btn_font
# btn6.grid(row=6, pady=(20,5), ) #column=2

btn5 = tk.Button(frame1, height=90, width=200, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20,10), column=2)

btn7 = tk.Button(frame1, text='AccessControl', height=90, width=220, fg='Green', compound='left', image=btn7_image)
btn_font = ('Arial', 18)
btn7['font'] = btn_font
btn7.grid(row=3, pady=(20,10), column=3, padx=(20,5))

btn8 = tk.Button(frame1, text='Add-Video', height=90, width=210, fg='Green', command=emp_video,compound='left', image=btn8_image)
btn8['font'] = btn_font
btn8.grid(row=4, pady=(20,10), column=3, padx=(20,5))

btn9 = tk.Button(frame1, text='Re-Train Model', height=90, width=210, fg='Green',compound='left', image=btn9_image)
btn9['font'] = btn_font
btn9.grid(row=5, pady=(20,10), column=3, padx=(20,5)) 

btn10 = tk.Button(frame1, text='Instructions', height=90, width=210, fg='orange', command=display_instructions, compound='left', image=btn10_image)
btn10['font'] = btn_font
btn10.grid(row=5, pady=(20,10),  padx=(20,5)) #column=3,

frame1.pack()
window.mainloop()
