import tkinter as tk

def click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

Cal = tk.Tk()
Cal.geometry("300x400")
Cal.title("Calculator")

entry = tk.Entry(Cal, font=("Times New Roman", 20))
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(Cal)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row_index = 1
col_index = 0
for text in buttons:
    button = tk.Button(button_frame, text=text, font=("Times New Roman", 18),
                       relief="ridge", borderwidth=3)
    button.grid(row=row_index, column=col_index, padx=5, pady=5)
    button.bind("<Button-1>", click)

    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

Cal.mainloop()
