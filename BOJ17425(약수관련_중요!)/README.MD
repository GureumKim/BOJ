# 알게된 내용

## python3 vs PyPY(참조. https://yoon-e.tistory.com/6)
Python3로 제출하게 되면 시간초과로 오답처리가 되지만 같은 코드를 PyPy로 돌리면 정답처리가 되는데, 이는 PyPy가 Python3 보다 더 빠른 연산속도를 가지기 때문이다. 만약 다른 문제에서도 Python3로 시간초과가 뜬다면 PyPy로 제출하는 방법도 생각해보자
<br>
PyPy는 반복되는 코드에 대한 캐싱기능(?)이 있어 이러한 반복을 많이 수행하는 코드에는 PyPy가 유리할 수 있다.

## 추가할 것들
### DP와 시간 복잡도
### PyPy vs Python3 보충 필요