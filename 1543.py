import sys; input = sys.stdin.readline
txt = input().rstrip()  # '\n'도 받아지니까 rstrip() 사용해서 줄바꿈  escape 문자를 제거해준다
pattern = input().rstrip()
l = len(txt)
s = len(pattern)
cnt = 0
i = s-1

# for 문은 index 건너뛰기 불가 (range 범위 순차적으로 접근) -> while 문 사용
while i < l:      # 인덱스 s-1부터 시작, 맨뒤가 일치하면 pattern 검사
    if txt[i] == pattern[-1]:
        for j in range(s):
            if txt[i-s+1+j] != pattern[j]:
                break
        else:
            cnt += 1
            i += s      # 맞추면 s만큼 인덱스 건너 뜀
            continue
    i += 1
print(cnt)