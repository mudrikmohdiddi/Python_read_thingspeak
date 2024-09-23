from requests import *
from tkinter import *
from tkinter.ttk import *
from time import *
try:
    r="https://api.thingspeak.com/channels/2653317/feeds.json?api_key=YHEJKMD4TPE7L5DL&results=1"
    
    channel_id = '2634942'
    read_api_key = 'XZD8794U78ZGFSY6'
        
    url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=1'
    room=Tk()
    room.title("MUDRIK MOHD IDDI")
    def my_saa():
        rr=get(r)
        led=rr.json()
        l = led['feeds'][0]['field1']
        if(str(l).startswith('10')):
            on='ON'
        elif(str(l).startswith('20')):
            on='OFF'
        else:
            on='ERROR'
        response = get(url)
        data = response.json()
        t = data['feeds'][0]['field2']
        h = data['feeds'][0]['field3']
        u = data['feeds'][0]['field4']
        saa.config(text=strftime(f"""
                                   SENSOR VALUE
       TEMPERATURE                                  HUMIDITY
       {t}°C                                      {h}percentage
       
       
       ULTRASONIC                           LED: {on}
       {u}cm
    
      %I:%M: %p  %A %d-%B-20%y
      BY  MUDRIK MOHD IDDI

    """))
        saa.after(4000,my_saa)
    saa=Label(room,font=("Digital",20),background=("blue"),foreground=("black"))
    saa.pack(anchor=("center"))
    def led_on():
        ur1="https://api.thingspeak.com/update?api_key=C43DPG0T68I3T287&field1=10"
        get(ur1)
    def led_off():
        ur2="https://api.thingspeak.com/update?api_key=C43DPG0T68I3T287&field1=20"
        get(ur2)
    on_button = Button(text='''

    \n\t\tON swith\t\t\n

    ''', command=led_on)
    on_button.pack(anchor='center')

    off_button = Button(text='''

    \n\t\tOFF swith\t\t\n

    ''', command=led_off)
    off_button.pack(anchor='center')
    
    my_saa()
    mainloop()
except ConnectionError:
    print("Please connect network")
    p=input("open again")
