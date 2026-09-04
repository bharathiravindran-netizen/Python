class multipleFunctions():
    def oddeven():
        num=int(input("Enter the number"))
        if((num%2)==0):
            print("Even number")
            message="even number"
        else:
            print("Odd number")
            message="odd number"
        return message
    def BMI():
        BMI= int(input("Enter the BMI Index:"))
        if(BMI<18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight")
            message="Very Overweight"
        return message