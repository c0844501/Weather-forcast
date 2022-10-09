import tkinter as tk
import requests, json
import time
kjgjg
#Student Name: Sonu Yadav
#Studen ID: c0844501
global city_name_string

win = tk.Tk()
win.title('WeatherApp')
win['background']='#14c97b'

number1 = tk.StringVar()
api_key = "a726802eb010be83da49130a6e7519c8"  #API Key
base_url = "http://api.openweathermap.org/data/2.5/weather?" #URL for weather application
 
label=tk.Label(win, text="City name :") #Use of tkinter for creating the labels
label.pack()
entry1 = tk.Entry(win,textvariable=number1, width= 40) #user input
city_name_string = number1
entry1.focus_set() #Setting the focus
entry1.pack()

#mehtod for finding the weather details
#backend details
def find(event):
    city_name = city_name_string.get()
    print(city_name)
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)\

    x = response.json()

    print(x)
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
    
        celsius = current_temperature-273.15
        
        celsius_format = "{:.2f}".format(celsius)
    
    
        current_pressure = y["pressure"]

        current_humidity = y["humidity"]
 
  
        current_wind = x["wind"]
    
        sys = x["sys"]
    
        country = sys["country"]
    
        z = x["weather"]
 
 
        weather_description = z[0]["description"]
 
 #Creating the empty labels   
        label1=tk.Label( text="", font=("Helvetica 22"))
        label1.pack()
      
        label2=tk.Label(win, text="", font=("Helvetica 22"))
        label2.pack()

        label3=tk.Label(win, text="", font=("Helvetica 22 "))
        label3.pack()

        label4=tk.Label(win, text="", font=("Helvetica 22 "))
        label4.pack()

        label5=tk.Label(win, text="", font=("Helvetica 22 "))
        label5.pack()

        label6=tk.Label(win, text="", font=("Helvetica 22 "))
        label6.pack()

        label7=tk.Label(win, text="", font=("Helvetica 22 "))
        label7.pack()

#Display the weather details to the labels
        label1.configure(text="City name : " + city_name)  
        label2.configure(text="Celsius Temperature : " + celsius_format +u"\N{DEGREE SIGN}"+"C")
        label3.configure(text="Country : " + country)
        label4.configure(text="Pressure : " + str(current_pressure))
        label5.configure(text="Humidity : " + str(current_humidity))
        label6.configure(text="Wind : " + str(current_wind))
        label7.configure(text="Weather Description : " + weather_description)
    else:
        label8=tk.Label(win, text="", font=("Helvetica 22 "))
        label8.pack()
        label8.configure(text="City Not Found")
        print("City is Not Found ")
    
button = tk.Button(win, text="Weather", command=lambda: find(city_name_string))
button.pack()  
win.after(180000, lambda: find(city_name_string))
def countdown(t,city_name_string):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    find(city_name_string)
    
#Method for resetting the values after 30 mins
def timerFor30Mins():
    times = 180000

    while times > -1:
        minute,second = (times // 60 , times % 60)
        seconds.set(second)
        minutes.set(minute)
        #Display the Updated values again
        win.update()
        time.sleep(1)
        if(times == 0):
            seconds.set('00')
            minutes.set('00')
            find(city_name_string)
        times -= 1 
    timerFor30Mins()

minutes= tk.StringVar()
minutes.set('00')
mins=tk.Entry(win, textvariable = minutes, width =2, font=(22))
mins.pack()
seconds =tk.StringVar()
seconds.set('00')
sec = tk.Entry(win, textvariable = seconds, width = 2, font=(22))
sec.pack()
timerFor30Mins()

win.mainloop()
