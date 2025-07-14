def missingNumber(self, nums: List[int]) -> int:
        '''
        0000
        0001
        0010
        0011
        xor = 0 when same and 1 when diff
        '''
        xorr=0
        for i in range(len(nums)):
             xorr ^= i ^ nums[i]
        xorr ^= len(nums)  # XOR the last number separately

        return xorr   