from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from PIL import Image
import pdf2image
from openai import OpenAI
import io
import base64
import requests
import json
from urllib.parse import urlencode
import plotly.graph_objects as go
import plotly.express as px

# Configure OpenAI
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    st.error("❌ OPENAI_API_KEY not found in environment variables. Please add it to your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# Google OAuth Configuration
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
    st.error("❌ Google OAuth credentials not found. Please add GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET to your .env file.")
    st.stop()

# Google OAuth URLs
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"

def create_circular_progress(percentage, title="RESUME MATCH"):
    """Create a beautiful circular progress indicator"""
    
    # Determine color based on percentage
    if percentage >= 80:
        color = "#00FF00"  # Bright green
        status = "EXCELLENT"
    elif percentage >= 60:
        color = "#90EE90"  # Light green
        status = "GOOD"
    elif percentage >= 40:
        color = "#FFD700"  # Gold
        status = "FAIR"
    elif percentage >= 20:
        color = "#FFA500"  # Orange
        status = "POOR"
    else:
        color = "#FF0000"  # Red
        status = "TERRIBLE"
    
    # Create circular progress chart
    fig = go.Figure()
    
    fig.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=percentage,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24, 'color': '#2E4053'}},
        delta={'reference': 100},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#2E4053"},
            'bar': {'color': color, 'thickness': 0.3},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#2E4053",
            'steps': [
                {'range': [0, 20], 'color': '#FFE6E6'},
                {'range': [20, 40], 'color': '#FFF2E6'},
                {'range': [40, 60], 'color': '#FFF9E6'},
                {'range': [60, 80], 'color': '#E6F7E6'},
                {'range': [80, 100], 'color': '#E6FFE6'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font={'color': "#2E4053", 'family': "Arial Black, Arial, sans-serif"},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig, status, color

def get_insult_and_meme(percentage):
    """Get a fun insult and meme for low scores"""
    if percentage < 50:
        insults = [
            "Your resume is so weak, even a paperclip could beat it in a fight! 📎",
            "This resume has fewer skills than a potato has eyes! 🥔",
            "Your resume is like a blank canvas - except it's not art, it's just empty! 🎨",
            "This resume is so basic, it makes 'Hello World' look like rocket science! 🚀",
            "Your resume is like a restaurant with no menu - confusing and disappointing! 🍽️"
        ]
        
        memes = [
            "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",  # Confused dog
            "https://media.giphy.com/media/3o7TKoWXm3okO1kgHC/giphy.gif",  # Facepalm
            "https://media.giphy.com/media/3o7TKDEq4w6beWElI4/giphy.gif",  # Crying
            "https://media.giphy.com/media/3o7TKDEq4w6beWElI4/giphy.gif",  # Disappointed
            "https://media.giphy.com/media/3o7TKDEq4w6beWElI4/giphy.gif"   # Sad
        ]
        
        import random
        return random.choice(insults), random.choice(memes)
    return None, None

def get_openai_response(input_text, pdf_content, prompt):
    try:
        # Create the message with the prompt and context
        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Job Description: {input_text}\n\nPlease analyze the resume and provide feedback."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{pdf_content[0]['data']}"
                        }
                    }
                ]
            }
        ]
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def extract_percentage_from_response(response):
    """Extract percentage from AI response"""
    import re
    # Look for percentage patterns like "85%", "85 percent", etc.
    percentage_patterns = [
        r'(\d+)%',
        r'(\d+)\s*percent',
        r'(\d+)\s*per\s*cent',
        r'match.*?(\d+)',
        r'(\d+).*?match'
    ]
    
    for pattern in percentage_patterns:
        match = re.search(pattern, response.lower())
        if match:
            percentage = int(match.group(1))
            return min(max(percentage, 0), 100)  # Ensure it's between 0-100
    
    # If no percentage found, try to estimate based on keywords
    response_lower = response.lower()
    if any(word in response_lower for word in ['excellent', 'perfect', 'outstanding', 'amazing']):
        return 90
    elif any(word in response_lower for word in ['good', 'strong', 'solid', 'well']):
        return 75
    elif any(word in response_lower for word in ['fair', 'average', 'decent', 'okay']):
        return 50
    elif any(word in response_lower for word in ['poor', 'weak', 'bad', 'terrible']):
        return 25
    else:
        return 50  # Default to 50%

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # converting the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        
        first_page = images[0]
        
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Main App
st.set_page_config(page_title="ATS RESUME SCORE-CHECKER", layout="wide")

# Authentication Section
st.header("🔐 ATS RESUME SCORE-CHECKER")

# Check if user is authenticated
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("Please login to continue")
    
    # Google Login Button
    if st.button("🔑 Login with Google", type="primary"):
        # Create authorization URL
        params = {
            'client_id': GOOGLE_CLIENT_ID,
            'redirect_uri': 'http://localhost:8503',
            'scope': 'openid email profile',
            'response_type': 'code',
            'access_type': 'offline'
        }
        
        auth_url = f"{GOOGLE_AUTH_URL}?{urlencode(params)}"
        st.markdown(f"[Click here to login with Google]({auth_url})")
    
    # Handle OAuth callback
    query_params = st.query_params
    if 'code' in query_params:
        code = query_params['code']
        
        # Exchange code for token
        token_data = {
            'client_id': GOOGLE_CLIENT_ID,
            'client_secret': GOOGLE_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': 'http://localhost:8503'
        }
        
        try:
            token_response = requests.post(GOOGLE_TOKEN_URL, data=token_data)
            token_response.raise_for_status()
            token_info = token_response.json()
            
            # Get user info
            headers = {'Authorization': f"Bearer {token_info['access_token']}"}
            user_response = requests.get(GOOGLE_USERINFO_URL, headers=headers)
            user_response.raise_for_status()
            user_info = user_response.json()
            
            # Store user info in session state
            st.session_state.authenticated = True
            st.session_state.user_info = user_info
            st.session_state.token_info = token_info
            
            st.success(f"✅ Welcome, {user_info.get('name', 'User')}!")
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Authentication failed: {str(e)}")
    
    st.stop()

# Main App Content (only shown if authenticated)
if st.session_state.authenticated:
    # User info display
    user_info = st.session_state.user_info
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.subheader(f"👋 Welcome, {user_info.get('name', 'User')}!")
    with col2:
        st.write(f"📧 {user_info.get('email', 'No email')}")
    with col3:
        if st.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.session_state.user_info = None
            st.session_state.token_info = None
            st.rerun()
    
    st.divider()
    
    # Job description input section
    st.subheader("📋 Job Description")
    input_text = st.text_area("Enter Job Description:", height=200, placeholder="Paste the job description here...")

    # Resume upload section
    st.subheader("📄 Resume Upload")
    uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

    if uploaded_file is not None:
        st.write("✅ PDF uploaded Successfully")
        
    # Analysis buttons
    st.subheader("🔍 Analysis Options")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        submit1 = st.button("📊 Tell me about the Resume", use_container_width=True)
        submit2 = st.button("🚀 How Can I improve my skills", use_container_width=True)
    
    with col2:
        submit3 = st.button("🔑 What are the Keywords that are missing", use_container_width=True)
        submit4 = st.button("📈 Percentage Match", use_container_width=True)
    
    with col3:
        submit5 = st.button("🤝 Would I give you an interview?", use_container_width=True)

    input_prompt1 = """
    You are an experienced HR Manager with Tech Experience in Data Science, Full Stack, Web Development, Big Data Engineering, DevOps, AWS, Data Analyst. Your task is to review the provided resume against the job description. 
    Please share your professional evaluation on whether the candidate's profile aligns with the role. 
    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
    """

    input_prompt3 = """
    You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
    Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
    the job description. First the output should come as percentage and then keywords missing and last final thoughts.
    """

    input_prompt5 = """
    You are an experienced HR Manager conducting interviews. Based on the resume and job description provided, 
    would you give this candidate an interview? Please provide a clear YES or NO answer first, followed by your reasoning.
    Consider factors like skills match, experience relevance, and overall fit for the role.
    """

    if submit1:
        if uploaded_file is not None and input_text:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_openai_response(input_text, pdf_content, input_prompt1)
            st.subheader("📊 Resume Analysis")
            st.write(response)
        else:
            st.write("⚠️ Please upload a resume and provide a job description")
            
    elif submit3:
        if uploaded_file is not None and input_text:
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_openai_response(input_text, pdf_content, input_prompt3)
            st.subheader("🔑 Keywords Analysis")
            st.write(response)
        else:
            st.write("⚠️ Please upload a resume and provide a job description")
            
    elif submit4:
        if uploaded_file is not None and input_text:
            with st.spinner("🔍 Analyzing your resume..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_openai_response(input_text, pdf_content, input_prompt3)
                
                # Extract percentage from response
                percentage = extract_percentage_from_response(response)
                
                # Create beautiful circular progress
                fig, status, color = create_circular_progress(percentage)
                
                # Display the progress chart
                st.plotly_chart(fig, use_container_width=True)
                
                # Display status
                st.markdown(f"<h2 style='text-align: center; color: {color};'>{status}</h2>", unsafe_allow_html=True)
                
                # Add insult and meme for low scores
                if percentage < 50:
                    insult, meme_url = get_insult_and_meme(percentage)
                    if insult:
                        st.markdown(f"<h3 style='text-align: center; color: #FF6B6B;'>{insult}</h3>", unsafe_allow_html=True)
                        # Center the meme
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            st.image(meme_url, width=300)
                
                # Show detailed analysis in expander
                with st.expander("📋 Detailed Analysis"):
                    st.write(response)
        else:
            st.write("⚠️ Please upload a resume and provide a job description")
            
    elif submit5:
        if uploaded_file is not None and input_text:
            with st.spinner("🤔 Evaluating interview potential..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_openai_response(input_text, pdf_content, input_prompt5)
                
                # Check if response contains YES or NO
                response_lower = response.lower()
                if 'yes' in response_lower[:50]:  # Check first 50 characters
                    st.success("🎉 YES! You would get an interview!")
                    st.balloons()
                elif 'no' in response_lower[:50]:
                    st.error("❌ NO, you would not get an interview.")
                else:
                    st.info("🤷 Maybe - check the detailed response below.")
                
                st.subheader("🤝 Interview Decision")
                st.write(response)
        else:
            st.write("⚠️ Please upload a resume and provide a job description")


     