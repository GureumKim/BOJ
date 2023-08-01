def isLeaf(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    return 0

Month_d = {
    'January' : 1,
    'February' : 2,
    'March' : 3,
    'April' : 4,
    'May' : 5,
    'June' : 6,
    'July' : 7,
    'August' : 8,
    'September' : 9,
    'October' : 10,
    'November' : 11,
    'December' : 12
}
Month_l = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

M, D, Y, T = input().split()

if isLeaf(int(Y)): 
    total = 527040 #366*24*60
    Month_l[2] = 29
else: total = 525600 #365일 기준
Sum_M = 0
for i in range(Month_d[M]):
    Sum_M += Month_l[i]
Sum_M *= 1440
D = (int(D[:-1])-1)*1440
H, m = map(int,T.split(':'))
H = H*60

Sum = m + D+ H + Sum_M
print(Sum/total*100)