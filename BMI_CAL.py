height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))   
BMI = weight / (height/100)**2  
print("Your Body Mass Index is", BMI)  
if BMI <= 18.5:  
    print("You are underweight.")  
elif BMI <= 24.9:  
    print("You are healthy.")  
elif BMI <= 29.9:  
    print(" You are over weight.")  
else:  
    print("You are obese.")
