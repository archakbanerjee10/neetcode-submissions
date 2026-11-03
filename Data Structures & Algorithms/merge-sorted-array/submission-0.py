class Solution:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Initialize pointers
    i = m - 1  # Last valid element in nums1
    j = n - 1  # Last element in nums2
    k = m + n - 1  # Last position of nums1

    # Merge in reverse order
    while i >= 0 and j >= 0:
      if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
      else:
        nums1[k] = nums2[j]
        j -= 1
      k -= 1

    # If there are remaining elements in nums2, copy them over
    while j >= 0:
      nums1[k] = nums2[j]
      j -= 1
      k -= 1

    # Note: No return statement needed! nums1 is modified in-place.