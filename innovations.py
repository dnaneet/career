import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
#from tabulate import tabulate

st.set_page_config(
     page_title='Aneet Narendranath\'s Dashboard of Career Accomplishments and Intellectual Products'
     #layout="wide"
)



df = pd.read_csv('innovations-timeline-2.csv')
df = df.assign(hack='').set_index('hack')
year_items = df['Year']

df_evals = pd.read_csv('TeachingEvals.csv')
df_evals[["Eval Score out of 5.0"]] = df_evals[["Eval Score out of 5.0"]]
df_evals = df_evals.assign(hack='').set_index('hack')

im = Image.open("career-progression.png")
piimg = Image.open("pi.jpg")
loginimg = Image.open("log-in.png")
feedingimg = Image.open("feeding-habits.png")
harppiimg = Image.open("harppi.png")
entimg = Image.open("ent-stages.png")

selection = st.sidebar.radio('Select ', ["Career Highlights", "Teaching and associated media samples", "Research Output and associated media samples", "Entrepreneurial Activity", "Extra-Curricular Activities with intellectual value"])
st.sidebar.markdown("---")
st.sidebar.write("This web-app showcases my teaching experience, innovations, nomination for teaching awards, research output, entrepreneurial efforts, and extra-curricular activities.")
st.sidebar.markdown("###### Created in Python with Streamlit.")
st.sidebar.markdown("###### Aneet Narendranath, PhD., Associate Teaching Professor")
st.sidebar.markdown("---")


if selection == "Career Highlights":
     st.title("Highlights of my Teaching, Research, Equity and Entrepreneurship")
     st.write("This page captures the highlights of my efforts since 2013 at Michigan Technological University.  Please visit in-depth pages on teaching, research and entrepreneurship by accessing the radio-buttons in the collapsible sidebar to the left.")
     st.markdown("## 🧑‍🏫 Cross-curricular Teaching with focus on collaborative problem-solving studios")
     st.write("I teach 3-4 sections of courses, per semester, across the Mechanical engineering curriculum. Through the courses I teach, I engage 150-250 students across a Mechanical Engineering curriculum in a year. Since 2019, I have begun to shed a traditional classroom (inert lecturing -- which I found to be ineffective for large enrollments) approach in favour of collaborative design studios, inverted classrooms, and data-driven course design.")
     
     st.markdown("## :microscope: Multidisciplinary Research")
     st.write("I am research-active non tenure-track faculty.  I publish 1-2 peer-reviewed papers in education research and on fundamental scientific researh in peer-reviewed national and international conferences and journals.  My current focus is Quantitative Learning Analytics and I am actively working on numerical models and machine learning tools to support systematic design of instruction, assessment data pipelines, and forecast models of student performance.")

     st.markdown("## :chart_with_upwards_trend: Data-driven staffing to ensure salary equity at the Engineering Learning Center")
     st.write("I currently manage a peer-tutoring center (Engineering Learning Center) in our Mechanical engineering department.  In fall 2021, through the application of usage data gathered over the last 3 years and the Scrum project management framework, I am restoring equity in salaries for our tutors while ensuring that their short-term academic and career-oriented goals are met.  The ELC coaches were paid 30-40% less than their peers at other learning centers and teaching assistants while shouldering similar responsibilities.")

     st.markdown("## :sparkles: Entrepreneurial work")
     st.write("In January 2021, I co-founded a tech startup with a focus on simulation sandboxes.  We were awarded a technology grant by Wolfram Research Inc.  We are currently purusing seed grants to build the scope of our technology.  In fall 2021, we engaged with a Senior Capstone Design course to supporting a *Digital Engineering* project at a mid-western university in North America.  We are currently in conversations to set-up a short-term *pop-up simulation environment studio* with another university.")
elif selection == "Teaching and associated media samples":
     st.title("Aneet Narendranath's Teaching Experience Dashboard")
     st.markdown('### 📺 Media samples of my instructional videos')
     st.markdown('These two media samples were created in summer 2021 towards a Computational thinking starter-pack for the Mechanical Engineering course on Mechanics of Materials.  These videos were shot by Lake Superior.  The location was chosen so as to remove the notion that instruction focused on computing should always have a computer screen as the focal point.')
     st.markdown('[Video: 2 minute vignette on the Convergence, Iteration with help from my GTA (Graduate Tabby Assistant)](https://youtu.be/VZeUe9ZjWb8)')
     st.markdown('[Video: 45 second vignette on the importance of computational thinking](https://youtu.be/y0EJsWmNvFU)')
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
elif selection == "Research Output and associated media samples":
     st.title("Aneet Narendranath's Research Output Dashboard")
     st.markdown('### :tv: Media from public speaking at the Wolfram Technology conference')
     st.markdown('The two media files linked below are my live-code notebook demonstration sessions captured at the Wolfram Technology conference in 2016 and 2019 respectively.  These videos are on two different topics: one on classical fluid dynamics and simulations and the other on cutting-edge Machine Learning as a replacement for Thermodynamic Steam Tables.  These have spawned multiple papers and presentations.')
     st.markdown("[Video: Dynamics of liquid films in microgravity](https://www.youtube.com/watch?v=qTCwmUuM-Gg)")
     st.markdown("[Video: Approximating Steam Properties with a Neural Network](https://www.youtube.com/watch?v=xngHOVYZ1ak)")     
     st.markdown("Computing and numerical solutions are the pillars of my research career.  I have research experience spanning multiple length and time-scales as described in [this map](https://raw.githubusercontent.com/dnaneet/career/main/career-progression.png) of my activities.")
     st.image(im, use_column_width="always")
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
     expand_proposals = st.expander(label='Expand me for a list of internal grants received and external proposals co-authored.')

     with expand_proposals:
          st.markdown('###### Internal Grants Received as PI:')
          st.markdown("I received internal grants for successful proposals that were reviewed by our external advisory board members.  The process was competitive.  The focus of my internal proposals has been Learning Analytics.")
          """
           - MEEM [External Advisory Board](https://www.mtu.edu/mechanical/people/advisory-board/) of corporate members fund: Assessment and Learning Analytics Dashboard for deployment in the Mechanical Engineering curriculum at Michigan Tech, September 2021.
           - MEEM EAB fund: Machine learning applied to student simulations to discover computation thinking attributes, September 2019.
           - [Summer undergraduate research fellowship](https://www.mtu.edu/honors/research/surf/): Reducing hull drag in conventional watercraft through an induced cavitation field.
           """
          st.markdown("###### External Proposals co-authored (Spronsored Programs) as co-PI")
          st.markdown("My primary responsibility was numerical simulations and creation of algorithms for active control of hydrodynamic instabilities, in these proposals.")
          """
            - NSF Collaborative Research: Heat transfer and convective structure evolution in transient, evaporating thin films, 2021. 
            - NSF Collaborative Research: Interfacial Instability and Convective Structure Evolution in Evaporating Films, 2019.
            - NSF Collaborative Research: Instability  Convective Structure and Heat Transfer in Evaporating Films in Microgravity, 2018.
            - NSF Collaborative Research: Interfacial Stability and Evolution of Convective Structure in Evaporating Films under Non-Stationary Conditions, 2017.
          """

     
     expand_student_advising = st.expander(label='Expand me for student advising activity.')
     with expand_student_advising:
          st.markdown("###### Fall 2021 and Spring 2022")
          st.markdown("I am currently advising an undergraduate student on a year long project on developing **Key Performance Indicators** for a Scrum-framework supported peer-learning tutoring center. The outcome of this project is an empirical identification of the dependent and independent variables in a peer-driven learning/teaching process.")  

          st.markdown("###### Summer 2021")
          st.markdown("I advised a graduate student on a short term research project with a focus on creating a **cloud-deployed Learning Analytics dashboard**.  This project was 15 hours in duration and used Scrum to incrementally develop a Learning Analytics forecast tool dashboard-solution that can be cloud deployed. The student is currently enrolled in the graduate school at Michigan Technological University and is pursuing a PhD in Combustion Science. The following research output was produced from this endeavour:")
          """
           - S. Gopujkar, A.D. Narendranath, "Building a Suite of Learning Analytics Tools for STEM Education" (Live Learning Analytics code demonstration), *Future of Education* Track at the Wolfram Technology Conference 2021 (October 6--12, 2021)
          """

          st.markdown("###### Summer 2020")
          st.markdown("I advised an undergraduate student in a successful [summer undergraduate research fellowship](https://www.mtu.edu/honors/research/surf/) on a **Scientific Machine Learning model for the control of drag on watercraft**.  The student is currently enrolled as a graduate student at Purdue university and is pursuing a Master's degree. The following research output was produced from this endeavour:")
          """
           - C.Grande, A.D. Narendranath, "Reducing Hull Drag in Conventional Watercraft through an Induced Cavitation Field: A Numerical/Predictive Approach", ASME IMECE 2020 Poster.
          """

elif selection == "Entrepreneurial Activity":
     st.title("Aneet Narendranath's Entrepreneurial Activity Dashboard")
     st.markdown("In January 2021, I co-founded Voxel Science LLC.  A Michigan based technology startup focused on simulation sandboxes with real time interactivity.  In March 2021 Voxel Science LLC received a [start-up technology grant](https://www.wolfram.com/startups/) from Wolfram Research Inc.  The stages of our evolution are described in the image below.  There exists an internal feedback loop between the 'Validate' and 'Demonstrate' stage.")
     st.write("")
     st.markdown("  ")
     st.image(entimg, use_column_width="always")
     st.markdown("---")
     st.write("Due to potential IP, descriptions of our digital products are not immediately available for public perusal.")
elif selection == "Extra-Curricular Activities with intellectual value":
     st.title("Aneet Narendranath's Extra-Curricular activities")	
     st.subheader("📊 A Raspberry-Pi learning center usage tracker")
     st.image(piimg, use_column_width="always")
     st.image(loginimg, use_column_width="always")
     st.markdown("I wrote a [bash-script](https://github.com/dnaneet/learning-center-management) that ran on a [Raspberry Pi Zero](https://raw.githubusercontent.com/dnaneet/career/main/pi.jpg) and tracked the usage of a peer-supported engineering tutoring center (learning center).  This was created for a cost of approximately $100 and replaced a system that cost several thousand-dollars a year.")
     st.write("The Mag-Pi interviewed me about this initiative.  This interview may be found via [Mag-Pi Number 65](https://www.raspberrypi.org/magpi-issues/MagPi65.pdf).")
     st.markdown("#### Intellectual value")
     st.write("This project kick-started a focus on data driven decision making for a peer-supported learning center.  It recently catalyzed my data-driven solutions to salary inequity experienced by my student employees.")
     st.markdown("----")
     st.subheader("🎵 Tracking the seasonal temperature and humidity variations around a Lyon and Healy Harp")
     st.markdown("I created a Python script that was deployed on a Raspberry Pi mounted with a Pi-Hat.  The hardware mounting and soldering was performed by my spouse who is a professional harpist.  The objective of this widget was to track the temperature and relative-humidity in the immediate vicinity of an expensive [Lyon and Healy harp](https://raw.githubusercontent.com/dnaneet/career/main/harppi.png).  Sadly, the live data-visualization component of this project is defunct due to a change in GitHub's hosting policies.  However, we continue to collect data using this widget and have accummulated temperature and relative-humidity data, at 5 minute intervals for 4 consecutive years!")
     st.image(harppiimg, use_column_width='always')
     st.markdown("#### Intellectual value")
     st.write("Harps are expensive musical instruments and require specialized care that we do not have access to.  Collecting 'comfort' data for my spouse's harp has allowed us to optimally deploy humidifiers and dehumidifiers to protect the structural integrity of the instrument.  Emergency round-trips to Lyon and Healy in Chicago, may have been averted by our approach.")
     st.markdown("----")
     st.subheader("🐈 Data-drive assistance for the treatment of my cat's ailment")
     st.markdown("In summer 2021, my cat was stricken by a severe case of IBD possibly due to Intestinal Lymphoma.  It was imperative that I tracked the feeding habits, patterns and quality of life of my cat so as to prolong her life through focused medical support.  I have been collecting data (manually for now) on various parameters of my cat's feeding habits and her response to an oral steroid.")  
     """
     ### Through visual analysis of the collected data, I made the following non-medical observations to help support the veterinarian
     Unordered List:
     - The oral steroid activates her appetite approximately 50% better than without it.  This is as expected by the veterinarian.
     - A dramatic change in her feeding habits has occurred. She moved from eating larger volumes (1-oz of solid food) per feeding to trickle feeding through the day.   
     - Although the volume of 'Nutrisource' brand of cat food consumed by my cat is greater than 'Taste of the Wild', her daily caloric intake has not changed between these two brands.  'Nutrisource' is less calorie-dense as compared to 'Taste of the Wild.'
     """
     st.markdown("#### Intellectual value")
     st.write("My cat's veterinarian informs me that never has such a detail on a cat's feeding been captured in literature.  A sample of the visualization of my cat's feeding habits may be found via [this link](https://raw.githubusercontent.com/dnaneet/career/main/feeding-habits.png).  When time permits, I plan on scaling my effort to an open-source app in collaboration with our veterinarian.")
     st.image(feedingimg, use_column_width='always')
     st.write("Although I have invested time and energy in collecting data on my cat's feeding behaviors, she is not a science project!  She is a valued member of my family to whom I owe a long and healthy life.")


col1, col2, col3 = st.columns(3)
with col1:
     st.markdown('### :email: [dnaneet@mtu.edu](dnaneet@mtu.edu)')

with col2:
     st.markdown('### :handshake: [LinkedIn](https://www.linkedin.com/in/dnaneet/)') 

with col3:
     st.markdown('### :books: [Google Scholar](https://scholar.google.com/citations?hl=en&user=uSSO_eAAAAAJ&view_op=list_works&authuser=1&sortby=pubdate)')


st.markdown('---')
st.markdown("###### Created with Python by Aneet Narendranath, PhD")
