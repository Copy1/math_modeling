#pos_num_sum=0
#max_value = int(input())
#min_value = int(input())
#for num in range(min_value, max_value + 1):
#    if num > 0:
#        pos_num_sum += num
#print(min_value, max_value, pos_num_sum)

nums = [int(num) for num in input().split()]
pos_num_sum = 0
for num in nums:
    if num >0:
        pos_num_sum += num 
print(pos_num_sum, min(nums), max(nums))
