## MAXIMUM SUBSEQUENCE SUM PROBLEM:
Given (possibly negative) integers a_1 , a_2 , . . . , a_n , find the maximum value of a_i + a_(i+1) + ... + a_j. 
(For convenience, the maximum subsequence sum is 0 if all the integers are negative.)

Example:
For input -2, 11, -4, 13, -5, -2, the answer is 20 (a_2 through a_4 ).

## Solution A
```python
def max_subsequence_sum(nums):
    this_sum, max_sum = 0, 0
    i, j = 0, 0
    best_i, best_j = 0, 0
    while j < len(nums):
        this_sum += nums[j]
        if this_sum > max_sum:
            max_sum = this_sum
            best_i = i
            best_j = j
        if this_sum < 1:
            i = j + 1
            this_sum = 0
        j += 1
    return max_sum, best_i, best_j
```

## Solution B
```python
def max_subsequence_sum(nums):
    return max_sub_sum(nums, 0, len(nums)-1)


def max_sub_sum(nums, left, right):
    if left == right:
        if nums[left] <= 0:
            return 0, left, right
        else:
            return nums[left], left, right
    center = (left + right) / 2
    max_left_sum, left_best_i, left_best_j = max_sub_sum(nums, left, center)
    max_right_sum, right_best_i, right_best_j = max_sub_sum(
        nums, center+1, right)
    left_border_sum, max_left_border_sum = 0, 0
    j, best_i = center, center
    while j >= left:
        left_border_sum += nums[j]
        if left_border_sum > max_left_border_sum:
            max_left_border_sum = left_border_sum
            best_i = j
        j -= 1
    right_border_sum, max_right_border_sum = 0, 0
    j, best_j = center + 1, center + 1
    while j <= right:
        right_border_sum += nums[j]
        if right_border_sum > max_right_border_sum:
            max_right_border_sum = right_border_sum
            best_j = j
        j += 1
    max_border_sum = max_left_border_sum + max_right_border_sum
    max_all_sum = max([max_left_sum, max_right_sum, max_border_sum])
    if max_left_sum == max_all_sum:
        best_i = left_best_i
        best_j = left_best_j
    if max_right_sum == max_all_sum:
        best_i = right_best_i
        best_j = right_best_j
    return max_all_sum, best_i, best_j
```

## Test code
```python
def main():
    nums = [4, -3, 5, -2, -1, 2, 6, -2]
    print max_subsequence_sum(nums)
    nums = [-2, 11, -4, 13, -5, -2]
    print max_subsequence_sum(nums)


if __name__ == "__main__":
    main()
```
