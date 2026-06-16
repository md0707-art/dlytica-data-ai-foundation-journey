# Day 1 Assignment
# Operator Precedence & Associativity in Python

print("=== Operator Precedence & Associativity ===\n")

# Example 1: Multiplication before Addition
print("2 + 3 * 4 =", 2 + 3 * 4)
# Expected Result: 14
# Reason: * has higher precedence than +

# Example 2: Parentheses Override Precedence
print("(2 + 3) * 4 =", (2 + 3) * 4)
# Expected Result: 20
# Reason: Parentheses are evaluated first

# Example 3: Exponentiation is Right Associative
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
# Expected Result: 512
# Reason: Evaluated as 2 ** (3 ** 2)

# Example 4: Exponentiation before Unary Minus
print("-3 ** 2 =", -3 ** 2)
# Expected Result: -9
# Reason: Evaluated as -(3 ** 2)

# Example 5: Left-to-Right Associativity
print("100 / 5 * 2 =", 100 / 5 * 2)
# Expected Result: 40.0
# Reason: / and * have same precedence, evaluated left to right

print("10 - 5 - 2 =", 10 - 5 - 2)
# Expected Result: 3
# Reason: - is left associative

# Example 6: Arithmetic + Comparison + Logical
result = 5 + 3 > 6 and not False

print("5 + 3 > 6 and not False =", result)
# Expected Result: True
# Reason:
# 5+3=8
# 8>6=True
# not False=True
# True and True=True