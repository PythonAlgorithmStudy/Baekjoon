"""
937. Reorder Log Files
맨 앞은 식별자
문자 로그가 숫자 로그를 앞서고
문자 로그들은 사전순서로
ex. logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
"""

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
log_str = []
log_num = []
nums = list(map(str, list(range(10))))  #["1", 2, ..., 9]
# 문자, 숫자 분리해 각각 sort 후 합치기
for i in range(len(logs)):
    if logs[i][5] in nums:  # isdigit으로 가능하다 함..
        log_num.append(logs[i])
    else:
        log_str.append(logs[i])

sorted_strs = sorted(log_str, key=lambda x:x[5])


result = sorted_strs + log_num

print(result)