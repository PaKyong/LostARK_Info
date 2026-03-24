import requests

# r = requests.post('http://developer-lostark.game.onstove.com/markets/items', headers=header, json=json_data)
# r = requests.get('https://developer-lostark.game.onstove.com/characters/야근러/siblings', headers=header).json()
# r = requests.get('https://developer-lostark.game.onstove.com/armories/characters/야근러/equipment', headers=header).json()
# r = requests.get('https://developer-lostark.game.onstove.com/auctions/options', headers=header)


class LostArkAPI:
    header = {
        'accept': 'application/json',
        'authorization': '',
        'content-Type': 'application/json'
    }

    def get_news(self):
        return requests.get(f'https://developer-lostark.game.onstove.com/news/events',
                            headers=self.header).json()

    def get_character_lists(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/characters/{name}/siblings',
                            headers=self.header).json()

    def get_character_profiles(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/profiles',
                            headers=self.header).json()

    def get_character_equipment(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/equipment',
                            headers=self.header).json()

    def get_character_avatars(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/avatars',
                            headers=self.header).json()

    def get_character_combat_skills(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/combat-skills',
                            headers=self.header).json()

    def get_character_engravings(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/engravings',
                            headers=self.header).json()

    def get_character_cards(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/cards',
                            headers=self.header).json()

    def get_character_gems(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/gems',
                            headers=self.header).json()

    def get_character_colosseums(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/colosseums',
                            headers=self.header).json()

    def get_character_collectibles(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/collectibles',
                            headers=self.header).json()

    def get_guild_ranking_in_server(self, server):
        return requests.get(f'https://developer-lostark.game.onstove.com/guilds/rankings?serverName={server}',
                            headers=self.header).json()

    def get_market_options(self):
        return requests.get(f'https://developer-lostark.game.onstove.com/markets/options',
                            headers=self.header).json()

    def get_market_items(self, item_id: int):
        return requests.get(f'https://developer-lostark.game.onstove.com/markets/items/{str(item_id)}',
                            headers=self.header).json()

    def post_market_items(self, item_id: int):
        return requests.get(f'https://developer-lostark.game.onstove.com/markets/items/{str(item_id)}',
                            headers=self.header).json()
if __name__ == '__main__':
    api = LostArkAPI()
    import json
    print(json.dumps(api.get_character_lists('야근러'), indent=1, ensure_ascii=False))
    print(json.dumps(api.get_character_profiles('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_equipment('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_avatars('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_combat_skills('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_engravings('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_cards('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_gems('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_colosseums('야근러'), indent=1, ensure_ascii=False))
    # print(json.dumps(api.get_character_collectibles('야근러'), indent=1, ensure_ascii=False))
