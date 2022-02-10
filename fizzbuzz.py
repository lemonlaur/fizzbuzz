# FIZZ BUZZ
# lauren cook
# feb 3 2022

# print numbers 1-100 replacing numbers divided by 3 with fizz, numbers divided by 5 with buzz, and numbers divided by both with fizzbuzz
for num in range(1,101):
    if num % 3 == 0 and num % 5 ==0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)