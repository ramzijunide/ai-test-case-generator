# ai-test-case-generator
AI-powered test case generator using Groq LLM and Streamlit

#  AI Test Case Generator

An AI-powered test case generator that automatically creates 
structured QA test cases from feature descriptions using 
Groq LLM and Streamlit.

##  Features
- Generate 5 professional test cases instantly from any feature description
- Structured format: TC ID, Title, Precondition, Steps, Expected Result, Status
- Export test cases directly to Excel (.xlsx) with one click
- Clean and simple web interface built with Streamlit

##  Tech Stack
- Python
- Groq LLM (Llama 3.3)
- Streamlit
- Pandas
- OpenPyXL

##  How to Run

1. Clone the repository
   git clone https://github.com/ramzijunide/ai-test-case-generator.git

2. Install dependencies
   pip install -r requirements.txt

3. Create a .env file and add your Groq API key
   GROQ_API_KEY=your_groq_api_key_here

4. Run the app
   streamlit run app.py

##  How It Works
1. Enter a feature description in the text area
2. Click "Generate Test Cases"
3. View the generated test cases
4. Click "Download as Excel" to export

##  Author
Mohammed Ramzim
