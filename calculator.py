import tkinter as tk
import messagebox

root=tk.Tk()
root.geometry("400x400")
root.title("Calculator")

def findSum():
    num1=entry1.get()
    num2=entry2.get()
    
    if num1.isdigit() and num2.isdigit():
        result=int(num1)+int(num2)
        messagebox.showinfo("Result:",f"Sum={result}")
    else:
        messagebox.showerror("Error", "Please enter valid numbers")


label = tk.Label(root, text="Calculator")
label.pack()
#input fields
l1=tk.Label(root, text="Num1:")
l1.pack(pady=5)
entry1=tk.Entry(root)
entry1.pack(pady=5)
l2=tk.Label(root, text="Num2:")
l2.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)

btn=tk.Button(root,text="Add",command=findSum).pack(pady=10)

root.mainloop()