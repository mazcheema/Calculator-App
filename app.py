# ============================================
# 🧮 Simple Streamlit Calculator App
# For Hugging Face or local use
# ============================================

import streamlit as st

# --- App Title ---
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")
st.markdown("Perform basic arithmetic operations easily!")

# --- Input Fields ---
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# --- Operation Selection ---
operation = st.selectbox(
    "Select an operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# --- Perform Calculation ---
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Cannot divide by zero!")
                result = None
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"✅ Result: **{result}**")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
