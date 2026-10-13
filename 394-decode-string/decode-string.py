class Solution:
    def decodeString(self, s: str) -> str:
        current_nums = 0
        current_string = ""
        stack = []
        for char in s:
            if char.isdigit():
                current_nums = current_nums * 10 + int(char)
            elif char is "[":
                stack.append((current_nums, current_string))
                current_nums = 0
                current_string = ""
            elif char is "]":
                #stack.pop()
                rc, previous_string = stack.pop()
                current_string = previous_string + current_string * rc
                #while current_num:
                    #current_string = char + current_string
            else:
                current_string += char
        return current_string



        