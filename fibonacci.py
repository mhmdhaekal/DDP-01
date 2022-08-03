
while True:
    def fibonacci(n):
        sequence=[]
        if n==1:
            sequence=[0]
        else:
            sequence=[0,1]
        for i in range (1, n-1):
            sequence.append(sequence[i-1] +sequence[i])
        return sequence
    a=int(input())
    print(fibonacci(a))
    
    