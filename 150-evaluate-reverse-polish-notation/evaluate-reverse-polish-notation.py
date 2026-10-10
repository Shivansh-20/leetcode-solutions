class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        store = []
        op = ["+","-","/","*"] #string
        for i in tokens:
            if i not in op:
                store.append(int(i)) #convert to int
            else:
                a = store.pop()
                b = store.pop()
                if i == "+":
                    result = a + b
                elif i == "-":
                    result = b - a
                elif i == "*":
                    result = a*b
                elif i == "/":
                    result =  abs(b) // abs(a) * (1 if b * a >= 0 else -1) #int(b / a)
                store.append(result)
        return store[0]
            
                    
                

        