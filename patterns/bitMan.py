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

'''
Some also use dp programming like this one 
'''
def func(n: int)-> List[int]:
    dp=[0]*(n+1)
    for i in range(1, n+1):
        offset=1
        if(offset*2==i):
            offset=i
        dp[i]=1+dp[i-offset]
    return dp


def reverseBits(self, n: int) -> int:
    res=0
    for i in range(32):
        bit =  (n >> i) & 1
        res = res | (bit << (31-i)) 
    return res  
