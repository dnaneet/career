import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go




df = pd.read_csv('innovations-timeline-2.csv')
year_items = df['Year']
x = st.selectbox('Select Year', np.unique(year_items))
st.write('My scholarly output is reflected from 2015. I was away from academia in the academic year 2015-2016, working at the French Nuclear commision.  During this time, I did not have any teaching responsibilities.')
st.write('Teaching evaluation scores are available on request.')


st.title('Summary of instructional innovations & scholarly outcomes')
#st.dataframe( df[df['Year']==x] )
fig1 = go.Figure(data=[go.Table(
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


fig1.update_layout(width=900, height=500)
st.plotly_chart(fig1)

st.title('Nomination for Instructional Awards')
yr = np.array([2016, 2017, 2018, 2019, 2020, 2020]);
nominations = np.array(['Wolfram Innovator Award Nomination',
                        'Best Teacher - Finalist out of 40 faculty', 
                        'Best Teacher - Finalist out of 40 faculty',
                        'Best Teacher - Finalist out of 40 faculty',
                        'Best Teacher - Finalist out of 40 faculty',
                        'Deans Teaching Showcase'])
category = np.array(['Industry', 'Department', 'Department', 'Department', 'Department', 'College'])                        
df_awards = pd.DataFrame({'Year': yr, 'Nomination or Award': nominations, 'Category':category})

fig2 = go.Figure(data=[go.Table(
    header=dict(values=list(df_awards.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_awards[df_awards['Year']==x]['Year'],
            df_awards[df_awards['Year']==x]['Nomination or Award'],
            df_awards[df_awards['Year']==x]['Category']],
            fill_color='lavender',
            align='left'))
])
st.plotly_chart(fig2)

st.markdown("###### Created with Python by Aneet Narendranath, PhD, dnaneet@mtu.edu")
