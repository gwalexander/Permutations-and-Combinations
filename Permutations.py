def factorial(number):
    answer = number
    for counter in range(1, number):
        answer = answer*(number-counter)

    return answer



print("THIS IS FOR PERMUATTIONS")
numberOfPeople = int(input("please Input The N Value:"))
numberOfPrizes = int(input("please Input The R Value:"))


numberOfPeopleFactorial = factorial(numberOfPeople)

differenceFacorial = factorial((numberOfPeople-numberOfPrizes))


formula = int(numberOfPeopleFactorial)/int(differenceFacorial)

print(formula)
