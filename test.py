"""
Created by: humberg
Date:       19.11.20

This module is for testing the setup.
"""

import pandas as pd
import gspread
import sys

cur_row = sys.argv[1]
path = str(sys.argv[2])

################################## UPDATE sheet and row here #######################################
df = pd.read_csv(path, encoding="latin-1", delimiter=";", skiprows=range(0, 11))

####################################################################################################

rel_rows = ["FAZ.NET", "Süddeutsche.de", "FOCUS ONLINE", "DER SPIEGEL", "stern.de", "WELT",
            "n-tv.de", "Bild.de", "ZEIT ONLINE"]

df = df.loc[df['Angebote'].isin(rel_rows), ["Angebote", "online Visits gesamt",
                                            "mobile Visits gesamt"]]
df = df.applymap(lambda x: str(x.replace('.','')))

convert_cols = df.columns.drop(['Angebote'])
df[convert_cols] = df[convert_cols].apply(pd.to_numeric, errors='coerce')
df = df.set_index("Angebote")

# url of ivw spreadsheet
url = 'https://docs.google.com/spreadsheets/d/1PFTWjVaEtp-0cpIHRQqBoFXtokfa2xz2oKOZu9nblaI/edit?usp=sharing'

# open spreadsheet
gc = gspread.oauth()
sh = gc.open_by_url(url)
worksheet = sh.worksheet("IVW-Konkurrenzübersicht")

# update cells

# set variables
faz_on = df.at["FAZNET", "online Visits gesamt"].tolist()
faz_mob = df.at["FAZNET", "mobile Visits gesamt"].tolist()
worksheet.update('J' + str(cur_row) + ':K' + str(cur_row), [[faz_on, faz_mob]])





