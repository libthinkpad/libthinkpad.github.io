#
# Copyright (c) 2017 Ognjen Galić
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
import os
from math import floor
from xml.etree.ElementTree import Element, tostring, SubElement

import time

def add_url(root, url: str):
    element = SubElement(root, "url")
    loc = SubElement(element, "loc")
    loc.text = "http://thinkpads.org/" + url
    lastmod = SubElement(element, "lastmod")
    lastmod.text = time.strftime("%Y-%m-%dT%H:%M:%S" + "+00:00")
    changefreq = SubElement(element, "changefreq")
    changefreq.text = "monthly"
    priority = SubElement(element, "priority")
    priority.text = "0.8"


def main():

    root = Element("urlset")
    root.set("xmlns","http://www.sitemaps.org/schemas/sitemap/0.9")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:schemaLocation", "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")

    locs = [
        "about/",
        "projects/",
        "blog/",
        "fru/"
        "repositories/"
    ]

    add_url(root, "")

    for loc in locs:
        for file in os.walk(loc):
            add_url(root, file[0])

    print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
    print(tostring(root).decode("utf-8"))

if __name__ == "__main__":
    main()