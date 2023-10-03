idx = {
    'A' : 0,
    'G' : 1,
    'C' : 2,
    'T' : 3
}

arr = [
    "ACAG",
    "CGTA",
    "ATCG",
    "GAGT"
]

l = int(input())
dna = list(input())

def result(temp,length):
    while length > 1:
        An = temp.pop()
        An_1 = temp.pop()
        temp += arr[idx.get(An_1)][idx.get(An)]
        length-=1
    return temp[0]
print(result(dna,l))