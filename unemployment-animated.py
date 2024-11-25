
import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('annual_unemployment_state.csv')
df.drop(columns='State', inplace=True)
df.dropna(inplace=True)

# Transforming the dataset to long format
df = df.reset_index()
dfm = pd.melt(df, id_vars='ST', value_vars=['ST']+[str(x) for x in range(1980, 2019)])
dfm.rename(columns={'variable':'year', 'value':'unemployment'}, inplace=True)

st.header('State unemployment rates (1980-2019)')

fig = px.bar(dfm,
            x="ST",
            y="unemployment",
            animation_frame="year",
            color="ST",
            range_y=[0,15])

event = st.plotly_chart(fig, key="mpg", on_select="rerun")

event.selection

st.header('Data source')
st.dataframe(dfm)
