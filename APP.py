import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Function to perform calculations
def calculator(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

# User input for numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# User input for the operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation when the button is clicked
if st.button("Calculate"):
    result = calculator(operation, num1, num2)
    st.write(f"The result is: {result}")
