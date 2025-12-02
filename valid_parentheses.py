# Given a string containing characters that may include parentheses (), braces {}, and brackets [], determine if the string is 
# well-formed (every opening symbol has a matching closing symbol in the correct order).

def isValid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in pairs.values():  # opening
            stack.append(ch)
        elif ch in pairs:  # closing
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
