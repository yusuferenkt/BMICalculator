import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)
window.minsize(width=300,height=200)

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
            result_string=write_result(BMI)
            btn_label.config(text=result_string)
        except:
            btn_label.config(text="Enter a valid number.")

def write_result(BMI):
    result_string=f"Your BMI is: {round(BMI,2)}. You are "
    if BMI <=16:
        result_string+="severely thin."
    elif 16 < BMI <= 17:
        result_string+="moderately thin."
    elif 17 < BMI <= 18.5:
        result_string+="mild thin."
    elif 18.5 < BMI <= 25:
        result_string+="normal."
    elif 25 < BMI <= 30:
        result_string+="overweight."
    elif 30 < BMI <= 35:
        result_string+="obese class I"
    elif 35 < BMI <= 40:
        result_string+="obese class II"
    elif BMI > 40:
        result_string+="obese class III"
    return result_string


#button
clc_button=tkinter.Button(text="Calculate",command=calculate)
clc_button.pack()



window.mainloop()