import json
import xml.etree.ElementTree as ET

def top_words(string, words_len, top):
  string_list = string.lower().split()
  string_dict = dict()
  for word in string_list:
    if len(word) > words_len:
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
  sorted_dict = sorted(string_dict.items(), key=lambda x: x[1], reverse=True)
  return sorted_dict[:top]

with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)

descriptions = json_data['rss']['channel']['items']
json_descriptions = str()

for description in descriptions:
    json_descriptions += str(description['description']).lower()
    json_descriptions.replace('[', '')
    json_descriptions.replace(']', '')

print(top_words(json_descriptions, 6, 10))


parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

items = root.findall('channel/item')
xml_descriptions = str()
for item in items:
    xml_descriptions += item.find('description').text.lower()

print(top_words(xml_descriptions, 6, 10))
