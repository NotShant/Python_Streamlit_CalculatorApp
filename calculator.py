import streamlit as st

def calculate(operation, num1, num2):
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
            return 'Error: Division by zero'
    else:
        return 'Invalid operation'

def main():
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 8px;
    }
    .title {
        font-size: 5em;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .input-box {
        margin-bottom: 20px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    .button:hover {
        background-color: #45a049;
    }
    .result {
        font-size: 1.5em;
        color: #555;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="title">Calculator</div>', unsafe_allow_html=True)
    
    # Input fields
    num1 = st.number_input('Enter the first number', value=0)
    num2 = st.number_input('Enter the second number', value=0)

    # Dropdown for selecting operation
    operation = st.selectbox('Select an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

    # Button to perform calculation
    if st.button('Calculate', key='calculate', help='Click to perform calculation'):
        result = calculate(operation, num1, num2)
        st.markdown(f'<div class="result">Result: {result}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
