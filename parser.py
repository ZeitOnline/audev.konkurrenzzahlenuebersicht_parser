"""
Created by: humberg
Date:       21.08.20

This module parses konkurrenzübersicht data from csv to google spreadsheet
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

sz_on = df.at["Süddeutschede", "online Visits gesamt"].tolist()
sz_mob = df.at["Süddeutschede", "mobile Visits gesamt"].tolist()
worksheet.update('N' + str(cur_row) + ':O' + str(cur_row), [[sz_on, sz_mob]])

foc_on = df.at["FOCUS ONLINE", "online Visits gesamt"].tolist()
foc_mob = df.at["FOCUS ONLINE", "mobile Visits gesamt"].tolist()
worksheet.update('R' + str(cur_row) + ':S' + str(cur_row), [[foc_on, foc_mob]])

sp_on = df.at["DER SPIEGEL", "online Visits gesamt"].tolist()
sp_mob = df.at["DER SPIEGEL", "mobile Visits gesamt"].tolist()
worksheet.update('V' + str(cur_row) + ':W' + str(cur_row), [[sp_on, sp_mob]])

stern_on = df.at["sternde", "online Visits gesamt"].tolist()
stern_mob = df.at["sternde", "mobile Visits gesamt"].tolist()
worksheet.update('Z' + str(cur_row) + ':AA' + str(cur_row), [[stern_on, stern_mob]])

welt_on = df.at["WELT", "online Visits gesamt"].tolist()
welt_mob = df.at["WELT", "mobile Visits gesamt"].tolist()
worksheet.update('AD' + str(cur_row) + ':AE' + str(cur_row), [[welt_on, welt_mob]])

ntv_on = df.at["n-tvde", "online Visits gesamt"].tolist()
ntv_mob = df.at["n-tvde", "mobile Visits gesamt"].tolist()
worksheet.update('AH' + str(cur_row) + ':AI' + str(cur_row), [[ntv_on, ntv_mob]])

bild_on = df.at["Bildde", "online Visits gesamt"].tolist()
bild_mob = df.at["Bildde", "mobile Visits gesamt"].tolist()
worksheet.update('AL' + str(cur_row) + ':AM' + str(cur_row), [[bild_on, bild_mob]])




