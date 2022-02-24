import json
import pyperclip
import os.path

database = "db_movvy_item.json"


def menuSystem():
    selection = input(
        "Select a Menu Item\n 1. Paste Items\n 2. Import Item\n 3. Print Database\n 4. Exit\n\n > "
    )
    if selection == "1":
        export_json()
        menuSystem()
    elif selection == "2":
        append_json()
        menuSystem()
    elif selection == "3":
        print_json()
        menuSystem()
    elif selection == "4":
        return


def export_json():
    if not os.path.isfile(database):
        data = {}
        data["ItemID"] = []

        for i in pyperclip.paste().split("\r\n"):
            data["ItemId"].append(
                {
                    "Id": 0,
                    "Item": i,
                    "Weight": 0,
                    "Class": "",
                    "Heals": 0,
                    "Durability": 0,
                    "Slots": "",
                    "Effects": "",
                    "Level_use": 0,
                    "Skill_use": "",
                    "Modifiers": "",
                    "enemy_source": "",
                    "location_source": "",
                    "holiday": "",
                    "Faction_craft": "",
                    "Level_craft": 0,
                    "Required_craft": "",
                    "Materials_craft": [{"quantity": 0, "Material": ""}],
                    "location_craft": "",
                    "quantity_craft": [{"min": 0, "max": 0}],
                    "skill_xp": [{"success": 0, "fail": 0}],
                    "char_xp": 0,
                    "clan_xp": 0,
                    "set": "",
                }
            )

        with open(database, "w") as j:
            json.dump(data, j, indent=4)
    else:
        print("File Already Exists")


def append_json():
    with open(database, "r") as j:
        data = json.load(j)
    print(data)


def print_json():
    with open(database, "r") as j:
        data = json.load(j)
        for id in data["ItemID"]:
            print(f"Item: {id['Item']}")
            print(f"Weight: {id['Weight']}")
    print("\n")


menuSystem()
