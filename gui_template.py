from datetime import datetime
import tkinter as tk
import pyttsx3

def tell_time():
    #获取当前时间
    now = datetime.now()
    time_str = f"现在时间是{now.hour}点{now.minute}分{now.second}秒"

    #打印到屏幕
    print(f"🕒{time_str}")

    #语音播报
    engine = pyttsx3.init()
    engine.say(time_str)
    engine.runAndWait()

root = tk.Tk()
root.title("timer")
root.geometry("500x500")

time_button = tk.Button(
    root,
    text="报时",
    command=tell_time,
)
time_button.pack(pady=100)


root.mainloop()
