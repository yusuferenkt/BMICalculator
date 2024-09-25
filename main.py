import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=200)

#kg label
kg_label=tkinter.Label(text="Enter Your Weight (kg)")
kg_label.pack()

#kg entry
kg_entry=tkinter.Entry()
kg_entry.pack()

#cm label
cm_label=tkinter.Label(text="Enter Your Height (cm)")
cm_label.pack()

#cm entry
cm_entry=tkinter.Entry()
cm_entry.pack()

#button label
btn_label=tkinter.Label()
btn_label.pack()

def calculate():
    my_kg=int(kg_entry.get())
    my_cm=int(cm_entry.get())
    BMI=(my_kg)/((my_cm/100)*(my_cm/100))
    if BMI < 18:
        btn_label.config(text="Underweight")
    if BMI > 18 and BMI <24:
        btn_label.config(text="Normal Weight")
    if BMI >25 and BMI <29:
        btn_label.config(text="Overweight")
    if BMI >30 and BMI <34:
        btn_label.config(text="Obesity Class I")
    if BMI >35 and BMI <39:
        btn_label.config(text="Obesity Class II")
    if BMI >40:
        btn_label.config(text="Obesity Class III")

#button
clc_button=tkinter.Button(text="Calculate",command=calculate)
clc_button.pack()



window.mainloop()