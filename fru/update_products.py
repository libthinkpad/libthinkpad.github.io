import re

import demjson

# 11e (Type 20E6, 20E8) Laptop (ThinkPad) - Type 20E8
# 11e (Type 20ED, 20EE) Laptop (ThinkPad) - Type 20EE
import os
import requests
import simplejson


class ThinkPad:

    def __init__(self, id, brand, name, img):
        self.id = id
        self.brand = brand
        self.name = name
        self.img = img

    def getRealName(self):
        chars = []
        for char in list(self.name):
            if char == '(' or char == '-':
                break
            chars.append(char)
        return "".join(chars)\
            .replace("Laptop", "")\
            .strip()

    def __eq__(self, other):
        return self.getRealName() == other.getRealName()

    def __str__(self) -> str:
        return "{};{};{};{}".format(
            self.getRealName(),
            self.id,
            self.brand,
            self.img
        )

def parseJsonFromSite(site):
    r = r'};ds_pspparts={(.*)};ds_pspaccessorie'
    matched = re.findall(r, site)
    if len(matched) != 1:
        print("Error matching JSON on site!")
        return None
    return "{" + matched[0] + "}"

def main():

    thinkpads = []

    print("Downloading product list from Lenovo")

    # Step 1: Download the list of all ThinkPad products
    response = requests.get("https://support.lenovo.com/us/en/caps")
    if response.status_code != 200:
        print("HTTP Error on lookup: {}".format(response.status_code))
        exit(1)

    pattern = re.compile(">ds_allproducts=(.*);ds_msemyprod")
    json = pattern.findall(response.text)

    if len(json) != 1:
        print("Failed to parse product list")
        exit(1)

    print("Parsing response....")

    json = simplejson.loads(json[0])

    for product in json:
        id = product["Id"]
        brand = product["Brand"]
        name = product["Name"]
        img = product["Image"]
        if "ThinkPad" not in name:
            continue
        if "laptops-and-netbooks" not in id:
            continue

        if id.count("/") != 3:
            continue

        thinkpad = ThinkPad(id, brand, name, img)

        if thinkpads.count(thinkpad) == 0:
            thinkpads.append(thinkpad)


    # Step 2: Download each FRU page
    print("Saving FRU data for ThinkPads")
    l = len(thinkpads)
    i = 0

    for thinkpad in thinkpads:
        i += 1

        if os.path.exists("raw/{}.json".format(thinkpad.getRealName()).replace(" ", "")):
            print("({}/{}) Skipping ThinkPad {}".format(i, l, thinkpad.getRealName()))
            continue

        print("({}/{}) Saving ThinkPad {} ({})".format(i,l,thinkpad.getRealName(), thinkpad.id))
        url = "https://pcsupport.lenovo.com/us/en/products/{}/Parts?isaccessory=false".format(thinkpad.id)

        response = requests.get(url)

        if response.status_code != 200:
            print("HTTP Error for ThinkPad {}".format(thinkpad.name))
            exit(1)

        json = parseJsonFromSite(response.text)

        if json is None:
            print("Failed for ThinkPad {} ({}), skipping".format(thinkpad.getRealName(), thinkpad.id))
            continue

        file = open("raw/{}.json".format(thinkpad.getRealName()).replace(" ", ""), "w")
        file.write(json)
        file.close()


if __name__=="__main__":
    main()