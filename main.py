import time
import datetime
import ctypes
from winotify import Notification, audio

alarmHour   = int(input("Masukan Jam Kedatangan : "))
alarmMin    = int(input("Masukan Menit Kedatangan : "))
alarmAm     = input("am / pm : ")

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

toast = Notification(app_id="WLB Notification",
                     title="Notifications",
                     msg="Hi, it's 5 minute time to go home!",
                     duration="long")

toast.set_audio(audio.Reminder, loop=False)
toast.add_actions(label="OK")

if alarmAm == "pm":
    alarmHour += 12

while True:
    if alarmHour+9 == datetime.datetime.now().hour and alarmMin-5 == datetime.datetime.now().minute:
        toast.show()