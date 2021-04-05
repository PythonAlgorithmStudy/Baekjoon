"""
팰린드롬 찾기
팰린드롬이란?
앞, 뒤가 똑같아 뒤집어도 같은 말이 되는 단어나 문장
"""
import re

word = str(input()).lower()
new_word = list(re.sub('[ :.,]', '', word))
len_word = len(new_word)
flag = 0

for i in range(len_word // 2):
    if new_word[i] != new_word[len_word - i - 1]:
        flag = 1
        break
    
if flag == 0:
    print("True")
else:
    print("False")

"""
1. 정규식을 써서 기호를 없애도 되고
isalnum()->True/False를 사용해 글자 또는 숫자로 구성되면 append를 하는 방법을 써도 됨.

2. list 자료형을 쓴다면 pop함수를 사용할 수도 있다.
new_word.pop(0) != new_word.pop()를 통해 맨앞과 뒤를 비교 후 삭제 가능하다

3. str 자료형을 사용한다면 단어를 뒤집어서 비교하면 된다.
str[::-1]하면 문자열이 뒤집어진다.

4. deque라는 자료형을 사용할 수 있다고 한다. 
이 방법을 쓰면 popleft()가 가능해지며 시간복잡도가 O(1)로 빠르다. 
"""