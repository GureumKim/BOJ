보완할 점

: 정답은 맞췄는데 실행 시간이 너무 긺<br>
더 좋은 구조 탐구 필요<br>
빠른 구조로 푼 사람 코드

```python
import os
os.write(1,b"\n".join(sorted(sorted(set(os.read(0,os.fstat(0).st_size).strip(b"0123456789").split())),key=len)))
```

아래([juhee0924](https://www.acmicpc.net/user/juhee0924)님 코드)는 56ms, 길이를 가지고 그룹화하는 것은 비슷하다

__set__ 쓰는 게 별로라고 생각했는데 쓰는게  더 빠른 거였다.

### 해답은 **sorted() 메서드**,

sorted()는 iterable을 받아 정렬된 list를 반환한다.
<br>
(**set도 iterable(list, tuple, string, set, dict)** 이다, 순회 가능한 객체

ex. set = {1,2,3} ; for s in set: ... 식으로 “순회” 가능하다.

```python
# 단어 정렬
import sys
input = sys.stdin.readline

# 집합 51개를 가지는 리스트 생성
word_set_list = [set() for _ in range(51)]

# 입력
n = int(input())
for _ in range(n):
    word = input().rstrip()
    word_set_list[len(word)].add(word)

# 정렬 & 출력
for word_set in word_set_list:
    if len(word_set) == 0:
        continue
    word_set = sorted(word_set)
    print('\n'.join(word_set))
```