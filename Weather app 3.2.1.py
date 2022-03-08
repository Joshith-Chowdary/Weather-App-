import tkinter as tk
import requests
import time


def show_frame(frame):
    frame.tkraise()
    
root = tk.Tk()

root.iconbitmap('Icon@weather3.2.2.png')
root.mainloop()
    
window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window)

for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0,column=0,sticky='nsew')
    
#==================home code
frame1_title=  tk.Label(frame1, text='Weather App 3.2.1', font='times 35', bg='blue')
frame1_title.pack(fill='both', expand=True)
frame1_title=  tk.Label(frame1, text='By Joshith', font='times 20',bg='blue')
frame1_title.pack(fill='both', expand=True)

frame1_btn = tk.Button(frame1, text='Current weather',command=lambda:show_frame(frame2))
frame1_btn.pack(fill='x', ipady=15)

frame1_btn = tk.Button(frame1, text='Future weather',command=lambda:show_frame(frame3))
frame1_btn.pack(fill='x', ipady=15)

frame1_btn = tk.Button(frame1, text='Past weather',command=lambda:show_frame(frame4))
frame1_btn.pack(fill='x', ipady=15)

#==================current weather code
def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(frame2, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(frame2, font=t)
label1.pack()
label2 = tk.Label(frame2, font=f)
label2.pack()

frame2_title=  tk.Label(frame2, text='Current Weather',font='times 35')
frame2_title.pack(fill='both', expand=True)



frame2_btn = tk.Button(frame2, text='Home',command=lambda:show_frame(frame1))
frame2_btn.pack(fill='x', ipady=15)

#==================future code
frame3_title=  tk.Label(frame3, text='Code Not Found',font='times 35', bg='yellow')
frame3_title.pack(fill='both', expand=True)

frame3_btn = tk.Button(frame3, text='Home',command=lambda:show_frame(frame1))
frame3_btn.pack(fill='x',ipady=15)





#=================Past weather code
frame4_title=  tk.Label(frame4, text='Code Not Found',font='times 35', bg='yellow')
frame4_title.pack(fill='both', expand=True)

frame4_btn = tk.Button(frame4, text='Home',command=lambda:show_frame(frame1))
frame4_btn.pack(fill='x',ipady=15)

show_frame(frame1)

window.mainloop()

print("Job Done | Thanks for using | Code Made by Joshith | DO NOT COPY! ")