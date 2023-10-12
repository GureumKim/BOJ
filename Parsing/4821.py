while 1:
    total = int(input())
    pages = [0]*(total+1)
    if total == 0: break
    ranges = input().rstrip().split(',')
    for i in range(len(ranges)):
        a = ranges[i].split('-')
        low, high = int(a[0]),int(a[-1])
        # print(low,high)
        if low<=high:
            if high<=total:
                pages[low:high+1] = [1]*(high-low+1)
            else:
                if low<=total:
                    pages[low:]=[1]*(total-low+1)
    # print("******************")
    print(pages.count(1))
    # print("******************")