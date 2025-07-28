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
- **🌐 Modern Frontend**: Next.js frontend with beautiful UI

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+ (for frontend)
- Google Chrome (for PDF processing)
- OpenAI API key
- Google OAuth credentials

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Ranoobaba/ATS-RESUME-TRACKer.git
   cd ATS-RESUME-TRACKer
   ```

2. **Install backend dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies**:
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_CLIENT_ID=your_google_client_id_here
   GOOGLE_CLIENT_SECRET=your_google_client_secret_here
   ```

5. **Run the backend (Streamlit)**:
   ```bash
   streamlit run app.py
   ```

6. **Run the frontend (Next.js)**:
   ```bash
   cd frontend
   npm run dev
   ```

7. **Open your browser**:
   - Backend: `http://localhost:8503`
   - Frontend: `http://localhost:3000`

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

### Streamlit Backend (Full Features)
1. **Login**: Use your Google account to authenticate
2. **Enter Job Description**: Paste the job description you're applying for
3. **Upload Resume**: Upload your resume in PDF format
4. **Choose Analysis**: Select from multiple analysis options

### Next.js Frontend (Modern UI)
1. **Enter Job Description**: Use the beautiful text area
2. **Upload Resume**: Drag and drop or click to browse
3. **Click Analysis Buttons**: Get instant feedback

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

### Backend
- **Framework**: Streamlit
- **AI**: OpenAI GPT-4o
- **Authentication**: Google OAuth 2.0
- **Charts**: Plotly
- **PDF Processing**: pdf2image, PIL

### Frontend
- **Framework**: Next.js 14
- **Styling**: Tailwind CSS
- **Language**: TypeScript
- **UI Components**: Custom components with modern design

## 📁 Project Structure

```
ATS-RESUME-TRACKer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
├── README.md          # This file
├── frontend/          # Next.js frontend
│   ├── src/
│   ├── package.json
│   └── ...
└── venv/              # Virtual environment (auto-created)
```

## 🚀 Deployment

### Backend (Streamlit)
- Deploy to Streamlit Cloud
- Or use Heroku, Railway, or any Python hosting

### Frontend (Next.js)
- Deploy to Vercel (recommended)
- Or use Netlify, Railway, or any static hosting

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
- Next.js for the modern frontend framework
- Google for OAuth authentication
- The open-source community for various libraries used

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for job seekers everywhere!**
