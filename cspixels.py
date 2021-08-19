import os
import random
import requests
import shutil

class CSPIXELS:
    def __init__(self):
        self.curdir = os.path.dirname(__file__)
        self.api_keys = ['563492ad6f917000010000015dcfc16f132a4cc7bb4e685544fa8bfc','563492ad6f91700001000001767f60a4a8ed40ae96de3f8499097df5','563492ad6f91700001000001ebb6a071844449dd963036ac486493a3','563492ad6f91700001000001ab7811a87b1f427f9d9750b7827f933b','563492ad6f91700001000001ecdd4dd9c83e4c80a815cd020e0d44fb','563492ad6f917000010000010083dba9323c4757bfe384e2fda21bd8']
        self.tmp_image = None

    def random_image(self,keyword,w=1200,h=675,img_name='cspixels_temporary.jpg',orientation = None):
        # orientation = landscape/portrait/square
        # Get total search result 
        keyword = requests.utils.quote(keyword)
        url = 'https://api.pexels.com/v1/search?query='+str(keyword)+'&page=1&per_page=1'
        url = url + ('&orientation='+orientation if orientation != None else '')
        res = requests.get(url, headers= {'Authorization':random.choice(self.api_keys)})
        if res.status_code != 200:
            return False
        res_json = res.json()
        total_results = res_json['total_results']
        print('Total search results: '+str(total_results))

        # Random from total search result 
        rand_page = random.randint(1,int(total_results))
        print('Random choice image: '+str(rand_page))
        url = 'https://api.pexels.com/v1/search?query='+str(keyword)+'&page='+str(rand_page)+'&per_page=1'
        url = url + ('&orientation='+orientation if orientation != None else '')
        res = requests.get(url, headers= {'Authorization':random.choice(self.api_keys)})
        res_json = res.json()
        photo = res_json['photos'][0]
        photo_path = photo['src']['original']
        print('Image id: '+str(photo['id']))

        # Download image to temporary file
        photo_path = photo_path+'?auto=compress&cs=tinysrgb&fit=crop&h='+str(h)+'&w='+str(w)
        tmp_path = os.path.join(self.curdir,img_name)
        res = requests.get(photo_path, stream=True)
        with open(tmp_path, 'wb') as out_file:
            shutil.copyfileobj(res.raw, out_file)
        self.tmp_image = tmp_path
        return tmp_path
    def clear(self):
        try:
            os.remove(self.tmp_image)
        except:
            pass

# px = CSPIXELS()
# img = px.random_image('female and rain')
# print(img)


