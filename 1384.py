n = int(input())
gn = 1
while n != 0:
    names = []
    papers = []
    flag = 1
    for _ in range(n):
        name, *paper = input().split()
        names.append(name)
        papers.append(paper)
    print(f"Group {gn}")
    for i in range(n):
        for j in range(n-1):
            if papers[i][j] == 'N':
                flag =0
                s = i-j-1
                if s< 0:
                    s+=n
                print(f"{names[s]} was nasty about {names[i]}")
    if flag:
        print("Nobody was nasty")
    gn +=1
    print()
    n = int(input())