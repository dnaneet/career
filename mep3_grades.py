import streamlit as st
import dask.dataframe as dd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.markdown('## MEP3 Historical Gradebook Dashboard')
st.write("This dashboard summarizes student grades in semesters when Dr. Narendranath was one of the instructors of MEP3.")
st.write(" ")
df = dd.read_csv('*_*.csv')
#print(df.columns)
#df.dtypes

u = np.unique(df['Semester'])
#print(u[0])

sem = st.sidebar.selectbox('Select semester of interest:', ['Fall 2017', 'Spring 2018', 'Fall 2018', 'Spring 2019', 'Fall 2019', 'Fall 2020', 'Spring 2021'])
ts =  st.sidebar.slider('Select threshold final score:', max_value = 100, min_value=0)
st.sidebar.markdown("---")
st.sidebar.markdown("Created by Dr. Narendranath using Python and Streamlit.  Confidential student identifier information has not been used in this dashboard.")
col1, col2, col3  = st.beta_columns(3)


with col1:
	st.markdown("#### Total students in the selected semester:")
	#total_students_this_sem = df[(df['Semester'] == sem)['Final Score'].count().compute()
	df_temp = pd.DataFrame({'Final Score': df[df['Semester'] == sem]['Final Score'].compute(), 'Threshold met':df[df['Semester'] == sem]['Final Score'].compute()>=ts })
	#st.table(df_temp)	
	total =  df[df['Semester'] == sem]['Final Score'].count().compute()
	st.write(total)

with col2:
	st.markdown('#### Number of students with final score >= threshold score:')
	met_threshold = df[(df['Semester'] == sem) & (df['Final Score'] >= ts)]['Final Score'].count().compute()
	st.write(df[(df['Semester'] == sem) & (df['Final Score'] >= ts)]['Final Score'].count().compute())

with col3:
	st.markdown("#### Percentage of students with final score >= threshold score:")
	st.write(np.round(met_threshold*100/total,1))

st.markdown("#### Class average and standard deviation in the selected semester:")
st.write("(", np.round(df[df['Semester'] == sem]['Final Score'].mean().compute(),1), ",", np.round(df[df['Semester'] == sem]['Final Score'].std().compute(),1),")")



st.markdown("#### Grade Distribution in selected semester")
fig = px.histogram(df_temp['Final Score'])
fig.update_xaxes(range=[0, 100])
fig.update_yaxes(range = [0, df['Final Score'].max().compute() + 5])
st.plotly_chart(fig)


ex = st.beta_expander('Expand this to see instructional and teaming features for the selected semester.')
with ex:
  if sem == 'Fall 2017':
    st.markdown(' - First time teaching MEP3')
    st.markdown(' - inclass software demos.')
  elif sem == 'Spring 2018':
    st.markdown('- inclass software demos.')
  elif sem == 'Fall 2018':
    st.markdown(' - First time with fully inverted classroom.')
  elif sem == 'Spring 2019':
    st.markdown(' - Fully inverted classroom.')
    st.markdown(' - First time with Some teams with more than 4 students.')
  elif sem == 'Fall 2019':
    st.markdown('- Fully inverted classroom.' )
    st.markdown(' - Some teams with more than 4 students')
  elif sem == 'Fall 2020':
    st.markdown('- Fully inverted classroom.')
    st.markdown('- Fully remote.')
    st.markdown('- All teams with more than 4 students.')
  elif sem == 'Spring 2021':
    st.markdown('- Fully inverted classroom.')
    st.markdown('- Fully remote.')
    st.markdown('- All teams with more than 4 students.')
    st.markdown('- Significant number of COVID related absences.')
#eof
