from main.others import decorator

class solution:
    @decorator.metric
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    @decorator.metric
    def twoSumPro(self, nums, target):
        idx = {}
        for id, ele in enumerate(nums):
            mid = target - ele
            if mid in idx:
                return [idx[mid], id]
            idx[ele] = id    


if __name__ == '__main__':
    s = solution()
    print(s.twoSum([2, 7, 11, 15], 9))    
    print(s.twoSumPro([2, 7, 11, 15], 9)) 