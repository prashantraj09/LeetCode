class Solution:
    def process(self, s):
        stack = []
        for w in s:
            if w == "#":
                if stack:
                    stack.pop()
            else:    
                stack.append(w)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process(s) == self.process(t)