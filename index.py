class Parentheses:
    def isBalanced(self, s: str) -> bool:
        """
        Checks if a given string contains balanced parentheses.

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the string contains balanced parentheses, otherwise returns False.
        """
        stack = []
        hashMap = {')': '(', ']': '[', '}': '{'} #Hashmap to store the closing and opening parentheses

        for p in s:
            if p in hashMap.values():
                stack.append(p) #Any open parenteses push into stack
            elif stack and hashMap[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []

def main():
    '''
    Reads user input, checks for valid input, and validates parentheses.

    Returns:
        None
    '''
    user_input = input("Enter a string of parentheses: ")

    if not only_parentheses(user_input):
        print("Invalid input. Please try again.")
        return

    parentheses = Parentheses()
    is_valid= parentheses.isBalanced(user_input)

    if is_valid:
        print("Input string contains valid parentheses.")
    else:
        print("Input string does not contain valid parentheses.")

def only_parentheses(user_input):
    """
    Check if the input string contains only parentheses.

    Args:
        user_input (str): The input string to be checked.

    Returns:
        bool: True if the input contains only parentheses, otherwise returns False.
    """
    for p in user_input:
        if p not in "()[]{}":
            return False
    return True

if __name__ == "__main__":
    main()










            

            
                