class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        countStack = []  # Stack for keeping track of numbers
        stringStack = []  # Stack for keeping track of strings
        currentString = ""
        k = 0
        
        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # Building the multiplier for cases like "10[a]"
            elif char == '[':
                # Push the current state to the stacks
                countStack.append(k)
                stringStack.append(currentString)
                # Reset for the new substring
                k = 0
                currentString = ""
            elif char == ']':
                # Pop the last number (multiplier) and string from their respective stacks
                num = countStack.pop()
                prevString = stringStack.pop()
                # Decode the current part and append it to the string from the top of the string stack
                currentString = prevString + num * currentString
            else:
                currentString += char  # Build the current string
        
        return currentString