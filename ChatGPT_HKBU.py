import configparser
import requests

class HKBU_ChatGPT():
    # def __init__(self,config_path='./config.ini'):
    #     if type(config_path) == str:
    #         self.config = configparser.ConfigParser()
    #         self.config.read(config_path)
    #     elif type(config_path) == configparser.ConfigParser:
    #         self.config = config_path
            
            
    def submit(self,message):
        conversation = [{"role": "user", "content": message}]

        url = (self.os.environ['CHATGPT_BASICURL']) + "/deployments/" + (self.os.environ['CHATGPT_MODELNAME']) + "/chat/completions/?api-version=" + (self.os.environ['CHATGPT_APIVERSION'])
        
        headers = { 'Content-Type': 'application/json',
        'api-key': (self.os.environ['CHATGPT_ACCESS_TOKEN']) }
        payload = { 'messages': conversation }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response
    
if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)