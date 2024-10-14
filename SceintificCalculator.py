import streamlit as st
import math

# Create a function for the calculator
def scientific_calculator():
    st.title("Scientific Calculator")

    # Select operation
    operation = st.selectbox(
        "Select an operation", 
        ['Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Square Root', 'Sine', 'Cosine', 'Tangent', 'Logarithm (Base 10)']
    )

    # Input fields based on the operation
    if operation in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power']:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)

        if st.button('Calculate'):
            if operation == 'Add':
                st.write(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operation == 'Subtract':
                st.write(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operation == 'Multiply':
                st.write(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operation == 'Divide':
                if num2 == 0:
                    st.error("Error! Division by zero.")
                else:
                    st.write(f"Result: {num1} / {num2} = {num1 / num2}")
            elif operation == 'Power':
                st.write(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")

    elif operation in ['Square Root', 'Sine', 'Cosine', 'Tangent', 'Logarithm (Base 10)']:
        num = st.number_input("Enter the number", value=0.0)

        if st.button('Calculate'):
            if operation == 'Square Root':
                st.write(f"Result: √{num} = {math.sqrt(num)}")
            elif operation == 'Sine':
                st.write(f"Result: sin({num}) = {math.sin(math.radians(num))}")
            elif operation == 'Cosine':
                st.write(f"Result: cos({num}) = {math.cos(math.radians(num))}")
            elif operation == 'Tangent':
                st.write(f"Result: tan({num}) = {math.tan(math.radians(num))}")
            elif operation == 'Logarithm (Base 10)':
                if num <= 0:
                    st.error("Error! Logarithm undefined for non-positive numbers.")
                else:
                    st.write(f"Result: log10({num}) = {math.log10(num)}")

# Run the calculator
if __name__ == "__main__":
    scientific_calculator()
