def get_odds(nums):
    output = []
    for num in nums:
        if num % 2 != 0:
            output.append(num)
    
    print(output)


nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)