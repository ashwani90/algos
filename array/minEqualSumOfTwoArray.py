'''

You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.


Example 1:

Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
Output: 12
Explanation: We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.


Example 2:

Input: nums1 = [2,0,2,0], nums2 = [1,4]
Output: -1
Explanation: It is impossible to make the sum of both arrays equal.

'''

def minSum(nums1, nums2):
    sum1 = sum(nums1)
    sum2 = sum(nums2)

    diff = abs(sum1 - sum2)

    # Count zeros in both arrays
    zeros1 = nums1.count(0)
    zeros2 = nums2.count(0)

    # Step 2: Early exit for feasibility
    if diff == 0:
        return sum1  # Already equal
    if zeros1 + zeros2 < diff:
        return -1  # Not enough zeros to bridge the gap

    min_adds = []
    if sum1 < sum2:
        min_adds.extend(1 for _ in range(zeros1))  # Replace nums1 zeros with 1
        min_adds.extend(range(1, zeros2 + 1))  # Replace nums2 zeros with increasing values
    else:
        min_adds.extend(range(1, zeros1 + 1))  # Replace nums1 zeros with increasing values
        min_adds.extend(1 for _ in range(zeros2))  # Replace nums2 zeros with 1
    
    # Use smallest additions to balance the difference
    min_adds.sort()
    total_added = 0
    for add in min_adds:
        if diff <= 0:
            break
        total_added += add
        diff -= 1

    if diff > 0:
        return -1  # Unable to balance
    return max(sum1, sum2) + total_added