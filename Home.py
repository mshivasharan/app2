import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Shiva Sharan Mudda")
    content = """
    Hi, I am Shiva! I am a Python programmer, currently working as a Senior Development Engineer in Germany. I graduated in 2014 with a Master of Science in Automation and Robotics from the Technical University of Dortmund in Germany with a focus on Robotics. I have also finished a advanced certification in Artificial Intelligence and Machine learning from the university IIIT Hyderabad in India
I have worked with companies from various countries, such as Dressler Automation, Germany and USA, IMSTec Germany, Fraunhofer insititute Germany and DigitUp as Senior Manager in India.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
