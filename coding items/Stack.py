# 1. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#Example 1:
#Input: s = "()"
#Output: true
#Example 2:
#Input: s = "()[]{}"
#Output: true
#Example 3:
#Input: s = "(]"
#Output: false
#Example 4:
#Input: s = "([])"
#Output: true
#Example 5:
#Input: s = "([)]"
#Output: false

# Approach
# Traverse the string character by character.
# If it is an opening bracket ((, [, {), push it onto the stack.
# If it is a closing bracket (), ], }):
# Check if the stack is empty → if yes, return False.
# Otherwise, pop from the stack and ensure the popped element matches the type of closing bracket.
# If not matching, return False.
# At the end, if the stack is empty, return True; otherwise, False.

class Solution:
    def isValid(self, s: str) -> bool:

        i=0
        a=[]

        for i in range(len(s)):

            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])

            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False

        return len(a)==0



# 2. Simplify Path
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
# The rules of a Unix-style file system are as follows:
# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

# Example 1:
# Input: path = "/home/"
# Output: "/home"
# Explanation: The trailing slash should be removed.

# Example 2:
# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: Multiple consecutive slashes are replaced by a single one.

# Example 3:
# Input: path = "/home/user/Documents/../Pictures"
# Output: "/home/user/Pictures"
# Explanation: A double period ".." refers to the directory up a level (the parent directory).

# Example 4:
# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is not possible.

# Example 5:
# Input: path = "/.../a/../b/c/../d/./"
# Output: "/.../b/d"
# Explanation: "..." is a valid name for a directory in this problem.


class Solution:
    def simplifyPath(self, path: str) -> str:

        p = path.split('/')
        s = []

        for i in p:
            if i == '' or i == '.':
                continue
            
            if i == '..':
                if s:
                    s.pop()

            else:
                s.append(i)

        return '/' + '/'.join(s)


# 3. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output: [null,null,null,null,-3,null,0,-2]
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            minval = min(value, self.stack[-1][1])
            self.stack.append((value, minval))

    def pop(self) -> None:
        self.stack.pop()       

    def top(self) -> int:
        return self.stack[-1][0] 

    def getMin(self) -> int:
        return self.stack[-1][1] 



# 4. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                c2, c1 = stack.pop(), stack.pop()
                stack.append(c1 - c2)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                c2, c1 = stack.pop(), stack.pop()
                stack.append(int(c1 / c2))
            else:
                stack.append(int(i))
        
        return stack[0]


# 5. Basic Calculator
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
# Example 1:
# Input: s = "1 + 1"
# Output: 2
# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        curr = 0
        sign = 1

        for i in s:
            if i.isdigit():
                curr = curr * 10 +int(i)
            elif i == "+":
                res += sign * curr
                sign = 1
                curr = 0
            elif i == "-":
                res += sign * curr
                sign = -1
                curr = 0
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif i == ")":
                res += sign * curr
                curr = 0
                res *= stack.pop()
                res += stack.pop()

        res += sign * curr
        return res
