def mktemp(a,b,op):
    oper = {
        0 : a + b,
        1: a - b,
        2: a * b,
        3: -(abs(a)//abs(b)) if (a<0 and b>0) or (a>0 and b<0) else a//b
    }
    return oper.get(op)

def do(level,res):
    global mn, mx
    if level == n-1:
        mn,mx = min(mn,res),max(mx,res)
        return
    
    for i in range(4):
        if oper_d[i]:
            oper_d[i]-=1
            temp = mktemp(res,nums[level+1],i)
            # print(res, temp, level)
            # print()
            # do(level+1,res+mktemp(nums[level],nums[level+1],i))
            do(level+1,temp)
            oper_d[i]+=1

    
n = int(input())
nums = list(map(int,input().split()))
oper_d = list(map(int,input().split()))

# 최대, 최솟 값이 이거일 경우 1e9는 float 형이기 때문에 소숫점도 출력된다, 이거 조심!
mn, mx = int(1e9),-int(1e9)
do(0,nums[0])

print(mx,mn,sep='\n')