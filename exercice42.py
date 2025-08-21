N = int (input("Veuillez saisir la valeur de N : ") )
M = N
Inverse = 0
while N != 0 :
    Inverse = (Inverse * 10) + (N % 10)
    N = N // 10
if M == Inverse :
    print(N,"est un nombre palindrome")
else :
    print(N, "est un nombre non palindrome")