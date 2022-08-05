import os 
import json
import requests
import urllib.request

base_image_url = 'https://fastwork-config.s3.ap-southeast-1.amazonaws.com/prod/contentful/image/'

def imageMobileDef(json_file):
    new_json_file = json_file
    for index, element in enumerate(json_file):
        image_path = element['fields']['imageMobile']['fields']['file']['url']
        new_image_name = base_image_url + image_path.split('/')[-1]
        
        new_json_file[index]['fields']['imageMobile']['fields']['file']['url'] = new_image_name
    return new_json_file
    
def imageDef(json_file):
    new_json_file = json_file
    for index, element in enumerate(json_file):
        image_path = element['fields']['image']['fields']['file']['url']
        new_image_name = base_image_url + image_path.split('/')[-1]
        
        new_json_file[index]['fields']['image']['fields']['file']['url'] = new_image_name
    return new_json_file

def multiDef(json_file):
    new_json_file = json_file
    for index, element in enumerate(json_file):
        image_path = element['fields']['offOpsHoursBanner']['fields']['file']['url']
        new_image_name = base_image_url + image_path.split('/')[-1]
        
        new_json_file[index]['fields']['offOpsHoursBanner']['fields']['file']['url'] = new_image_name
        
        image_path = element['fields']['onOpsHoursBanner']['fields']['file']['url']
        new_image_name = base_image_url + image_path.split('/')[-1]
        
        new_json_file[index]['fields']['onOpsHoursBanner']['fields']['file']['url'] = new_image_name
    return new_json_file

def saveNewJson(new_json, json_path):
    json_object = json.dumps(new_json)
 
    # Writing to sample.json
    with open(json_path, "w") as outfile:
        outfile.write(json_object)

def mainDef(executePath, suffix):
    current_directory = os.getcwd()
    execute_foler = current_directory + '/' + executePath
    dir_list = os.listdir(execute_foler)
    for folder in dir_list:
        image_file = open(execute_foler + '/' + folder + '/' + folder + '.json')
        json_file = json.load(image_file)
        
        new_json_path = execute_foler + '/' + folder + '/convertedJson/' + folder + '.json'
        
        if folder == suffix + '-discount-banner':
            new_json = imageDef(json_file)
            saveNewJson(new_json, new_json_path)
            
        elif folder == suffix + '-support-banner':
            new_json = multiDef(json_file)
            saveNewJson(new_json, new_json_path)
            
        else:
            new_json = imageMobileDef(json_file)
            saveNewJson(new_json, new_json_path)
     
        
if __name__ == "__main__":
    mainDef('execute-id', 'id')
    mainDef('execute', 'th')
    
        