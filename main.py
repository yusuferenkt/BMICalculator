import tkinter

bmi_window=tkinter.Tk()
bmi_window.title("BMI Calculator")
bmi_window.config(padx=30,pady=30)
bmi_window.minsize(width=300,height=200)

#kg label
kg_label=tkinter.Label(text="Enter Your Weight (kg)")
kg_label.pack()

#kg entry
kg_entry=tkinter.Entry(width=20)
kg_entry.pack()

#cm label
cm_label=tkinter.Label(text="Enter Your Height (cm)")
cm_label.pack()

#cm entry
cm_entry=tkinter.Entry(width=20)
cm_entry.pack()

#button label
btn_label=tkinter.Label()
btn_label.pack()

def calculate():
    my_kg=kg_entry.get()
    my_cm=cm_entry.get()

    if my_kg=="" or my_cm=="":
        btn_label.config(text="Enter both weight and height.")
    else:
        try:
            BMI=float(my_kg) / (float(my_cm) / 100)**2
            if BMI <= 16:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are severely thin.")
            elif 16 < BMI <= 17:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are moderately thin.")
            elif 17 < BMI <= 18.5:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are mild thin.")
            elif 18.5 < BMI <= 25:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are normal.")
            elif 25 < BMI <= 30:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are overweight.")
            elif 30 < BMI <= 35:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are obese class I.")
            elif 35 < BMI <= 40:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are obese class II.")
            elif BMI > 40:
                btn_label.config(text=f"Your BMI is : {round(BMI,2)}. You are obese class III.")
        except:
            btn_label.config(text="Enter a valid number.")

#button
clc_button=tkinter.Button(text="Calculate",command=calculate)
clc_button.pack()



bmi_window.mainloop()