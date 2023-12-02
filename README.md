**Shunting Yard Algorithm for Evaluating Mathematical Expressions**

### Overview

This Python script demonstrates the Shunting Yard algorithm to convert infix mathematical expressions into postfix notation and subsequently evaluates them. The script extends the basic Shunting Yard algorithm to handle decimal numbers and multi-digit integers using regular expressions.

### Features

1. **Decimal and Integer Support:**
   - The script recognizes both integers and decimal numbers, including multi-digit integers and decimals with an integer part.
   - Regular expressions are used to validate input strings as integers or decimals.

2. **Basic Operators:**
   - The script supports basic arithmetic operators: `+`, `-`, `*`, `/`, `^` (exponentiation), `(`, and `)`.

3. **Error Handling:**
   - The script provides error messages for various scenarios, such as unknown symbols, unmatched parentheses, and invalid postfix expressions.

### Functions

1. **`is_integer_or_decimal(s)`**
   - Checks if an input string matches an integer or decimal number using regular expressions.

2. **`make_infix(expr)`**
   - Splits the input expression into individual parts, including operators and operands.

3. **`convert(expr)`**
   - Converts an infix mathematical expression to postfix notation, considering decimal numbers and multi-digit integers.

4. **`evaluator(expr)`**
   - Evaluates a postfix mathematical expression, handling basic arithmetic operations.

### Example Usage

```python
expr = "(2.5*4+3*2.0)^1.5"
print(f"After preprocessing, {expr} becomes:")
infix = make_infix(expr)
print(infix)
postfix = convert(infix)
print("Then in postfix: ", postfix)
print("which evaluates to: %.3f" % evaluator(postfix))
```

### Notes
- Only handles infix expressions, so ensure parentheses are used if subtracting
- The script uses regex for improved handling of decimal numbers and multi-digit integers.
- Error messages are displayed for invalid expressions.
- The example demonstrates the conversion of an infix expression to postfix and its subsequent evaluation.

Feel free to modify the `expr` variable in the example to test the script with different mathematical expressions.
