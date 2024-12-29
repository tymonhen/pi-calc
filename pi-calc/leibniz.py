rep = int(input("How many repetitions? (Note: this isn't the same as the number of decimal places, the Leibniz series converges to Pi relatively slowly) : "))

num = 0
for k in range(rep):
    num += (-1) ** (k) * 4 / (2*k + 1)

print(num)