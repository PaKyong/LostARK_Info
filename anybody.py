import json

abcd = {
    'my_character_name': '야근러'
}
with open('./hyp.json', 'w') as f:
    json.dump(abcd, f, indent=2)