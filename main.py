import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#################   Load Data  ###################
file_path = "CAPSTONEDATA.csv"  # Update this if necessary
data = pd.read_csv(file_path)

st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Select a Country", ["All"] + list(data["COUNTRY"].unique()))
selected_client = st.sidebar.selectbox("Select a Client ID", ["All"] + list(data["CLIENTID"].unique()))

if selected_country != "All":
    data = data[data["COUNTRY"] == selected_country]
if selected_client != "All":
    data = data[data["CLIENTID"] == selected_client]


st.title("Sales Dashboard")

#########Bar Chart: Gross Income per Country#############
st.subheader("Gross Income per Country")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.barplot(data=data, x="COUNTRY", y="GROSSINCOME", ax=ax1, palette="coolwarm")
ax1.set_title("Gross Income per Country")
st.pyplot(fig1)

#################  Pie Chart: Gross Sales by Client ID  ################
st.subheader("Gross Sales by Client ID")
fig2, ax2 = plt.subplots(figsize=(8, 8))
top_clients = data.nlargest(min(10, len(data)), "GROSSSALES")  # Show top 10 clients
ax2.pie(top_clients["GROSSSALES"], labels=top_clients["CLIENTID"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
ax2.set_title("Top Clients by Gross Sales")
st.pyplot(fig2)

#############  Data Table   ##################
st.subheader("📋 Data Preview")
st.dataframe(data.head(20))  # Show first 20 rows

