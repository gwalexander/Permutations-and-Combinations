def factorial(number):
    answer = number
    for counter in range(1, number):
        answer = answer*(number-counter)

    return answer


print("THIS IS FOR COMBINATIONS")
n = int(input("please Input The N Value:"))
r = int(input("please Input The R Value:"))


nFactorial = factorial(n)
rFactorial = factorial(r)
differenceFacorial = factorial((n-r))

result = int(nFactorial)/(int(rFactorial)*int(differenceFacorial))

print(result)

