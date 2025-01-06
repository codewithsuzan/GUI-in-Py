import tkinter as tk
root=tk.Tk()

def greet():
    label.config(text="Hello, Welcome to tkinter")

root.title("Interactive GUI")
# Create a Label widget
label=tk.Label(root,text="Click the button to get greeted")
font=("arial",14)
label.pack(pady=20)

# add a button
button=tk.Button(root,text="Greet me",command=greet)
button.pack(pady=10)
root.geometry("400x400")
root.mainloop()