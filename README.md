# 🔐 ATS Resume Score Checker

A powerful AI-powered resume analysis tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) and improve their chances of getting interviews.

## ✨ Features

- **🔍 AI-Powered Analysis**: Uses OpenAI GPT-4o to analyze resumes against job descriptions
- **📊 Visual Score Display**: Beautiful circular progress indicators with color-coded scoring
- **🎯 Multiple Analysis Types**:
  - Resume overview and strengths/weaknesses
  - Missing keywords identification
  - Percentage match calculation
  - Interview likelihood assessment
  - Skills improvement suggestions
- **😄 Fun Features**: Humorous insults and memes for low scores
- **🔐 Google OAuth**: Secure login with Google accounts
- **📱 Responsive Design**: Works on desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Google Chrome (for PDF processing)
- OpenAI API key
- Google OAuth credentials

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Ranoobaba/ATS-RESUME-TRACKer.git
   cd ATS-RESUME-TRACKer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_CLIENT_ID=your_google_client_id_here
   GOOGLE_CLIENT_SECRET=your_google_client_secret_here
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**:
   Navigate to `http://localhost:8503`

## 🔧 Setup Instructions

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account and get your API key
3. Add it to your `.env` file

### Google OAuth Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add `http://localhost:8503` as authorized redirect URI
6. Copy Client ID and Client Secret to your `.env` file

## 📖 How to Use

1. **Login**: Use your Google account to authenticate
2. **Enter Job Description**: Paste the job description you're applying for
3. **Upload Resume**: Upload your resume in PDF format
4. **Choose Analysis**: Select from multiple analysis options:
   - **Resume Analysis**: Get detailed feedback on your resume
   - **Keywords Missing**: Identify missing keywords from job description
   - **Percentage Match**: See your match score with visual indicator
   - **Interview Likelihood**: Find out if you'd get an interview
   - **Skills Improvement**: Get suggestions to improve your skills

## 🎨 Features in Detail

### Visual Score Display
- **Color-coded scoring**: Green (80-100%), Light Green (60-79%), Gold (40-59%), Orange (20-39%), Red (0-19%)
- **Status labels**: EXCELLENT, GOOD, FAIR, POOR, TERRIBLE
- **Circular progress indicators** with smooth animations

### Fun Elements
- **Random insults** for scores below 50%
- **GIF memes** that display for low scores
- **Balloons animation** for high interview likelihood

### Security
- **Google OAuth authentication**
- **Environment variable protection** for API keys
- **Secure session management**

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **AI**: OpenAI GPT-4o
- **Authentication**: Google OAuth 2.0
- **Charts**: Plotly
- **PDF Processing**: pdf2image, PIL
- **Styling**: Custom CSS with emojis and modern design

## 📁 Project Structure

```
ATS-RESUME-TRACKer/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── venv/              # Virtual environment (auto-created)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4o API
- Streamlit for the amazing web framework
- Google for OAuth authentication
- The open-source community for various libraries used

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for job seekers everywhere!** 