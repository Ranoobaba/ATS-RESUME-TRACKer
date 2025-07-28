'use client'

import { useState } from 'react'

export default function Home() {
  const [jobDescription, setJobDescription] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleAnalyze = async () => {
    setIsLoading(true)
    // This would connect to your Streamlit backend
    // For now, we'll just show a message
    alert('This would connect to your Streamlit backend for analysis!')
    setIsLoading(false)
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            🔐 ATS Resume Score Checker
          </h1>
          <p className="text-xl text-gray-600">
            AI-powered resume analysis for better job applications
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-xl p-8">
          <div className="mb-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              📋 Job Description
            </h2>
            <textarea
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="Paste the job description here..."
              className="w-full h-40 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
            />
          </div>

          <div className="mb-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              📄 Resume Upload
            </h2>
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">
              <p className="text-gray-500">
                Drag and drop your resume (PDF) here, or click to browse
              </p>
              <input
                type="file"
                accept=".pdf"
                className="hidden"
                id="resume-upload"
              />
              <label
                htmlFor="resume-upload"
                className="mt-4 inline-block bg-blue-600 text-white px-6 py-2 rounded-lg cursor-pointer hover:bg-blue-700 transition-colors"
              >
                Choose File
              </label>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <button
              onClick={handleAnalyze}
              disabled={isLoading}
              className="bg-blue-600 text-white p-4 rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50"
            >
              {isLoading ? 'Analyzing...' : '📊 Analyze Resume'}
            </button>
            <button
              onClick={handleAnalyze}
              disabled={isLoading}
              className="bg-green-600 text-white p-4 rounded-lg hover:bg-green-700 transition-colors disabled:opacity-50"
            >
              {isLoading ? 'Processing...' : '🔑 Check Keywords'}
            </button>
            <button
              onClick={handleAnalyze}
              disabled={isLoading}
              className="bg-purple-600 text-white p-4 rounded-lg hover:bg-purple-700 transition-colors disabled:opacity-50"
            >
              {isLoading ? 'Calculating...' : '📈 Get Score'}
            </button>
          </div>
        </div>

        <div className="mt-8 text-center">
          <p className="text-gray-600">
            💡 This frontend can be connected to your Streamlit backend via API calls
          </p>
        </div>
      </div>
    </main>
  )
}
