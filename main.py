from agents.interviewer import InterviewerAgent
from agents.evaluator import EvaluatorAgent
from agents.coach import CoachAgent
import os

def load_prompt(path):
    base = os.path.dirname(__file__)
    with open(os.path.join(base, path), "r") as f:
        return f.read()

def main():
    role = input("Role: ")
    background = input("Background: ")
    focus = input("Focus: ")

    interviewer = InterviewerAgent(load_prompt("prompts/interviewer.txt"))
    evaluator = EvaluatorAgent(load_prompt("prompts/evaluator.txt"))
    coach = CoachAgent(load_prompt("prompts/coach.txt"))

    context = f"Role: {role}\nBackground: {background}\nFocus: {focus}"
    history = []

    for _ in range(5):
        question = interviewer.ask_question(context)
        print("\nQ:", question)

        answer = input("A: ")

        evaluation = evaluator.evaluate(question, answer)
        print("Score:", evaluation["score"])

        history.append({
            "question": question,
            "answer": answer,
            "evaluation": evaluation
        })

        if evaluation["score"] < 6:
            context += f"\nWeak: {answer}"
        else:
            context += f"\nStrong: {answer}"

    print("\n--- Final Feedback ---")
    print(coach.generate_feedback(history))

if __name__ == "__main__":
    main()