def kadane(nums: List[int]) -> int:

    '''
    Basically key idea is that if we adding the other number and its
    decreasing it then its better to start fresh
    '''
    curr=nums[0]
    ma=nums[0]

    for i in range(1, len(nums)):
        curr=max(nums[i],curr+nums[i])
        ma=max(curr, ma)
    return ma

    '''
    Another way to think about it is that if curr<0 then just set
    it to 0 and start fresh as its gonna drag it down

    for num in nums:
        if curr<0:
        curr=0
        curr+=nums
        ma=max(curr,ma)

    '''
