# AI Mock Interview Coach

## Overview

This project is an attempt to simulate a realistic interview experience using AI.

Instead of asking fixed questions, the system adapts to user responses, asks follow-up questions when needed, and provides structured feedback at the end.

The focus of this project is on building a simple multi-agent system with clear orchestration and decision-making.

---

## Motivation

While preparing for interviews, I found that:

* Practicing alone is not very effective
* Most tools do not adapt to responses
* Feedback is often missing or too generic

This project was built to address these gaps in a simple and practical way.

---

## How it Works

The system is built using three components:

Interviewer

* Generates questions based on the role
* Adapts based on response quality

Evaluator

* Scores answers on clarity, depth, and relevance
* Produces structured output used for control flow

Coach

* Reviews the full session
* Provides final feedback with strengths and improvement areas

---

## Flow

User input → Question → Answer → Evaluation → Decision

* Weak answer → Follow-up question
* Strong answer → Next question

After a few rounds, the system generates a final feedback report.

---

## Setup

```bash
git clone <your-repo-link>
cd mock-interview-coach
pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run

CLI:

```bash
python main.py
```

UI:

```bash
streamlit run streamlit_app.py
```

---

## Features

* Multi-agent architecture
* Adaptive questioning logic
* Real-time evaluation
* Structured feedback output
* Simple Streamlit interface

---

## Limitations

* No retrieval system (RAG) yet
* Evaluation depends on model responses
* Limited interview length (5–7 turns)

---

## Future Work

* Add role-specific question retrieval
* Store session history
* Improve evaluation consistency
* Add performance visualization

---

## Project Structure

```bash
mock-interview-coach/
│
├── agents/
│   ├── interviewer.py
│   ├── evaluator.py
│   └── coach.py
│
├── prompts/
│   ├── interviewer.txt
│   ├── evaluator.txt
│   └── coach.txt
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Author

Pratik Das
M.Tech – Food Process Engineering
Indian Institute of Technology Kharagpur

---

## Note

This is a learning-focused project aimed at exploring multi-agent AI systems and practical orchestration.

Feedback and suggestions are welcome.
