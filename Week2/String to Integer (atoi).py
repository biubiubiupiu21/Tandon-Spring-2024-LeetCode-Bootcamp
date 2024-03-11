class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        def digits_to_int(digits):
            string_number = ''.join(map(str, digits))
            return int(string_number)

        def is_number(s):
            try:
                float(s)  # Try converting to a float
                return True
            except ValueError:
                return False

        n = len(s)
        sign = -1
        firstSign = 0
        firstNumber = 0
        returnList = []
        min_val = -2**31
        max_val = 2**31 - 1

        for i in range(n):
            if s[i] == "+":
                firstSign = i
                sign = 1
                break
            elif s[i] == "-":
                firstSign = i
                sign = 0
                break
            elif is_number(s[i]) == True:
                firstSign = i
                break
            elif s[i] == " ":
                pass
            else:
                return 0


        start = max(firstSign,firstNumber)
        print(firstSign,firstNumber)
        if firstSign >= firstNumber and sign != -1:
            start = start + 1
        for j in range(start,n):
            if is_number(s[j]) == True:
                returnList.append(s[j])
            else:
                break 
        # print(returnList)

        if len(returnList) == 0:
            return 0
        else:
            number = digits_to_int(returnList)
            if sign == 0:
                number = -number
            else:
                pass

            if min_val <= number <= max_val:
                return number
            elif number < min_val:
                return min_val
            else:
                return max_val
