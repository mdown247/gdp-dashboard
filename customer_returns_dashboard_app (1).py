
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Customer Returns Dashboard', layout='wide')
st.title("Customer Returns Dashboard")
st.image("UploadedImage1.jpg", width=300)

view = st.radio("Select View", ["Customer Returns Summary", "Pivot Chart"])

if view == "Customer Returns Summary":
    st.subheader("Summary Table")
    df = pd.DataFrame({"Month": [], "Total Dollar Amount": []})
    st.dataframe(df)
    st.bar_chart(df.set_index("Month"))
else:
    st.subheader("Pivot Chart View")
    df = pd.DataFrame({"Month": [], "Total Dollar Amount": []})
    st.dataframe(df)
    st.bar_chart(df.set_index("Month"))
