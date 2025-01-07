import tkinter as tk
from tkinter import messagebox as mb

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("Simple Interest Calculator")

# Function to calculate Simple Interest
def find_simple_interest(P_value, T_value, R_value):
    try:
        P = float(P_value.get())
        T = float(T_value.get())
        R = float(R_value.get())
        SI = (P * T * R) / 100
        mb.showinfo("Simple Interest", f"The Simple Interest is: Rs.{SI}")
    except ValueError:
        mb.showerror("Input Error", "Please enter valid numeric values.")

# Header Label
label = tk.Label(root, text="Simple Interest Calculator", font=("Arial", 16))
label.pack(pady=10)

# Input fields
l1 = tk.Label(root, text="Enter Principal (P):")
l1.pack()
P = tk.Entry(root)
P.pack(pady=5)

l2 = tk.Label(root, text="Enter Time (T) in years:")
l2.pack()
T = tk.Entry(root)
T.pack(pady=5)

l3 = tk.Label(root, text="Enter Rate of Interest (R):")
l3.pack()
R = tk.Entry(root)
R.pack(pady=5)

# Button to calculate Simple Interest
btn = tk.Button(root, text="Find SI", command=lambda: find_simple_interest(P, T, R))
btn.pack(pady=10)

# Run the main loop
root.mainloop()
