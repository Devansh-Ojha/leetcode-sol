'''
The key idea here is that you check the middle and update the pointer 
accordingly this would help to minimize looking at unecessary values
'''


def search(self, nums: List[int], target: int) -> int:
        l = 0
        r=len(nums)-1

        while l<= r:
            middle = (l+r)//2
            if nums[middle] < target:
                l=middle+1
            elif (nums[middle]>target):
                r=middle-1
            else:
                return middle
        return -1
        