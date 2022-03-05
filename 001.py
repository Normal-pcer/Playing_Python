average=0
ans=0
n,m=eval(input())
a = [0]*m
b = 0
end = [(0,0)]*n
for i in range(n):
    j = 0
    while j<m:
        a[j],b = eval(input())
        for k in range(b):
            a[j+k] = a[j]
            average = average+a[j]
        j = j+b
    average = round(average/m, 3)
    for j in range(m):
        ans = ans + pow(a[j]-average, 2)
    ans = round(ans/m, 3)
    end[i] = eval('('+str(average)+','+str(ans)+')')
    print('-'*20)
for i in range(n):
    print(end[i])
