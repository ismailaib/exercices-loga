N = int( input("Donner le nombre N :"))
S = 0
for i in range(1,N):
    K = 0
    for j in range(1,i):
        if i % j == 0:
            K = K + 1 
            print("K = ", K)
    if K <= 2 :
        S = S + i
    print("S = ",S)