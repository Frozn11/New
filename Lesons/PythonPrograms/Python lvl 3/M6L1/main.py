import json
import time
import requests
import base64

class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)


def gen_image(prompt, api_url, api_key, secret_key):
    # api = Text2ImageAPI(api_url, '1AA6F14EC22644183057474F029AA58A', '8BB787B3F6773D95804D7E2EAFF02D08')
    api = Text2ImageAPI(api_url, api_key, secret_key)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)
    my_string = str(images).replace("[", "").replace("]", "").replace("'", "")
    # print(my_string) 
    imgdata = base64.b64decode(my_string)
    filename = 'some_image.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)
        
    # with open("1.txt", 'w', encoding='utf-8') as t:
    #   t.write(str(my_string))
    return

if __name__ == '__main__':
    prompt = 'joe'
    api_url = 'https://api-key.fusionbrain.ai/'
    api_key='1AA6F14EC22644183057474F029AA58A'
    secret_key='8BB787B3F6773D95804D7E2EAFF02D08'
    image =gen_image(prompt,api_url, api_key, secret_key)
    print(image)
#Не забудьте указать именно ваш YOUR_KEY и YOUR_SECRET.