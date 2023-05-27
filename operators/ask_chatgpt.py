import json

from .base_operator import BaseOperator


class AskChatGpt(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Ask ChatGPT'
    
    @staticmethod    
    def declare_parameters():
        return [
            {
                "name": "question",
                "data_type": "string",
                "placeholder": "Enter your question"
            },
            {
                "name": "context",
                "data_type": "string",
                "placeholder": "Enter context (optional)"
            },
            {
                "name": "max_tokens",
                "data_type": "integer",
                "placeholder": "Enter max tokens for response"
            }
        ]
     
    @staticmethod   
    def declare_inputs():
        return [
            {
                "name": "question",
                "data_type": "string",
                "optional": "1"
            },
        ]
    
    @staticmethod 
    def declare_outputs():
        return [
            {
                "name": "chatgpt_response",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        input_question = ai_context.get_input('question', self)
        param_question = p['question']
        prompt = input_question or param_question
        context = p.get('context')
        if context:
            prompt = f'given the context: {context} answer the question: {prompt}'
        ai_response = ai_context.run_chat_completion(prompt=prompt)
        ai_context.set_output('chatgpt_response', ai_response, self)
        ai_context.add_to_log(f'Response from ChatGPT: {ai_response}', save=True)
        
        
