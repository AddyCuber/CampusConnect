from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])

    # Check if the response is a GenerateContentResponse
    if hasattr(response, 'parts'):
        # Extract text from all parts
        text_parts = []
        for part in response.parts:
            if hasattr(part, 'text'):
                text_parts.append(part.text)
        return ' '.join(text_parts)
    elif hasattr(response, 'text'):
        # If it's a simple text response
        return response.text
    else:
        # If we can't extract text, return an error message
        return "Error: Unable to parse the model's response."
## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has two tables: TECH_CLUBS and STUDENTS.

    TECH_CLUBS table columns:
    ID, NAME, DESCRIPTION, YEAR_INAUGURATED, PAST_EVENTS, BUDGET, UPCOMING_EVENTS, HOW_TO_ENROLL

    STUDENTS table columns:
    StudentID, Name, Year, Semester, Division, Subject, Marks, GPA, CGPA

    For example:
    Example 1 - How many tech clubs are there?, 
    the SQL command will be: SELECT COUNT(*) FROM TECH_CLUBS;

    Example 2 - What are the names of all the clubs?, 
    the SQL command will be: SELECT NAME FROM TECH_CLUBS;

    Example 3 - Which club has the highest budget?,
    the SQL command will be: SELECT NAME, BUDGET FROM TECH_CLUBS ORDER BY BUDGET DESC LIMIT 1;

    Example 4 - How many students are in the first year?,
    the SQL command will be: SELECT COUNT(DISTINCT StudentID) FROM STUDENTS WHERE Year = 1;

    Example 5 - What is the average GPA of students in the Computer Architecture course?,
    the SQL command will be: SELECT AVG(GPA) FROM STUDENTS WHERE Subject = 'Computer architecture';

    The SQL code should not have ``` in the beginning or end and should not include the word 'sql' in the output.
    """
]

## Streamlit App

st.set_page_config(page_title="Campus Connect")
st.header("Club Connect")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    try:
        response = get_gemini_response(question, prompt)
        print("Generated SQL query:", response)  # For debugging

        if response.startswith("Error"):
            st.error(response)
        else:
            results = read_sql_query(response, "clubs.db")
            st.subheader("The Response is")
            if results:
                # Create a DataFrame from the results
                import pandas as pd

                df = pd.DataFrame(results)
                st.table(df)
            else:
                st.write("No results found.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
