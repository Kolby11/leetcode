def remove_duplicates_from_sorted_array(nums: list[int]) -> int:
  for i, num in enumerate(nums):
    if num == "_":
      return nums.index("_")
    while nums.count(num) > 1:
      nums.pop(i)
      nums.append("_")

# 6, nums = [0,1,2,3,4,5,_,_,_,_]
nums1 = [0,0,1,1,2,3,4,5,5,5]
print(f'{remove_duplicates_from_sorted_array(nums1)}, nums = {nums1}')

# 4, nums = [0,1,2,3,4,5,_,_,_]
nums2 = [1,1,2,3,4,4,4]
print(f'{remove_duplicates_from_sorted_array(nums2)}, nums = {nums2}')

# 2, nums = [1,2]
nums3 = [1,1,2]
print(f'{remove_duplicates_from_sorted_array(nums3)}, nums = {nums3}')