import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go


st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide"
)



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


fig1.update_layout(width=1100, height=350)
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
fig1.update_layout(width=900, height=500)
st.plotly_chart(fig2)

st.markdown("###### Created with Python by Aneet Narendranath, PhD")
st.markdown('[dnaneet@mtu.edu](dnaneet@mtu.edu) | [LinkedIn](https://www.linkedin.com/in/dnaneet/) | [Google Scholar](https://scholar.google.com/citations?hl=en&user=uSSO_eAAAAAJ&view_op=list_works&authuser=1&sortby=pubdate)')
st.markdown('[Short lecture on the Convergence, Iteration with help from my GTA](https://youtu.be/VZeUe9ZjWb8)')
st.markdown('[Short lecture on the importance of computational thinking](https://youtu.be/y0EJsWmNvFU)')