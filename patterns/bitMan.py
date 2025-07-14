'''
There is usually the use of XOR, OR and AND
in these type of questions along with >> and << to shift the bits

'''

def single_number(nums: List[int])->int:
    xor=0
    for i in range(len(nums)):
        xor^=nums[i]
    return xor

'''
one more example where we use >> to right shift it by 1
0010--->0001
'''
def func(n:int)->int:
    count=0
    for i in range(32):
        count+=(n&1)
        n=n>>1
    return count