import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
#from PIL import Image
#from tabulate import tabulate

st.set_page_config(
     page_title='Aneet Narendranath\'s Academic Experience and Achievements Dashboard'
     #layout="wide"
)



df = pd.read_csv('innovations-timeline-2.csv')
df = df.assign(hack='').set_index('hack')
year_items = df['Year']

df_evals = pd.read_csv('TeachingEvals.csv')
df_evals[["Eval Score out of 5.0"]] = df_evals[["Eval Score out of 5.0"]]
df_evals = df_evals.assign(hack='').set_index('hack')

#im = Image.open("career-progression.png")
#piimg = Image.open("pi.jpg")
#loginimg = Image.open("log-in.png")
#feedingimg = Image.open("feeding-habits.png")
#harppiimg = Image.open("harppi.png")

selection = st.sidebar.radio('Select ', ["Highlights", "Teaching", "Research", "Entrepreneurial", "ExtraCurricular"])
st.sidebar.markdown("---")
st.sidebar.write("This interactive page fully created in Python showcases my teaching experience, innovations, nomination for teaching awards, research output, entrepreneurial efforts, and extra-curricular activities.")
st.sidebar.markdown("Aneet Narendranath (C) 2021")
st.sidebar.markdown("---")


if selection == "Highlights":
     st.title("Highlights of my Teaching, Research, Equity and Entrepreneurship")
     st.write("This page captures the highlights of my efforts since 2013 at Michigan Technological University.  Please visit in-depth pages on teaching, research and entrepreneurship by accessing the radio-buttons in the collapsible sidebar to the left.")
     st.markdown("## 🧑‍🏫 Cross-curricular Teaching with focus on collaborative problem solving studios")
     st.write("I teach 3-4 sections of courses, per semester, across the Mechanical engineering curriculum.  Since 2019, I have begun to shed a traditional classroom (inert lecturing) approach in favour of the inverted classroom, emphasis on 1-on-1 time, and collaborative design studios.")
     
     st.markdown("## :microscope: Multidisciplinary Research")
     st.write("I am research-active non tenure-track faculty.  I publish 1-2 peer-reviewed papers in education research and on fundamental scientific researh in peer-reviewed national and international conferences and journals.  My current focus is Quantitative Learning Analytics and I am actively working on numerical models and machine learning tools to support systematic design of instruction, assessment data pipelines, and forecast models of student performance.")

     st.markdown("## :chart_with_upwards_trend: Data-driven staffing at the Engineering Learning Center")
     st.write("I currently manage a peer-tutoring center (Engineering Learning Center) in our Mechanical engineering department.  In fall 2021, through the application of usage data gathered over the last 3 years and the Srum project management framework, I am restoring equity in salaries for our tutors while ensuring that their short-term academic and career-oriented goals are met when they work at our peer-tutoring center.  The ELC coaches were being paid 30% less than their peers at other learning centers (due to different amount of funds available).")

     st.markdown("## :sparkles: Entrepreneurial work")
     st.write("In January 2021, I co-founded a tech startup with a focus on simulation sandboxes.  We were awarded a technology grant by Wolfram Research Inc.  We are currently purusing seed grants to build the scope of our technology.  In fall 2021, we engaged with a Senior Capstone Design course to supporting a *Digital Engineering* project at a mid-western university in North America.  We are currently in conversations to set-up a short-term *pop-up simulation environment studio* with another university.")
elif selection == "Teaching":
     st.title("Aneet Narendranath's Teaching Experience Dashboard")
     #st.dataframe(df_evals)
     st.markdown("## :bar_chart: All Teaching Evaluation Scores")
     st.write('My teaching evaluation compound scores may be interactively visualized via this chart.')
     st.write('Hover on each data point to see the year I instructed this course, the course enrollment and the number of students who responded to a teaching evaluation survey.  Some of the bubbles provide additional context through an added Note.  You may zoom into data points by  clicking and dragging around them.')
     st.write('The bubble size signifies enrollment.  Some bubbles are on top of each other since they represent the exact same teaching evaluation score but in different semesters.')

     expand_teaching_eval = st.expander(label='Expand me for a description of how my university uses these teaching evals.')

     with expand_teaching_eval:
          st.markdown('##### University policies and notes about teaching evaluations:')
          st.markdown('###### [Faculty handbook teaching evaluation policy](https://www.mtu.edu/faculty-handbook/faculty/chapter3/s3-2/3213/)')
          st.markdown('###### [Center for Teaching and Learning](https://www.mtu.edu/ctl/instructional-resources/student-rating-instrument/)')
          st.markdown('###### [What happens with student teaching evaluations (News Article at Michigan Tech)?](https://mtulode.com/1130/news/what-happens-with-students-course-evaluations/)')


     fig = px.scatter(df_evals, x = "Course", y = "Eval Score out of 5.0", hover_data = ["Year", "Semester", "Enrollment", "Responded", "Note"], size = "Enrollment", color = "Course")
     fig.update_yaxes(range=[0,5])
     st.plotly_chart(fig)

     yr_evals = df_evals[["Year"]]
     #x_evals = st.selectbox('Select Year', np.unique(yr_evals), key = "innovations")
     #df_evals[df_evals['Year']==x][["Course", "Enrollment", "Responded", "Eval Score out of 5.0"]]

     st.markdown("## :date: Teaching Evaluation Scores by Year")
     x = st.selectbox('Select Year', np.unique(year_items) , key = "innovations")

     st.table(df_evals[df_evals['Year']==x][["Course", "Semester", "Enrollment", "Responded", "Eval Score out of 5.0", str("Note")]])

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


     st.markdown('### :bulb: Summary of instructional innovations & scholarly outcomes by year')
     st.table(df[df['Year']==x][["Course", "Activity", "Category", "Scholarly output", "Other Outcome"]])

     # st.write(str(df[df['Year']==x][["Course"]]).split()[-1])

     # temp_activity = str(df[df['Year']==x][["Activity"]]).split()
     # activity = ' '.join(temp_activity[2:])
     # st.write("Activity: ", activity)

     # temp_category = str(df[df['Year']==x][["Category"]]).split()
     # category = ' '.join(temp_category[2:])
     # st.write("Category: ", category)

     # temp_sch = str(df[df['Year']==x][["Scholarly output"]]).split()
     # sch = ' '.join(temp_sch[2:len(temp_sch)-1])
     # st.write("Scholarly outcome: ", sch)

     # temp_other = str(df[df['Year']==x][["Other Outcome"]]).split()
     # other = ' '.join(temp_other[2:len(temp_other)-1])
     # st.write("Scholarly outcome: ", other)


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




     st.markdown('## :trophy: Nomination for Instructional Awards by year')
     yr = np.array([2016, 2017, 2018, 2019, 2020, 2020]);
     nominations = np.array(['Wolfram Innovator Award Nomination',
                         'Best Teacher - Finalist out of 40 faculty', 
                         'Best Teacher - Finalist out of 40 faculty',
                         'Best Teacher - Finalist out of 40 faculty',
                         'Best Teacher - Finalist out of 40 faculty',
                         'Deans Teaching Showcase'])
     category = np.array(['Industry', 'Department', 'Department', 'Department', 'Department', 'College'])                        
     df_awards = pd.DataFrame({'Year': yr, 'Nomination or Award': nominations, 'Category':category})
     df_awards = df_awards.assign(hack='').set_index('hack')

     st.table(df_awards[df_awards['Year']==x])

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

     st.markdown("### :information_source: Course descriptions")
     expand = st.expander(label='Expand me for course descriptions')
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
     st.markdown('[Video: 2 minute vignette on the Convergence, Iteration with help from my GTA (Graduate Tabby Assistant)](https://youtu.be/VZeUe9ZjWb8)')
     st.markdown('[Video: 45 second vignette on the importance of computational thinking](https://youtu.be/y0EJsWmNvFU)')                   
elif selection == "Research":
     st.title("Aneet Narendranath's Research Output Dashboard")
     st.write("Computing and numerical solutions are the pillars of my research career.  I have research experience spanning multiple length and time-scales as described in this map of my activities.")
     #st.image(im, use_column_width="always")
     st.title("Aneet Narendranath's Research Output Dashboard")
     #st.write("In the years 2016 and 2019 my presentation at the Wolfram technology conference were recorded as media and published online.")
     #st.write("My research focus has been on numerical methods for nonlinear problems in technology and quantitative methods in assessment in STEM.")
     df_research = pd.read_csv('ResearchCitations.csv')     
     df_research = df_research.assign(hack='').set_index('hack')
     df_research = df_research.replace({np.NAN: None})
     years_research = np.unique(df_research[["Year"]])
     select_year = st.selectbox('Select year', years_research)
     #st.table(df_research[["Authors", "Year", "Title", "Publication", "Media"]].sort_values(by = ["Year"], ascending = False))
     st.table(df_research[df_research['Year']==select_year][["Authors", "Year", "Title", "Publication", "Media"]])
     st.markdown("[Video: Dynamics of liquid films in microgravity](https://www.youtube.com/watch?v=qTCwmUuM-Gg)")
     st.markdown("[Video: Approximating Steam Properties with a Neural Network](https://www.youtube.com/watch?v=xngHOVYZ1ak)")
elif selection == "Entrepreneurial":
     st.title("Aneet Narendranath's Entrepreneurial Activity Dashboard")
     st.write("In January 2021, I co-founded Voxel Science LLC.  A Michigan based technology startup focused on simulation sandboxes with real time interactivity.")
     st.write("In March 2021 Voxel Science LLC received a technology grant from Wolfram Research Inc.")
     st.markdown("---")
     st.write("Due to potential IP, descriptions of our digital products are not immediately available for public perusal.")
elif selection == "ExtraCurricular":
     st.title("Aneet Narendranath's Extra-Curricular activities")	
     st.subheader("A Raspberry-Pi learning center usage tracker")
     #st.image(piimg, use_column_width="always")
     #st.image(loginimg, use_column_width="always")
     st.write("I wrote a bash-script that tracked the usage of a peer-supported engineering tutoring center (learning center).  This was created for a cost of approximately $100 and replaced a system that cost several thousand-dollars a year.")
     st.write("The Mag-Pi interviewed me about this initiative.  This interview may be found via [Mag-Pi Number 65](https://www.raspberrypi.org/magpi-issues/MagPi65.pdf).")
     st.subheader("Tracking the seasonal temperature and humidity variations around a Lyon and Healy Harp")
     st.write("I created a Python script that was deployed on a Raspberry Pi mounted with a Pi-Hat.  The hardware mounting and soldering was performed by my spouse who is a professional harpist.  The objective of this widget was to track the temperature and relative-humidity around an expensive Lyon and Healy harp.  Sadly, this project is defunct now as I have not had the time to invest in changing the web-hosting nuances.  However, we continue to collect data using this widget and have accummulated temperature and relative-humidity data, at 5 minute intervals for 4 consecutive years!")
     #st.image(harppiimg, use_column_width='always')
     st.subheader("Python code to visualize feeding habits of my cat")
     st.write("In summer 2021, my cat was stricken by a severe case of IBD possibly due to intestinal lymphoma.  It was imperative that I tracked the feeding habits, patterns and quality of life of my cat so as to prolong her life through focused medical support.  I have been collecting data (manually for now) on various parameters of my cat's feeding habits and her response to an oral steroid.  We discovered that the oral steroid activates her appetite approximately 50% better than without it.  An additional discovery of a dramatic change in her feeding habits was discovered.  Pre-2021, my cat was feeding on 1-oz of solid food in the day time and 1-oz in the night.  In 2021, her feeding habits have changed to her being a trickle-feeder.  She now ingests 4-6 meals, each of 0.2 to 0.3-oz of food. My cat's veterinarian informs me that never has such a detail on a cat's feeding been captured in literature.  When time permits, I plan on scaling my effort to an open-source app with the permission and collaboration of our veterinarian.")    
    # st.image(feedingimg, use_column_width='always')


col1, col2, col3 = st.columns(3)
with col1:
     st.markdown('### :email: [dnaneet@mtu.edu](dnaneet@mtu.edu)')

with col2:
     st.markdown('### :handshake: [LinkedIn](https://www.linkedin.com/in/dnaneet/)') 

with col3:
     st.markdown('### :books: [Google Scholar](https://scholar.google.com/citations?hl=en&user=uSSO_eAAAAAJ&view_op=list_works&authuser=1&sortby=pubdate)')


st.markdown('---')
st.markdown("###### Created with Python by Aneet Narendranath, PhD")
