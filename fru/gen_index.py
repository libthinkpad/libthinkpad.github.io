import os

import simplejson

def getRealName(name):
    chars = []
    for char in list(name):
        if char == '(' or char == '-':
            break
        chars.append(char)
    return "".join(chars) \
        .replace("Laptop", "") \
        .strip()

def main():

    print("[", end="")

    i = 0
    dirs = os.listdir("raw")

    for file in dirs:
        i += 1
        file = open("raw/{}".format(file), "r")
        data = file.read()
        file.close()

        json = simplejson.loads(data)
        product = getRealName(json["ProductName"])

        try:
            sch_main = json["SchematicResults"][0]["Schematic"]["Picture"]
            sch_lcd = json["SchematicResults"][1]["Schematic"]["Picture"]

        except:
            sch_main = "null"
            sch_lcd = "null"

        devdict = dict({
            "name": "ThinkPad {}".format(product),
            "lcd_ass": sch_main,
            "main_ass": sch_lcd,
            "res_file": "{}".format(file.name).replace(".json", "").replace("raw/", "")
        })

        if i == len(dirs):
            print("{}".format(devdict).replace("'", "\""))
        else:
            print("{},".format(devdict).replace("'", "\""))

    print("]", end="")

if __name__ == "__main__":
    main()