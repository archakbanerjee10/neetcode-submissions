class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:

        def merge(arr, left, mid, right):
            # Create temporary left and right subarrays
            L = arr[left : mid + 1]
            R = arr[mid + 1 : right + 1]

            i = left  # Initial index of merged subarray
            j = 0  # Initial index of left subarray
            k = 0  # Initial index of right subarray

            # Merge the temp arrays back into arr[left..right]
            while j < len(L) and k < len(R):
                if L[j] <= R[k]:
                    arr[i] = L[j]
                    j += 1
                else:
                    arr[i] = R[k]
                    k += 1
                i += 1

            # Copy the remaining elements of L[], if there are any
            while j < len(L):
                arr[i] = L[j]
                j += 1
                i += 1

            # Copy the remaining elements of R[], if there are any
            while k < len(R):
                arr[i] = R[k]
                k += 1
                i += 1

        def mergesort(arr, l, r):
            # Base case: if the subarray has 1 or fewer elements, it's already sorted
            if l >= r:
                return

            # Find the middle point to divide the array into two halves
            m = (l + r) // 2

            # Sort first and second halves recursively
            mergesort(arr, l, m)
            mergesort(arr, m + 1, r)

            # Merge the sorted halves
            merge(arr, l, m, r)

        # Call mergesort on the entire nums array
        mergesort(nums, 0, len(nums) - 1)

        # Return the fully sorted array to satisfy LeetCode's requirements
        return nums