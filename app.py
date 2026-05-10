import streamlit as st
from groq import Groq
import pandas as pd
import io

import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title(" AI Test Case Generator")
st.write("Enter a feature description and get test cases instantly!")

feature = st.text_area(
    "Describe the feature you want to test:",
    placeholder="Example: Login page with email and password fields..."
)

def parse_test_cases(text):
    cases = []
    blocks = text.strip().split("\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        tc = {
            "TC ID": "",
            "Title": "",
            "Precondition": "",
            "Steps": "",
            "Expected Result": "",
            "Status": ""
        }
        for line in lines:
            if line.startswith("TC_"):
                tc["TC ID"] = line.strip()
            elif line.startswith("Title:"):
                tc["Title"] = line.replace("Title:", "").strip()
            elif line.startswith("Precondition:"):
                tc["Precondition"] = line.replace("Precondition:", "").strip()
            elif line.startswith("Steps:"):
                tc["Steps"] = line.replace("Steps:", "").strip()
            elif line.startswith("Expected Result:"):
                tc["Expected Result"] = line.replace("Expected Result:", "").strip()
            elif line.startswith("Status:"):
                tc["Status"] = line.replace("Status:", "").strip()
        if tc["TC ID"] or tc["Title"]:
            cases.append(tc)
    return cases

if st.button("Generate Test Cases"):
    if feature.strip() == "":
        st.warning("Please enter a feature description!")
    else:
        with st.spinner("Generating test cases..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": """You are a professional QA Engineer. 
                        When given a feature description, generate detailed test cases.
                        Format each test case exactly as:
                        TC_001
                        Title: 
                        Precondition: 
                        Steps: 
                        Expected Result: 
                        Status: Pass/Fail"""
                    },
                    {
                        "role": "user",
                        "content": f"Generate 5 test cases for: {feature}"
                    }
                ]
            )
            result = response.choices[0].message.content
            st.session_state.result = result

if "result" in st.session_state:
    st.success("Test cases generated!")
    st.text_area("Generated Test Cases:", st.session_state.result, height=400)

    # Excel download button
    cases = parse_test_cases(st.session_state.result)
    if cases:
        df = pd.DataFrame(cases)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Test Cases")
        buffer.seek(0)
        st.download_button(
            label=" Download as Excel",
            data=buffer,
            file_name="test_cases.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )