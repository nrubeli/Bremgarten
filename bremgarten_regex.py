import re
import requests

url = 'https://www.hydrodaten.admin.ch/lhg/vorhersage/pqprevi/Pqprevi_COSMO1_2018.txt'
r = requests.get(url)
pattern = re.compile(r"^\d{2}\s\d{2}\s\d{4}(.*)\d$", re.MULTILINE)
if r.status_code == 200:
    print('Accessed Webpage\n')
    html = r.text
    list_of_matches = list(pattern.finditer(html))
    match_array = []
    for element in list_of_matches:
        match_array.append((str(element.group()).split()))
else:
    print('Site could not be reached')

day_1 = []
day_2 = []
day_3 = []
for entry in match_array:
    if match_array[0][0] == entry[0]:
        day_1.append(float(entry[5]))
    elif (int(match_array[0][0])+1) == int(entry[0]):
        day_2.append(float(entry[5]))
    else:
        day_3.append(float(entry[5]))

average_day_1 = int(sum(day_1)/len(day_1))
average_day_2 = int(sum(day_2)/len(day_2))
average_day_3 = int(sum(day_3)/len(day_3))

print('Mittlerer Abfluss von gestern: {} m^3/s'.format(average_day_1))
print('Mittlerer Abfluss von heute: {} m^3/s'.format(average_day_2))
print('Mittlerer Abfluss von morgen: {} m^3/s'.format(average_day_3))
