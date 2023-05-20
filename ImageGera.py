import requests
import json


API_KEY = '---Your API KEY HERE!---'
API_URL = 'https://api.openai.com/v1/images/generations'

def generate_images(model, prompt, size, num_images, response_format='url'):
    params = {'model': model, 'prompt': prompt, 'size': size, 'num_images': num_images, 'response_format': response_format}
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(params))
        data = response.json()
        images = []
        for url in data['data']:
            response = requests.get(url)
            images.append(response.content)
        return images
    except requests.exceptions.RequestException as e:
        print('Ocorreu um erro durante a solicitação:', e)
        return None
    except KeyError as e:
        print('A resposta da API não inclui os dados esperados:', e)
        return None
#model prompt and Max size of the image!!
model = 'image-alpha-001'
prompt = 'Rose field painted in blue'
size = '1024x1024'
num_images = 1

images = generate_images(model, prompt, size, num_images)
if images is not None:
    for i, image in enumerate(images):
        filename = f'futuristic_city_{i}.png'
        with open(filename, 'wb') as f:
            f.write(image)
