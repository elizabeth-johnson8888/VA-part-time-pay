# Created By: Elizabeth Johnson
# Date: 3/4/2025

'''
Calculates how much money someone will earn in two weeks in Virginia based on
their hourly wage(s) and how many hours they worked part time. Assuming you are not withholding any taxes.
'''


'''
Gets the user's wages and hours and returns a final salary
'''
def wageAndHourAmount():
    print("Do you have multiple hourly wages over this two week period? Enter Y or N\n\tFor example: Someone might get paid $15 an hour one shift and $17 for another shift.")
    numberOfWages = 0
    while (True):
        multipleWages = input()
        print()

        '''
        Determine whether the user has multiple pay rates, and how many in their paycheck.
        '''
        if (multipleWages.upper().strip(" ") == "Y"):
            print("How many different pay rates do you earn? Enter a number.")
            while (True):
                numberOfWages = input().strip(" ")
                print()

                try:
                    numberOfWages = int(numberOfWages)
                    break
                except:
                    print("The number you entered was invalid. How many different pay rates do you earn?")
            break
        elif (multipleWages.upper().strip(" ") == "N"):
            numberOfWages = 1
            break
        else:
            print("Answer was invalid. Please write Y or N.")



    '''
    Determine what the pay rates are for and how much the user is paid hourly for each and add it to list payRates
    '''
    payRates = []
    for i in range(1, numberOfWages + 1, 1):
        print(f"Pay Rate {i}:")

        print("What is the job title for this pay rate?")
        jobTitle = input()

        print(f"\nWhat is the pay rate of {jobTitle} hourly? Write a number.")
        while (True):
            payRate = input().strip(" ")
            print()

            try:
                payRate = float(payRate)
                break
            except:
                print(f"The number you entered was invalid. What is the pay rate of {jobTitle} hourly?")

        print("How many hours did you do this job in your current pay period?")
        while (True):
            hours = input().strip(" ")
            print()

            try:
                hours = float(hours)
                payRates.append((jobTitle, payRate, hours))
                break
            except:
                print(f"The number you entered was invalid. How many hours of {jobTitle} did you work?")

    '''
    Determine how much money is owed to the user without taxes
    '''
    salary = 0
    for job in payRates:
        salary = salary + float(job[1] * job[2])

    return salary



print("\nWelcome to your paycheck calculator!\n")
print("To determine how much your employer owes you, I need to know a few things first.\n")
print("Do you already know how much you are getting paid this paycheck? Write Y or N")

salary = 0
while (True):
    knowSalary = input()
    print()

    if (knowSalary.upper().strip(" ") == "Y"):
        '''
        If the user already knows how much they will be getting paid without taxes, they enter the amount and the 
        payment after taxes will show
        '''
        print("How much are you getting paid this period without taxes? Enter a number")
        while (True):
            salary = input().strip(" ")
            print()

            try:
                salary = float(salary)
                break
            except:
                print(f"The number you entered was invalid. What is your salary without taxes?")
        break
    elif (knowSalary.upper().strip(" ") == "N"):
        '''
        If the person does not know how much they will get paid in a pay period, the caculator asks how much the user
        gets paid for each wage and calculates the final salary
        '''
        salary = wageAndHourAmount()
        break
    else:
        print("You did not write a valid answer. Write Y or N")

'''
Figure out Virginia Income Tax Bracket
'''
print("We must know your Virginia tax bracket to figure out how much Virginia income taxes you will pay.")
print("A. $0 - $3,000")
print("B. $3,001 - $5,000")
print("C. $5,001 - $17,000")
print("D. $17,000+")
print("Write A, B, C or D")

virginiaIncomeTax = 0
while (True):
    taxBracket = input().upper().strip(" ")
    print()
    match taxBracket:
        case "A":
            virginiaIncomeTax = salary * 0.02
            break
        case "B":
            virginiaIncomeTax = salary * 0.03 + 60
            break
        case "C":
            virginiaIncomeTax = salary * 0.05 + 120
            break
        case "D":
            virginiaIncomeTax = salary * 0.0575 + 730
            break
        case _:
            print("Your answer was invalid. Please write A, B, C or D")




'''
Calculate the taxes
'''
medicareTax = salary * 0.0145
socialSecurityTax = salary * 0.062

netSalary = salary - virginiaIncomeTax - medicareTax - socialSecurityTax
print(f"Your net salary will be ${netSalary:.2f}")
