import requests

# r = requests.post('http://developer-lostark.game.onstove.com/markets/items', headers=header, json=json_data)
# r = requests.get('https://developer-lostark.game.onstove.com/characters/야근러/siblings', headers=header).json()
# r = requests.get('https://developer-lostark.game.onstove.com/armories/characters/야근러/equipment', headers=header).json()
# r = requests.get('https://developer-lostark.game.onstove.com/auctions/options', headers=header)

class GetData:
    header = {
        'accept': 'application/json',
        'authorization':  
                          
                          
                          
                          
                          
                          ,

        'content-Type': 'application/json'
    }

    def get_character_lists(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/characters/{name}/siblings',
                            headers=self.header).json()

    def get_character_profiles(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/profiles',
                            headers=self.header).json()

