n=int(input())
a=list(map(int, input().split()))

for i in range(n - 1):
    num = a[i] * a[i+1]
    print(num, end=' ')

# 実装例
n=int(input())
a=list(map(int, input().split()))

b=[]
for i in range(n-1):
    b.append(a[i]*a[i+1])
print(*b)