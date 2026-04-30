import streamlit as st

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="AI Mock Interview Coach", layout="wide")

import os
from agents.interviewer import InterviewerAgent
from agents.evaluator import EvaluatorAgent
from agents.coach import CoachAgent


# -------- LOAD PROMPTS --------
def load_prompt(path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, path)

    with open(full_path, "r") as f:
        return f.read()


# -------- INIT AGENTS --------
@st.cache_resource
def init_agents():
    interviewer = InterviewerAgent(load_prompt("prompts/interviewer.txt"))
    evaluator = EvaluatorAgent(load_prompt("prompts/evaluator.txt"))
    coach = CoachAgent(load_prompt("prompts/coach.txt"))
    return interviewer, evaluator, coach


interviewer, evaluator, coach = init_agents()

st.title("🤖 AI Mock Interview Coach")

# -------- SESSION STATE --------
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.history = []
    st.session_state.context = ""
    st.session_state.turn = 0
    st.session_state.current_question = ""

# -------- SETUP --------
if not st.session_state.started:
    role = st.text_input("Target Role")
    background = st.text_area("Background")
    focus = st.selectbox("Focus", ["behavioral", "technical", "mixed"])

    if st.button("Start Interview"):
        st.session_state.started = True
        st.session_state.context = f"Role: {role}\nBackground: {background}\nFocus: {focus}"
        st.session_state.turn = 0
        st.session_state.history = []
        st.session_state.current_question = ""
        st.rerun()

# -------- INTERVIEW --------
if st.session_state.started:

    if st.session_state.current_question == "":
        st.session_state.current_question = interviewer.ask_question(
            st.session_state.context
        )

    st.markdown(f"**Interviewer:** {st.session_state.current_question}")

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):
        if answer.strip() == "":
            st.warning("Enter answer")
        else:
            evaluation = evaluator.evaluate(
                st.session_state.current_question, answer
            )

            st.success(f"Score: {evaluation['score']}")

            st.session_state.history.append({
                "question": st.session_state.current_question,
                "answer": answer,
                "evaluation": evaluation
            })

            if evaluation["score"] < 6:
                st.session_state.context += f"\nWeak: {answer}"
            else:
                st.session_state.context += f"\nStrong: {answer}"

            st.session_state.turn += 1
            st.session_state.current_question = interviewer.ask_question(
                st.session_state.context
            )

            st.rerun()

    if st.session_state.turn >= 5:
        st.subheader("Final Feedback")
        feedback = coach.generate_feedback(st.session_state.history)
        st.markdown(feedback)