import requests
import struct
import time

def uuid_to_int_array(uuid):
    # Remove hyphens and convert to a list of 8-character strings
    uuid = uuid.replace("-", "")
    parts = [uuid[i:i + 8] for i in range(0, len(uuid), 8)]

    # Convert each part to a signed integer
    int_array = [struct.unpack('!i', bytes.fromhex(part))[0] for part in parts]

    return int_array

user = input("Username: ")

try:
    resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{user}")
    data = resp.json()
    
    if "id" in data:
        uuid = data["id"]
        int_array = uuid_to_int_array(uuid)

        # Create the formatted string
        formatted_string = f"/give @p allay_spawn_egg[minecraft:entity_data={{id:ender_pearl,LeftOwner:1b,Owner:[I; {int_array[0]}, {int_array[1]}, {int_array[2]}, {int_array[3]} ]}},minecraft:item_name='[{{\"text\":\"/tp {user}\",\"italic\":false}}]']"
        print("Command:")
        print(formatted_string)
    else:
        error = data["error"]
        print(error)
except Exception as e:
    print("An error occurred:", e)

while (True):
    time.sleep(1)
