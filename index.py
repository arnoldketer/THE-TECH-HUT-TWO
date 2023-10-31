class Parentheses:
    def isBalanced(self, s: str) -> bool:
        stack = []
        hashMap = {')': '(', ']': '[', '}': '{'} #Hashmap to store the closing and opening parentheses

        for p in s:
            if p in hashMap.values():
                stack.append(p)
            elif stack and hashMap[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []


            

            
                