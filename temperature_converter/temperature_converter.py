import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry.get())
        scale = scale_var.get()

        if scale == "Celsius":
            c = temp
            f = (c * 9/5) + 32
            k = c + 273.15
        elif scale == "Fahrenheit":
            f = temp
            c = (f - 32) * 5/9
            k = (f - 32) * 5/9 + 273.15
        elif scale == "Kelvin":
            k = temp
            c = k - 273.15
            f = (k - 273.15) * 9/5 + 32
        else:
            messagebox.showerror("Error", "Please select a valid scale")
            return

        result_label.config(
            text=f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")


tk.Label(root, text="🌡 Temperature Converter 🌡", font=("Arial", 14)).pack(pady=10)


tk.Label(root, text="Enter Temperature:").pack()
entry = tk.Entry(root)
entry.pack(pady=5)


tk.Label(root, text="Select Input Scale:").pack()
scale_var = tk.StringVar(value="Celsius")
tk.Radiobutton(root, text="Celsius", variable=scale_var, value="Celsius").pack()
tk.Radiobutton(root, text="Fahrenheit", variable=scale_var, value="Fahrenheit").pack()
tk.Radiobutton(root, text="Kelvin", variable=scale_var, value="Kelvin").pack()


tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)


root.mainloop()
