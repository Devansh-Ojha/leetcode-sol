def func(n: int)-> List[int]:
    '''
    key idea here is 
    0000
    0001
    0010
    0011
    0100

    01 01
    01 10
    01 11
    10 00

    change the offset when 1s place shift 
    '''
    arr=[0]*(n+1)
    for i in range(1, n+1):
        offset=1
        if(offset*2==i):
            offset=i
        dp[i]=1+dp[i-offset]
