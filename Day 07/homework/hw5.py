# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.

n = int(input(" Enter your number: "))
n1 = 0
n2 = 1

while n2 <= n:
    n1 += n2
    n2 += 1

print(n1)