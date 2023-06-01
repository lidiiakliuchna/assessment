def find_grid(user_input):
    fact = 0
    for i in range(1, user_input + 1):
        fact = fact + (i**2)
    print(fact)
user_input=int(input())
find_grid(user_input)