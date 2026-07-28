class Solution:
    def isValid(self, s: str) -> bool:
      # stack to keep track of any open brackets
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)   # if any open brackets are found it will be added to the stack
            else: # checks for a valid match for a clsoing bracket
                if not stack:
                    return False # returns false for empty stack or no open brackets
                
                # remove and return the top element
                top = stack.pop()

                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
        
        # all brackets matched correctly and the stack is empty 
        return len(stack) == 0