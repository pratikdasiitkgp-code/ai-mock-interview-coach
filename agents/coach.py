from utils import call_llm

class CoachAgent:
    def __init__(self, prompt):
        self.system_prompt = prompt

    def generate_feedback(self, history):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": str(history)}
        ]
        return call_llm(messages)