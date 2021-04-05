"""
15. 3Sum
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트 출력
"""
nums = [-1,0,1,2,-1,-4]
results = []
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] + nums[j] + nums[k] == 0 and i < j and j < k:
                zeros = [nums[i], nums[j], nums[k]] 

                
                results.append(zeros)
for i in results:
    i.sort(key=lambda x:x)
unique_results = tuple(set(map(tuple, results)))
list_results = list(map(list, unique_results))
print(list_results)