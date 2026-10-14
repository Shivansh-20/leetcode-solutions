class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        def nsl(n,arr):
            stack = []
            result = []
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                if stack: #cannpt use to check stack not empty keeping orignal?
                    result.append(stack[-1])
                else:
                    result.append(-1)
                stack.append(i)
            return result
        def nsr(n,arr):
            stack = []
            result = n * [n]
            for i in range(n-1,-1,-1): #stop -1 is excluded so stop at index 0
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1]
                stack.append(i)
            return result
        left = nsl(n,arr)
        right = nsr(n,arr)
        total_sum = 0
        for i in range(n): #will stop at index 3
            ls = i - left[i]
            rs = right[i] - i
            total_sa = ls * rs
            total_sum = (total_sum + arr[i] * total_sa) % mod
        return total_sum





