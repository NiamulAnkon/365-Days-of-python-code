import streamlit as st
import time

st.title("Welcome to my first streamlit app")

st.header("see around this site hope fully you like it")

st.info("this is a info about me\ni have been doing coding since almost 2 years")

st.write("Write what you want")
st.write(range(6969))

st.text("Look at the math equation")

st.latex(r''' a+b x^2+c''')
st.markdown(":moon:")

st.checkbox("You did seen this thing on some site right?")

st.button("Click here to get rich and pray for me")

st.select_slider("how much you rate this", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

st.progress(20)

with st.spinner("Just wait"):
    time.sleep(2)


st.balloons()

