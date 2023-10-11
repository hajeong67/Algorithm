import sys

N=int(sys.stdin.readline())

stack=[]
result=1

for _ in range(N):
    stack.append(int(sys.stdin.readline()))
Max =stack[-1]

for i in range(len(stack)-1,-1,-1):
    if stack[i]>Max:
        result+=1
        Max=stack[i]

print(result)