import os 
import json
import requests
import urllib.request

current_directory = os.getcwd()
execute_foler = current_directory + '/execute'
dir_list = os.listdir(execute_foler)

def downloadImage(imagePath, imageUrl):
    with open(image_name, 'wb') as handle:
        response = requests.get(image_path_url, stream=True)
        print(imagePath)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block) 

for folder in dir_list:
    image_file = open(execute_foler + '/' + folder + '/images.json')
    json_file = json.load(image_file)
    for image_path in json_file:
        image_path_url = 'https:' + image_path
        
        image_name = image_path.split('/')[-1]
        full_image_path = execute_foler + '/' + folder + '/images/' + image_name
        print(full_image_path)
        
        urllib.request.urlretrieve(image_path_url, full_image_path)


