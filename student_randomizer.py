import random
import streamlit as st
from streamlit_tags import st_tags


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


st.title("Student Randomizer")
st.header("by: A. Vera")
st.write("Use this app to randomly assign students in your classroom into teams.")
st.write('Type the names of your students in the provided space below, up-to 100 students.')

students = st_tags(label="Enter the names of your students here:", text="Press enter to add more", maxtags=100)


number_of_teams = st.number_input("Number of teams to create:", min_value=2, max_value=50, help="Make sure that the number of groups you select is less than the number of students.")


def make_random_groups(students, number_of_teams):
    if st.button("Generate Teams"):
    
        #Shuffle list of students
        random.shuffle(students)
    
        #Create groups
        all_teams = []
        for index in range(number_of_teams):
            group = students[index::number_of_teams]
            all_teams.append(group)
    
        #Format and display groups
        for index, group in enumerate(all_teams):
            f"👤Team {index+1}👤: {' / '.join(group)}\n"


make_random_groups(students, number_of_teams)







