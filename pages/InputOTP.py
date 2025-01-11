import streamlit as st
import streamlit_shadcn_ui as ui

st.header("Input-OTP Component")

# with open("docs/components/input_otp.md", "r") as f:
#     st.markdown(f.read())

otp_value = ui.input_otp(default_value="123456", max_length=6, key="otp1")
st.write("OTP Value:", otp_value)

st.write(ui.input_otp)