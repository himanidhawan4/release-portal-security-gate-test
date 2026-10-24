"""
SonarCloud detection test.
WARNING: This file intentionally contains insecure code.
Use only in a test branch; do not use this pattern in production.
"""

def evaluate_user_expression(user_input):
    # Intentionally unsafe: eval can execute arbitrary Python expressions.
    return eval(user_input)


if __name__ == "__main__":
    expression = input("Enter an expression: ")
    print(evaluate_user_expression(expression))
