x = float(input("What x to find the square root of? "))
g = float(input("What guess to start with? "))

# 1. Print the current estimate square
print("Current estimate square:", g**2)

# 2. Calculate the next guess using Newton's formula:
# next_guess = g - f(g)/f'(g)
# where f(g) = g^2 - x  and  f'(g) = 2*g
f_g = g**2 - x
f_prime = 2 * g

next_guess = g - (f_g / f_prime)

# 3. Print the next guess
print("Next guess:", next_guess)