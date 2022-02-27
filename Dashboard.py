import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Headings for dashboard

st.title("Covid-19 Dashboard For India")
st.markdown('The dashboard will visualize the Covid-19 Situation in India')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

# reading dataset for corona cases state wise
df = pd.read_csv("Corona Stats.csv")

# plotting data of all states in form of pie chart
fig = px.pie(df, values=df['Cases'], names=df['State'])
st.plotly_chart(fig)

# creating a sidebar with a dropdown
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
# checking condition for the selected option in sidebar
if not st.sidebar.checkbox("Hide", False, key='1'):
    if select == 'Pie chart':
        # plotting pie chart graph for top five cities
        st.title("Selected top 5 cities")
        fig = px.pie(df, values=df['Cases'][:5], names=df['State'][:5], title='Total Confirmed Cases')
        st.plotly_chart(fig)
    if select == 'Bar plot':
        st.title("Selected Top 5 Cities")
        # plotting bar chart graph for top five cities
        fig = go.Figure(data=[go.Bar(name='Cases', x=df['State'][:5], y=df['Cases'][:5]),
                              go.Bar(name='Cured', x=df['State'][:5], y=df['Cured'][:5]),
                              go.Bar(name='Death', x=df['State'][:5], y=df['Death'][:5])])
        st.plotly_chart(fig)

# reading corona data on daily bases
df2 = pd.read_csv('case_time_series.csv')
# fetching date from the dataset
df2['Date'] = df2['Date'].astype('datetime64[ns]')
# creating another sidebar
select1 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered'], key='2')
# checking condition for selected option in another sidebar
if not st.sidebar.checkbox("Hide", False, key='3'):
    if select1 == 'Confirmed':
        # plotting line graph for confirmed cases
        fig = px.line(df2, x=df2["Date"], y=df2["Total Confirmed"])
        st.plotly_chart(fig)
    elif select1 == 'Recovered':
        # plotting line graph for Recovered cases
        fig = px.line(df2, x=df2["Date"], y=df2["Total Recovered"])
        st.plotly_chart(fig)
