import os
import openai
from ChatGPTContext import ChatGPTContext as ct
class ChatGPT():
    
    def __init__(self,api_key):
        openai.api_key = api_key
        self.context = ct.get_context_pizzaria()

    def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, 
        )
        return response.choices[0].message["content"]

    def collect_messages(self,msg):
        prompt = msg
        self.context.append({'role':'user', 'content':f"{prompt}"})
        response = self.get_completion_from_messages(self.context) 
        self.context.append({'role':'assistant', 'content':f"{response}"})
        return f'Atendente: {response}\n'



def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, 
        )
        return response.choices[0].message["content"]
    
if __name__ == '__main__':
    
    openai.api_key = ""

    get_completion_from_messages("Bom dia!")
    