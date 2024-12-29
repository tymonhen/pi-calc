import mpmath

mpmath.mp.dps = 200  

num = int(input("Pick a number: "))

def summation(k):
    return (-1)**k * mpmath.factorial(6*k) * (545140134*k + 13591409) / (mpmath.factorial(3*k) * mpmath.factorial(k)**3 * (640320)**((3*k + 3) / 2))

pi_appr = mpmath.mpf(0)

for i in range(num):
    pi_appr += summation(i)

pi_appr *= 12
pi_appr = 1 / pi_appr

print(pi_appr)
