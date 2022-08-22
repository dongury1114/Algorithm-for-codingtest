# 입력: str1, str2

# 출력: 자카드 유사도 -> 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# ans = int(ans *  65536)
import re
from itertools import combinations
str1 = "FRANCE"
str2 = "french"
answer = 0

special = re.compile(r'[^ A-Za-z0-9가-힣+]')

# 정규표현식을 사용해서 일단 특수문자 다날리기
# result = special.sub('',text)
str1 = list(special.sub("", str1).lower().strip())
str2 = list(special.sub("", str2).lower().strip())

tmp_str1 = list(combinations(str1, 2))
tmp_str2 = list(combinations(str2, 2))

tmp_diff = list(set(tmp_str1) & set(tmp_str2))
tmp_union = list(set(tmp_str1) | set(tmp_str2))

if len(str1) == 0 and len(str2) == 0:
    print(1)
else:
    answer = int(len(tmp_diff)/len(tmp_union)*65536)
    print(answer)
