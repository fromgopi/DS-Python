def product(nums, k):
    prod = []
    p = 1
    for index in range(len(nums)):
        p *= nums[index]
        p /= 1 if index < k else nums[index - k]
        prod.append(p)
    return prod


print(product([7, 6, 5, 4, -4, 5, 6, 0, 7, 8], k=2))
