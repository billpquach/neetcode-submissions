class Solution:
    def isValid(self, s: str) -> bool:
        # ({{]})
        # s[i] == ']'       if '[' != 
        # stack = [( { ]
        # only add opening p to stack
        # if s[i] == closing, check if we have corresponding opening & pop stack
        # if pop does not correspond to s[i]: return False
        # stack ({

        # (: 0
        # {: 0
        # [: 0

        count = defaultdict(int)    # O(1)
        corr = {'}': '{',           # O(1)
                ')': '(',
                ']': '[',
                }

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                count[s[i]] += 1
                stack.append(s[i])
            
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack) == 0:
                    return False
                curr_open = stack.pop()
                if count[curr_open] == 0 or corr[s[i]] != curr_open:
                    return False
                count[curr_open] -= 1
        return len(stack) == 0
                


