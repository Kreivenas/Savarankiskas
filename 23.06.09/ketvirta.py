import tkinter as tk

def farenheit_to_celsius():
    temperature = float(entry.get())
    celsius = (temperature - 32) * 5/9
    result_label.config(text=f"Celsijais: {celsius:.2f}")

def celsius_to_farenheit():
    temperature = float(entry.get())
    farenheit = (temperature * 9/5) + 32
    result_label.config(text=f"Farenheitas: {farenheit:.2f}")

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

farenheit_button = tk.Button(window, text="Farenheit -> Celsijus", command=farenheit_to_celsius)
farenheit_button.pack()

celsius_button = tk.Button(window, text="Celsijus -> Farenheit", command=celsius_to_farenheit)
celsius_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
