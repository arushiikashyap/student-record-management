import streamlit as st
import pandas as pd

# Title
st.title("Student Record Management System")

# Initialize student data
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["Roll No", "Name", "Age", "Course"]
    )

# Input fields
st.subheader("Enter Student Details")

roll = st.number_input("Roll Number", min_value=1, step=1)
name = st.text_input("Student Name")
age = st.number_input("Age", min_value=1, step=1)
course = st.text_input("Course")

# CREATE
st.subheader("Add Student")

if st.button("Add Student"):
    if name and course:
        if roll not in st.session_state.students["Roll No"].values:

            new_student = pd.DataFrame(
                [[roll, name, age, course]],
                columns=["Roll No", "Name", "Age", "Course"]
            )

            st.session_state.students = pd.concat(
                [st.session_state.students, new_student],
                ignore_index=True
            )

            st.success("Student Added Successfully!")

        else:
            st.error("Roll Number Already Exists!")

    else:
        st.error("Please Enter Name and Course!")

# READ
st.subheader("Student Records")
st.dataframe(st.session_state.students)

# UPDATE
st.subheader("Update Student")

update_roll = st.number_input(
    "Enter Roll Number to Update",
    min_value=1,
    step=1,
    key="update"
)

new_name = st.text_input("New Name", key="new_name")
new_course = st.text_input("New Course", key="new_course")

if st.button("Update Student"):

    if update_roll in st.session_state.students["Roll No"].values:

        idx = st.session_state.students[
            st.session_state.students["Roll No"] == update_roll
        ].index[0]

        st.session_state.students.loc[idx, "Name"] = new_name
        st.session_state.students.loc[idx, "Course"] = new_course

        st.success("Student Updated Successfully!")

    else:
        st.error("Student Not Found!")

# DELETE
st.subheader("Delete Student")

delete_roll = st.number_input(
    "Enter Roll Number to Delete",
    min_value=1,
    step=1,
    key="delete"
)

if st.button("Delete Student"):

    if delete_roll in st.session_state.students["Roll No"].values:

        st.session_state.students = st.session_state.students[
            st.session_state.students["Roll No"] != delete_roll
        ]

        st.success("Student Deleted Successfully!")

    else:
        st.error("Student Not Found!")