import tkinter as tk
def add():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        result=num1+num2
        display_result(result)
    except ValueError:
        display_result("Invalid input!")
def subract():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        result=num1-num2
        display_result(result)
    except ValueError:
        display_result("Invalid input!")
def multiply():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        result=num1*num2
        display_result(result)
    except ValueError:
        display_result("Invalid input!")
def divide():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        result=num1/num2
        display_result(result)
    except ValueError:
        display_result("Invalid input!")
def display_result(result):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    result_label.config(text="Result:"+ str(result))
window=tk.Tk()
window.title("Calculator")
entry1=tk.Entry(window)
entry1.grid(row=0, column=0, padx=5, pady=5)
entry2=tk.Entry(window)
entry2.grid(row=0, column=1, padx=5, pady=5)
add_button=tk.Button(window, text="+", command=add)
add_button.grid(row=1, column=0, pady=5)
subract_button=tk.Button(window, text="-", command=subract)
subract_button.grid(row=1, column=1, pady=5)
multiply_button=tk.Button(window, text="*", command=multiply)
multiply_button.grid(row=2, column=0, pady=5)
divide_button=tk.Button(window, text="/", command=divide)
divide_button.grid(row=2, column=1, pady=5)
result_label=tk.Label(window, text="Result:")
result_label.grid(row=3, column=0, columnspan=2)
window.mainloop()









