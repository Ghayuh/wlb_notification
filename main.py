import datetime
import PySimpleGUI as sg
from datetime import datetime
from winotify import Notification, audio

def notification(start_hour=None, start_minute=None):
    toast = Notification(app_id="WLB Notification",
                     title="Notifications",
                     msg="Hi, it's 5 minute time to go home!",
                     duration="long")

    toast.set_audio(audio.Reminder, loop=False)
    toast.add_actions(label="OK")

    while True:
        if start_hour+9 == datetime.now().hour and start_minute-5 == datetime.now().minute:
            toast.show()

def popup_get_time(start_hour=None, start_minute=None):
    option = {
        "font": ("digital-7", 36, "bold"),
        "enable_events": True,
        "background_color": None,
        "text_color": "white",
        "justification": "center",
        "pad": (0, 0)
    }
    now = datetime.now()
    hour, minute = now.hour, now.minute
    hour = hour if start_hour is None else max(0, min(int(start_hour), 23))
    minute = minute if start_minute is None else max(0, min(int(start_minute), 59))
    layout = [
        [sg.Text(f"{hour:0>2d}", **option, size=(3, 1), key="Hour"),
         sg.Text(":",  **option),
         sg.Text(f"{minute:0>2d}", **option, size=(3, 1), key="Minute")],
        [sg.Button("OK"), sg.Button("Cancel")]
    ]
    window = sg.Window("Select Time", layout, grab_anywhere=True,
        keep_on_top=True, modal=True, finalize=True)
    hour_element, minute_element = window['Hour'], window['Minute']
    hour_element.bind("<MouseWheel>", "_Wheel")
    minute_element.bind("<MouseWheel>", "_Wheel")

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            window.close()
            # return (None, None)
            return
        elif event == "OK":
            window.close()
            return (hour,minute)
        elif event == "Hour_Wheel":
            delta = -int(hour_element.user_bind_event.delta/120)
            hour = (hour+delta) % 24
            hour_element.update(f'{hour:0>2d}')
        elif event == "Minute_Wheel":
            delta = -int(minute_element.user_bind_event.delta/120)
            minute = (minute+delta) % 60
            minute_element.update(f'{minute:0>2d}')

sg.theme("DarkBlue")

layout = [
    [sg.Button('SET-TIME')],
]
window = sg.Window('Title', layout,auto_size_buttons=False,finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'SET-TIME':
        hour, minute = popup_get_time(5, 20)
        print(f'You set time as {hour:0>2d}:{minute:0>2d}')
        notification(hour, minute)
        window.close()