import streamlit as st

def find_largest(a, b, c):
    """
    This function takes in three numbers and returns the largest among them.
    """
    return max(a, b, c)

st.title("Find the largest among 3 numbers")

# Get input from user
a = st.number_input("Enter first number:")
b = st.number_input("Enter second number:")
c = st.number_input("Enter third number:")

# Find the largest number
largest_num = find_largest(a, b, c)

# Display result
st.write("The largest number is:", largest_num)

