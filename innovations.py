import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title('Summary of instructional innovations & scholarly outcomes')

df = pd.read_csv('innovations-timeline-2.csv')

year_items = df['Year']

x = st.selectbox('Select Year', np.unique(year_items))
st.write('My scholarly output is reflected from 2015. I was away from academia in the academic year 2015-2016, working at the French Nuclear commision.  During this time, I did not have any teaching responsibilities.')
st.write('Teaching evaluation scores are available on request.')

#st.dataframe( df[df['Year']==x] )

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df[df['Year']==x]['Year'],
		       df[df['Year']==x]['Course'],
		       df[df['Year']==x]['Activity'],
		       df[df['Year']==x]['Category'],
		       df[df['Year']==x]['Scholarly output'],
		       df[df['Year']==x]['Title'],
		       df[df['Year']==x]['Other Outcome']],
               fill_color='lavender',
               align='left'))
])


fig.update_layout(width=900, height=600)
st.plotly_chart(fig)


st.markdown("###### Created with Python by Aneet Narendranath, PhD, dnaneet@mtu.edu")
