import tkinter as tk
import join
# dfs = str(join.join())

headerfont = ('Avenir', 24)
font = ('Avenir', 14)


def test_function():
    file_path_1_text = file_path_1.get()
    file_path_2_text = file_path_2.get()
    column_1_text = file_path_3.get()
    column_2_text = file_path_4.get()
    output_text = file_path_5.get()
    join.join(file_path_1_text, file_path_2_text, column_1_text, column_2_text, output_text)


root = tk.Tk()
root.geometry("500x500")
root.title("mergify")

title = tk.Label(root, text="Mergify", font=headerfont)
title.pack(padx=20, pady=20)
description = tk.Label(root, text="Please select two csv files, columns\nto join on, and output file name", font=headerfont)
description.pack(padx=10, pady=10)

input_frame = tk.Frame(root)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

label_1 = tk.Label(input_frame, text="First file path:", font=font)
label_1.grid(row=0, column=0)
file_path_1 = tk.Entry(input_frame, font=font)
file_path_1.grid(row=0, column=1)

label_2 = tk.Label(input_frame, text="Second file path:", font=font)
label_2.grid(row=1, column=0)
file_path_2 = tk.Entry(input_frame, font=font)
file_path_2.grid(row=1, column=1)

label_3 = tk.Label(input_frame, text="Column from first file:", font=font)
label_3.grid(row=2, column=0)
file_path_3 = tk.Entry(input_frame, font=font)
file_path_3.grid(row=2, column=1)

label_4 = tk.Label(input_frame, text="Column from second file:", font=font)
label_4.grid(row=3, column=0)
file_path_4 = tk.Entry(input_frame, font=font)
file_path_4.grid(row=3, column=1)

label_5 = tk.Label(input_frame, text="Output file path:", font=font)
label_5.grid(row=4, column=0)
file_path_5 = tk.Entry(input_frame, font=font)
file_path_5.grid(row=4, column=1)

input_frame.pack()

mergify_button = tk.Button(
    root,
    text="Mergify!",
    #  TODO
    bg='green',
    font=headerfont,
    command=test_function
)
mergify_button.pack(padx=100,pady=30)

# textbox = tk.Text(root, height=3, font=font)
# textbox.pack(padx=20, pady=10)
#
# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)
#
#
# btn1 = tk.Button(buttonframe, text="1", font=font)
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
# btn2 = tk.Button(buttonframe, text="2", font=font)
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
# btn3 = tk.Button(buttonframe, text="3", font=font)
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
# btn4 = tk.Button(buttonframe, text="4", font=font)
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
# btn5 = tk.Button(buttonframe, text="5", font=font)
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
# btn6 = tk.Button(buttonframe, text="6", font=font)
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
#
# buttonframe.pack(fill='x')

# anotherbtn = tk.Button(root, text="TEST", font=font)
# anotherbtn.place(x=200, y=200, height=100, width=100)

root.mainloop()
