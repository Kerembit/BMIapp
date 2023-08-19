from tkinter import *


window = Tk()
window.configure(bg="blue")
window.minsize(width=600, height=400)
window.title("BMI Calculator")
window.update()
window_height = window.winfo_height()
window_width = window.winfo_width()

calculation_result = "Enter valid numbers and push calculate"


def bmi_calculator():
    input_weight = weight_entry.get()
    input_height = height_entry.get()
    if input_height == "" or input_weight == "":
        return_label.config(text="Don't leave the line blank")
    else:
        try:
            input_weight = int(weight_entry.get())
            input_height = int(height_entry.get())
            bmi = input_weight / (input_height / 100) ** 2
            return_label.config(text="You are healthy.")
            if bmi <= 18.5:
                return_label.config(text="You are thin.")
            else:
                if 18.5 < bmi <= 24.9:
                    return_label.config(text="You are healthy.")
                else:
                    if 24.9 < bmi <= 29.9:
                        return_label.config(text="You are over-weight.")
                    else:
                        if 29.9 < bmi:
                            return_label.config(text="You are obese.")
                        else:
                            return_label.config(text="Enter valid characters")
        except:
            return_label.config(text="Enter a valid number.")


weight_label = Label(text="Enter your weight below!")
weight_label.update()
weight_label.place(x=window_width/4 - 50, y=window_height/4)


height_label = Label(text="Enter your height below!")
height_label.update()
height_label.place(x=window_width * 3/4 - 50, y=window_height/4)


weight_entry = Entry()
weight_entry.place(x=window_width/4 - 50, y=window_height/4+20)
weight_entry.insert(0, "kg")


height_entry = Entry()
height_entry.place(x=window_width * 3/4 - 50, y=window_height/4+20)
height_entry.insert(0, "cm")


calculate_button = Button(text="Calculate", command=bmi_calculator)
calculate_button.place(x=window_width/2, y=window_height * 3/4)

return_label = Label(text=calculation_result)
return_label.place(x=window_width/2, y=window_height * 3/4+40)
return_label.update()

window.mainloop()
