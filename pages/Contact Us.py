import streamlit as st
import pandas as pd
import streamlit
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
from plotly.graph_objs import Histogram
from streamlit.elements.widgets.selectbox import SelectboxSerde

sns.set()

data=pd.read_csv("tips.csv")


###### Kinonvert ko lang yung billdate para sa x axis########
#data['billdate'] = pd.to_datetime(data['billdate'])


st.header("Sales Daily Rate")
streamlit.line_chart(data,x="billdate",y="total_bill",color='#FF0000')


st.divider()

st.scatter_chart(data,x="tip",y="total_bill",color='#0C0844')


st.divider()

fig, ax = plt.subplots()
ax.hist(data["tip"],bins=20, label="Histogram", color='Pink')


st.pyplot(fig)

st.divider()

a=st.number_input("What is your Salary")
b=st.number_input("How much is your Tax")
if st.button("CALCULATE"):
    c=a-b
else:
    c=0.00
st.write("My Net Salary is ", c)







