# 🎓 TrojanTrack – Your AI-Powered USC Schedule Planner

**TrojanTrack** is a standalone AI-powered web application that helps USC students build a personalized, semester-by-semester course plan based on their STARS report, academic progress, and scheduling preferences.

## 💡 Project Overview

TrojanTrack uses a custom parser, curated academic data, and an AI planning agent to generate smart, graduation-aligned class schedules. Students can upload their STARS report, input personal constraints (like course difficulty limits, unit caps, and GE goals), and receive an optimized course plan they can review and revise through an interactive AI chat.

## ⚙️ Core Features

- 📄 **STARS Report Upload** – Upload your academic record directly
- 🧠 **AI-Powered Schedule Generation** – Get a plan that balances course difficulty, credits, and requirements
- 🎯 **Custom Preferences** – Add constraints like "only 12 units next semester" or "finish GE by junior year"
- 💬 **Interactive Planner** – Refine your schedule via an intelligent chat interface
- 📚 **Manually Curated Course Knowledge Base** – Class prerequisites, unit count, and difficulty scores for accurate planning

## 🧱 Tech Stack

- **Frontend**: React + TailwindCSS
- **Backend**: FastAPI (Python)
- **AI/LLM**: OpenAI GPT-4 + Semantic Kernel
- **Parsing**: Python (pdfplumber or BeautifulSoup)
- **Data**: Custom course catalog in JSON

## 🚀 Getting Started

1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/trojantrack.git
   cd trojantrack

2. Set up the backend
    ```bash
    Copy
    Edit
    cd backend
    pip install -r requirements.txt
    uvicorn app:app --reload
3. Set up the frontend
    ```bash
    Copy
    Edit
    cd frontend
    npm install
    npm run dev