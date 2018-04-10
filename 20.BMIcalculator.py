import os
import webbrowser

class Body_Mass_Index:
    value = 0
    def additional_informations(self):
        print("\nDo you want to know presice informations about Body Mass Index values ?")
        print('Note: "Yes" will open a website of U.S. Department of Health. If you want to exit, press any button.')
        choice = input()
        if choice.lower() == "yes":
            webbrowser.open('https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm')
        else:
            print("Move up to be healthy and happy :) !")
            exit()

    def calculator(self, height, weight):
        height = int(height)/100
        operation = int(weight) / (height ** 2)
        self.value = operation
        os.system('cls')
        print('This is your BMI: %.2f' % (self.value))

    def interpreter(self):
        if self.value < 18.50:
            print("It means you have underweight !")
            self.additional_informations()
        elif self.value in range(int(18.51), int(24.99)):
            print("Your body mass is fine (fits in the norm). Keep it going :)")
        else:
            print("It means you are overweight or even obese !")
            self.additional_informations()

BMI = Body_Mass_Index()
print('Weight: ')
weight = input()
print('Height: ')
height = input()

if weight.isdigit() and height.isdigit():
    BMI.calculator(height, weight)
    BMI.interpreter()
else:
    print("Wrong values.")