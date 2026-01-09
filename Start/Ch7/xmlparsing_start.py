# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#
import xml.dom.minidom
import os
from os import path

# use the parse() function to load and parse an XML file
realpath = os.path.realpath("/workspaces/learning-python-3980343/samplexml.xml")
doc = xml.dom.minidom.parse(realpath)

# print out the document node and the name of the first child tag
# print(doc.nodeName)
# print(doc.firstChild.tagName)

# get a list of XML tags from the document and print each one
skills = doc.getElementsByTagName("skill")
print("Skill count: ", skills.length)
for skill in skills:
  print(skill.getAttribute("name"))
    
# create a new XML tag and add it into the document
new_skill = doc.createElement("skill")
new_skill.setAttribute("name", "IODL")
doc.firstChild.appendChild(new_skill)

# Save the modified XML back to file
with open(realpath, "w", encoding="utf-8") as f:
    f.write(doc.toprettyxml("\n"))

skills = doc.getElementsByTagName("skill")
# print(skills)
print("Skill count: ", skills.length)
for skill in skills:
  print(skill.getAttribute("name"))