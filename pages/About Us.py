import streamlit as st
import pandas as pd

data=pd.read_csv("tips.csv")


st.title("Data Table")
st.table(data)

