import statistics

count=int(input())
l=map(int,list(input().split()))
med=int(statistics.median(l))
print(med)
