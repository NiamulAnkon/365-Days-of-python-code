from tkinter import *
import speedtest as st


def speed_test():
  sp = st.Speedtest()
  sp.get_servers()
  download = str(round(sp.download() / (10**6), 3)) + "Mbps"
  upload = str(round(sp.upload() / (10**6), 3)) + "Mbps"
  lab_down.config(text=download)
  lab_up.config(text=upload)


sp = Tk()
sp.title("internet speed test")
sp.geometry("500x700")
sp.config(bg="White")
lab = Label(sp,
            text="internet speed test",
            font=("Time new Roman", 25, "bold"),
            fg="Black",
            bg="White")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Downloading speed", font=("Time new Roman", 25, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Time new Roman", 25, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Uploading speed", font=("Time new Roman", 25, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Time new Roman", 25, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

button = Button(sp,
                text="CHECK SPEED",
                font=("Time new Roman", 30, "bold"),
                relief=RAISED,
                command=speed_test)
button.place(x=60, y=360, height=50, width=380)

sp.mainloop()
