
from bs4 import BeautifulSoup
import requests

list_of_gps = [
  'bahrain',
  'emilia-romagna',
  'portuguese',
  'spanish',
  'monaco',
  'azerbaijan',
  'french',
  'styrian',
  'austrian',
  'british',
  'hungarian',
  'belgian',
  'dutch',
  'italian',
  'russian',
  'turkish',
  'united-states',
  'mexican',
  'brazilian',
  'qatar',
  'saudi-arabia',
  'abu-dhabi',
]

data = []

data_format = {
    "driver": "",
    "fastest_time":"",
    "position":"",
    "laps":"",
    "team":"",
    "gp":"",
    "session":"",
    "year":"",
  } 
    

for i in list_of_gps:
  practice = requests.get("https://www.bbc.co.uk/sport/formula1/2021/{}-grand-prix/results/practice/".format(i))
  practice_parsed = BeautifulSoup(practice.content, "html.parser")
  main_group = practice_parsed.find("div", class_="gel-layout gel-layout--center")
  tables = main_group.find_all("div", class_='qa-tables-container')

  for x in tables:
    # getting the rows from each table
    session_name = x.find("h2", class_='qa-event-name')
    # print(session_name.text)
    data_table = x.find("tbody", class_="gel-long-primer")
    row = data_table.find_all("tr")
    # getting the header values for each table
    header_values = []
    needed_values = ["Rank", "Driver", "Team", "Fastest Lap", "Laps" ]
    table_header = x.find("thead", class_="gs-o-table__head")
    table_content = table_header.find_all("th")
    for o in table_content:
      header_values.append(o.text)

    print(header_values)
    for l in row:
      row_content = l.find_all("td")
      data_format['gp'] = i
      data_format['session'] = session_name.text
      data_format['year'] = 2021
      value_counter = 0
      for m in row_content:
        row_value = m.find('span')
        # collect the row data and add to the data format
        if header_values[value_counter] in needed_values:
          if header_values[value_counter] == 'Rank':
            data_format['position'] = row_value.text
          elif header_values[value_counter] == 'Driver':
            data_format['driver'] = row_value.text
          elif header_values[value_counter] == 'Team':
            data_format['team'] = m.text
          elif header_values[value_counter] == 'Fastest Lap':
            data_format['fastest_time'] = row_value.text
          elif header_values[value_counter] == 'Laps':
            data_format['laps'] = row_value.text
          value_counter += 1 
        else:
          value_counter += 1 
          continue
          
    
      print(data_format)
        # if row_value == None:
        #   print(m.text)
        # else:
        #   print(row_value.text)
          



  # qualifying = requests.get("https://www.bbc.co.uk/sport/formula1/2021/{}-grand-prix/results/qualifying/".format(i))
  # race = requests.get("https://www.bbc.co.uk/sport/formula1/2021/{}-grand-prix/results/race/".format(i))
