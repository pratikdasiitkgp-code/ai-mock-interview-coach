from utils import call_llm
import json

class EvaluatorAgent:
    def __init__(self, prompt):
        self.system_prompt = prompt

    def evaluate(self, question, answer):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Question: {question}\nAnswer: {answer}"}
        ]

        response = call_llm(messages, temperature=0.3)

        try:
            return json.loads(response)
        except:
            return {
                "score": 5,
                "clarity": 5,
                "depth": 5,
                "relevance": 5,
                "issues": ["Invalid JSON"],
                "followup_hint": "Can you clarify?"
            }