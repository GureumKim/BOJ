while 1:
    n = input()
    if n == "0":
        break
    s,e = 0,len(n)-1
    while s<=e:
        if n[s]!=n[e]:
            print("no")
            break
        s += 1
        e -= 1
    else:
        print("yes")