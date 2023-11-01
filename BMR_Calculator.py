#Import packages needed
import tkinter as tk

# Calculate the BMR and set value to BMR
def calculateBMR():
    #get enterd values
    weight = float(weightValue.get())* 0.45359237 
    height = float(heightValue.get()) * 30.48
    age = float(ageValue.get())
    #calculate BMR
    BMR = round(88.362 + ((13.397)* weight) + ((4.799) * height) - ((5.677)* age),)
    #Set BMR Value to BMR
    BMR_value.set(BMR)

#main window
root = tk.Tk()
root.title('Stock Price Calculator')

#label to prompt the user to enter weight value
weight_Label = tk.Label(root, text = "Enter Weight in Lb:")
weight_Label.grid(row = 0, column = 0)

#new varibale for weight value
weightValue = tk.StringVar()

#entry to retrive the users input 
weight_entry = tk.Entry(root, width=25, textvariable= weightValue)
weight_entry.grid(row=0, column=1)

#label to prompt user for height in ft
height_Label = tk.Label(root, text = "Enter Height in Ft:")
height_Label.grid(row = 1, column = 0)

#new varibale for height value
heightValue = tk.StringVar()

#entry to retrive the users input for height 
height_entry = tk.Entry(root, width=25, textvariable= heightValue)
height_entry.grid(row=1, column=1)

#label to prompt user for age
age_Label = tk.Label(root, text = "Enter Age in Years:")
age_Label.grid(row = 2, column = 0)

#new varibale for age value
ageValue = tk.StringVar()

#entry to retrive the users input for age
age_entry = tk.Entry(root, width=25, textvariable= ageValue)
age_entry.grid(row=2, column=1)

#label to pdisplay BMR
BMR_Label = tk.Label(root, text = "Your BMR is:")
BMR_Label.grid(row = 3, column = 0)

#valiable to hold BMR value
BMR_value = tk.StringVar()

#entry to retrive the users input for age
BMR_entry = tk.Entry(root, width=25, state= "readonly", textvariable = BMR_value)
BMR_entry.grid(row=3, column=1)

#Buttom for calculation
calculation_Button = tk.Button(root, text = 'Calculate', command = calculateBMR)
calculation_Button.grid(row = 4, column = 0)

#Exit Button 
exit_Button = tk.Button(root, text = 'Exit', command = root.destroy)
exit_Button.grid(row = 4, column = 1)

#format the components 
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
