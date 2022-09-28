
def isBalanced(s):
    # Write your code here
    stack = []
    brackets = {'{': '}', '(': ')', '[': ']'}
    openings = ['{', '[', '(']

    for char in s:
        if char in openings:
            stack.append(char)
        else:
            if stack:
                last_element = stack.pop()
                if brackets[last_element] != char:
                    return 'NO'
            else:
                return 'NO'
    return 'NO' if stack else 'YES'


#jeśli założymy że string jest symetryczny po podzieleniu na pół:

# def isBalanced(s):
#     # Write your code here
#     #if s[0:(len(s)//2)] == s[(len(s)//2):][::-1]:
#     openings = ['{', '(', '[']
#     closings = ['}',')',']']
#     stack =[]
#     for i in range(0,len(s)//2):
#         if openings.index(s[i]) == closings.index(s[(len(s)//2):][::-1][i]):
#             stack.append('YES')
#         else:
#             stack.append('NO')
#     if 'NO' in stack:
#         return 'NO'
#     else:
#         return 'YES'