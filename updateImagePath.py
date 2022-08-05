import os 
import json
import requests
import urllib.request

current_directory = os.getcwd()
execute_foler = current_directory + '/execute'
dir_list = os.listdir(execute_foler)

def imageMobileDef(json_file):
    print('test')
    
def imageDef(json_file):
    
    print('test')

def multiDef(json_file):
    print('test')

def mainDef():
    for folder in dir_list:
        image_file = open(execute_foler + '/' + folder + '/' + folder + '.json')
        json_file = json.load(image_file)
        
        if folder == 'th-discount-banner':
            imageDef(json_file)
        elif folder == 'th-support-banner':
            multiDef(json_file)
        else:
            imageMobileDef(json_file)
     
        
if __name__ == "__main__":
    mainDef()
        