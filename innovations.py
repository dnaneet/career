import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
     page_title='Aneet Narendranath\'s Teaching Dashboard'
     #layout="wide"
)



st.title("Aneet Narendranath's Teaching Experience Dashboard")
df = pd.read_csv('innovations-timeline-2.csv')
year_items = df['Year']
st.sidebar.write('I started teaching in the spring semester of 2013.  Since then I have instructed cross-curricular courses and created innovative examples and published some at ASEE conferences.  My current education research is on data driven systematic design of instruction, forecast models of student performance and machine learning algorithms to identify learning groups.')

st.sidebar.markdown("---")
st.sidebar.write("This is an interactive page fully created in Python that showcases my teaching experience, teaching evaluation and innovations, nomination for teaching awards and course descriptions.")
st.sidebar.markdown("Aneet Narendranath (C) 2021")

df_evals = pd.read_csv('TeachingEvals.csv')
#st.dataframe(df_evals)
st.subheader("All Teaching Evaluation Scores Scores")
st.write('Hover on each data point to see the year I instructed this course, the course enrollment and the number of students who responded to a teaching evaluation survey.')
st.write('Heat transfer does not have data available since the paper teaching evaluation has been misplaced.  If memory serves me right, this evaluation was around 4.2 out of 5.0.')
st.write('The bubble size is by enrollment.')

expand_teaching_eval = st.beta_expander(label='Expand me for a description of what these teaching evals represent and university policies governing them')

with expand_teaching_eval:
     st.markdown('##### University policies and notes about teaching evaluations:')
     st.markdown('###### [Faculty handbook teaching evaluation policy](https://www.mtu.edu/faculty-handbook/faculty/chapter3/s3-2/3213/)')
     st.markdown('###### [Center for Teaching and Learning](https://www.mtu.edu/ctl/instructional-resources/student-rating-instrument/)')
     st.markdown('###### [What happens with student teaching evaluations (News Article at Michigan Tech)?](https://mtulode.com/1130/news/what-happens-with-students-course-evaluations/)')


fig = px.scatter(df_evals, x = "Course", y = "Eval Score out of 5.0", hover_data = ["Year", "Enrollment", "Responded"], size = "Enrollment", color = "Course")
st.plotly_chart(fig)

yr_evals = df_evals[["Year"]]
#x_evals = st.selectbox('Select Year', np.unique(yr_evals), key = "innovations")
#df_evals[df_evals['Year']==x][["Course", "Enrollment", "Responded", "Eval Score out of 5.0"]]

st.subheader("Teaching Evaluation Scores by Year")
x = st.selectbox('Select Year', np.unique(year_items) , key = "innovations")

st.dataframe(df_evals[df_evals['Year']==x][["Course", "Enrollment", "Responded", "Eval Score out of 5.0"]])
# fig = px.scatter(df_evals[df_evals['Year']==x], x="Course", y="Eval Score out of 5.0", hover_data=['Enrollment', 'Responded'])
# st.plotly_chart(fig)

# fig3 = go.Figure(data=[go.Table(
#     header=dict(values=list(df_evals[["Course", "Enrollment", "Responded", "Eval Score out of 5.0"]]),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=[df_evals[df_evals['Year']==x]['Course'],
#             df_evals[df_evals['Year']==x]['Enrollment'],
#             df_evals[df_evals['Year']==x]['Responded'],
#             df_evals[df_evals['Year']==x]['Eval Score out of 5.0']],
#             fill_color='lavender',
#             align='left'))
# ])
# #fig3.update_layout(width=900, height=300)
# st.plotly_chart(fig3)

#fig4 = px.histogram(df_evals[df_evals['Year']==x][["Course", "Eval Score out of 5.0"]], x="Course", y="Eval Score out of 5.0")
#st.plotly_chart(fig4)



st.subheader('Summary of instructional innovations & scholarly outcomes by year')
st.dataframe(df[df['Year']==x][["Course", "Activity", "Category", "Scholarly output", "Other Outcome"]].transpose())


#st.dataframe( df[df['Year']==x] )

# fig1 = go.Figure(data=[go.Table(
#     header=dict(values=list(df.columns),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=[df[df['Year']==x]['Year'],
#             df[df['Year']==x]['Course'],
#             df[df['Year']==x]['Activity'],
#             df[df['Year']==x]['Category'],
#             df[df['Year']==x]['Scholarly output'],
#             df[df['Year']==x]['Title'],
#             df[df['Year']==x]['Other Outcome']],
#             fill_color='lavender',
#             align='left'))
# ])


# #fig1.update_layout(width=700, height=350)
# st.plotly_chart(fig1)




st.subheader('Nomination for Instructional Awards by year')
yr = np.array([2016, 2017, 2018, 2019, 2020, 2020]);
nominations = np.array(['Wolfram Innovator Award Nomination',
                        'Best Teacher - Finalist out of 40 faculty', 
                        'Best Teacher - Finalist out of 40 faculty',
                        'Best Teacher - Finalist out of 40 faculty',
                        'Best Teacher - Finalist out of 40 faculty',
                        'Deans Teaching Showcase'])
category = np.array(['Industry', 'Department', 'Department', 'Department', 'Department', 'College'])                        
df_awards = pd.DataFrame({'Year': yr, 'Nomination or Award': nominations, 'Category':category})
st.dataframe(df_awards[df_awards['Year']==x])

# fig2 = go.Figure(data=[go.Table(
#     header=dict(values=list(df_awards.columns),
#                 fill_color='paleturquoise',
#                 align='left'),
#     cells=dict(values=[df_awards[df_awards['Year']==x]['Year'],
#             df_awards[df_awards['Year']==x]['Nomination or Award'],
#             df_awards[df_awards['Year']==x]['Category']],
#             fill_color='lavender',
#             align='left'))
# ])
# #fig2.update_layout(width=500, height=300)
# st.plotly_chart(fig2)


expand = st.beta_expander(label='Expand me for course descriptions')

st.subheader("Course descriptions")
with expand:
     list_of_courses = df_evals[["Course"]]
     c = st.selectbox('Select a course name that featured in one of the tables above', np.unique(list_of_courses))

     if c == "Adv Fluid Mech":
          st.write("This is a graduate course in Fluid Mechanics.  The focus is on partial differential equation based models, analytical and numerical solutions to reduced forms of the Navier-Stokes equations.")
     elif c == "Comp fl Eng":
          st.write("This is an course on Computational Fluids Engineering (CFD with software tools).  The enrollment was composed of both undergraduate and graduate students.  The graduate students had an extra assignment of writing MATLAB code to solve the Burger's equation.")
     elif c == "Comp fl Eng (Grad)":
          st.write("This is an course on Computational Fluids Engineering (CFD with software tools).  The enrollment was composed of both undergraduate and graduate students.  The graduate students had an extra assignment of writing MATLAB code to solve the Burger's equation.")       
     elif c == "Intro Thermo/ETF-1":
          st.write("This is an undergraduate course on introductory thermodynamics. In our curriculum, this is also known as ETF-2 (Energy ThermoFluids 1.")
     elif c == "Heat Transfer":
          st.write("This is an undergraduate course in Heat Transfer.  In our curriculum, this is also known as ETF-2 (Energy ThermoFluids 2.")
     elif c == "Intro to FEM":
          st.write("This is an elective course on the Finite Element Method.  It has both undergraduate students and graduate students enrolled.  There is no difference in instruction or expectation from either level of student.")
     elif c == "MEP II":
          st.write("This is 'Mechanical Engineering Practice - II', a hands-on undergraduate course that focuses on 'theory through practice'.  It is the second of a 4-course sequence and focuses on hands-on experiments, data acquisition and technical communication of energy and momentum conservation principles as applicable to rigid body dynamics and fluid flow (incompressible regime). ")     
     elif c == "MEP III":
          st.write("This is 'Mechanical Engineering Practice - III', a hands-on undergraduate course that focuses on 'theory through practice'.  It is the third of a 4-course sequence and focuses on 'Model Based Design through a collaborative studio setting'.  Teams of 4-6 students work on a semester long project to create a fully functional 3D rigid body computer model of a 'locomotion device' (such as an UAV, Automated Pallet, Amazon Conveyor belt).  Students also perform FEA (static) and Fatigue strength analysis of critical some critical component of the locomotion device they design.")  
     elif c == "Mechanics of Materials":
          st.write("This is an undergraduate course in Strength of Materials.  Starting fall 2021, a cloud computing component will be (has been) introduced in this course.")  
     elif c == "Statics":
          st.write("This is an undergraduate course in Static force balances.")            

col1, col2, col3 = st.beta_columns(3)
with col1:
     st.markdown(':email: [dnaneet@mtu.edu](dnaneet@mtu.edu)')

with col2:
     st.markdown(':handshake: [LinkedIn](https://www.linkedin.com/in/dnaneet/)') 

with col3:
     st.markdown(':books: [Google Scholar](https://scholar.google.com/citations?hl=en&user=uSSO_eAAAAAJ&view_op=list_works&authuser=1&sortby=pubdate)')

st.markdown('[Short lecture on the Convergence, Iteration with help from my GTA (Graduate Tabby Assistant)](https://youtu.be/VZeUe9ZjWb8)')
st.markdown('[Short lecture on the importance of computational thinking](https://youtu.be/y0EJsWmNvFU)')

st.markdown('---')
st.markdown("###### Created with Python by Aneet Narendranath, PhD")
