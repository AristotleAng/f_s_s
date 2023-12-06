def subset_sum_backtrack(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:]) 
            return
        for i in range(start, len(nums)):
            if target - nums[i] >= 0:
                path.append(nums[i])
                backtrack(i + 1, target - nums[i], path)
                path.pop()

    result = []
    nums.sort()  
    backtrack(0, target, [])
    return result

if __name__=="__main__":
    nums = [2, 4, 6, 8]
    target_sum = 8
    subsets = subset_sum_backtrack(nums, target_sum)
    print(subsets)
