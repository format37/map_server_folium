# The script, which sends a csv table to the foliums server.
# Receiving the map from the server.

import requests
import pandas as pd

# create a table: lat;lon;info;color;fill_color;fill_opacity
df = pd.DataFrame(columns=['lat','lon','info','color','fill_color','fill_opacity'])
# Moscow center
df.loc[0] = [55.753215, 37.622504, 'Moscow', 'red', 'red', 0.5]
# Moscow north
df.loc[1] = [55.8606, 37.4969, 'Moscow north', 'red', 'red', 0.5]
# Moscow south
df.loc[2] = [55.6458, 37.5810, 'Moscow south', 'red', 'red', 0.5]
# Moscow east
df.loc[3] = [55.7558, 37.6177, 'Moscow east', 'red', 'red', 0.5]
# Moscow west
df.loc[4] = [55.7505, 37.6266, 'Moscow west', 'red', 'red', 0.5]


address = 'http://localhost:8081/map'

# save the table to a csv file
df.to_csv('data.csv', sep=';', index=False)

# send the table to the server
r = requests.post(address, data=df.to_csv(sep=';'))
# save text response into a html file
with open('map.html', 'w') as f:
    f.write(r.text)
