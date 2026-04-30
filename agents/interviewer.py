from utils import call_llm

class InterviewerAgent:
    def __init__(self, prompt):
        self.system_prompt = prompt

    def ask_question(self, context):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": context}
        ]
        return call_llm(messages)
        