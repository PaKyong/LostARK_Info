import requests

# r = requests.post('http://developer-lostark.game.onstove.com/markets/items', headers=header, json=json_data)
# r = requests.get('https://developer-lostark.game.onstove.com/characters/야근러/siblings', headers=header).json()
# r = requests.get('https://developer-lostark.game.onstove.com/armories/characters/야근러/equipment', headers=header).json()
# r = requests.get('https://developer-lostark.game.onstove.com/auctions/options', headers=header)

class GetData:
    header = {
        'accept': 'application/json',
        'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZ'
                         'CI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIs'
                         'ImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwM'
                         'DEwMDgifQ.H1Jy5z7lpJrbSxfwDf-8k1pnG5aYsCglMBppfwEg0PlroaK99duLq5aZl65f8qOIh_Q1qRqSyNGQhxTOGijuYnq'
                         'rISfKagyAltzk4Eap7soz7pMSfBQjtKM4G6pBEtGv1SNcu8mSztpAHZ6fg63v2MB50bS5dkpftIJj0oBXMimXPSsYJgoBj4DYn'
                         'DasFfzsXeeBHsjfDF_84IIMGfGVcHB4RTX24Vb-9uCIU0vyRcJt2zLisxX56TIx8ZInMQhsJ7CiEYTyhELoJwDwBpZIPTMbT'
                         'h_xfsl4Kl4KYXPvRccB4F31b_zExlnxT1GF6LVTpH3KpBBlGUF-f-5Twzi-vQ',

        'content-Type': 'application/json'
    }

    def get_character_lists(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/characters/{name}/siblings',
                            headers=self.header).json()

    def get_character_profiles(self, name):
        return requests.get(f'https://developer-lostark.game.onstove.com/armories/characters/{name}/profiles',
                            headers=self.header).json()

