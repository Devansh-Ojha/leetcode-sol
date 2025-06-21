class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        # This is need for the to keep track of things we have seen so far

        theMap={']':'[', '}':'{', ')':'('}
        # This is required we want to map the things we have seen vs things we have not seen so far

        for c in s:
            #just going over characters in the string

            if c in theMap:

                if stack and stack[-1]==theMap[c]:
                    
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False