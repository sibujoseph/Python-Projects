# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 02:27:49 2019

@author: sibuj
"""

import pandas as pd
from datetime import datetime

print(datetime.now())
#Read the Raffle data range
dfAll=pd.read_excel('C:\Sibu\Personal\Church\Harvest Festival 2019\BombayAuction.xlsx', usecols='A:C', sheet_name=None)
df = dfAll['TrackSheet']
#Column Names: Name (Bidder)	Total Bid	Difference
print(datetime.now())
grouped_s=df["Difference"].groupby([df["Name (Bidder)"]]).sum()
grouped_df=pd.DataFrame(grouped_s).reset_index()
grouped_df.columns = ["Name", "Total-Bid-Amount"]
grouped_df.sort_values(by=["Total-Bid-Amount"], inplace=True, ascending=False)
#print(grouped_df.to_string(index=False))

#Winner=dfWinner["Name"].to_string(index=False)

dphtml1="""
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="5" charset="utf-8">
    <title>Harvest Festival 2019 - Bombay Auction</title>
    <link rel="stylesheet" href="C:\Sibu\Personal\Church\Harvest Festival 2019\Display\styleB.css">
  </head>
  <body>
      <div class="table">
          <span class="text4">Bombay Auction Status</span>
      </div>
  </body>
</html>
"""
#.format(Prize, Winner, SelectedTicket)

dphtml1 += grouped_df.to_html(index=False)

DisplayFile='C:\Sibu\Personal\Church\Harvest Festival 2019\Display\BombayAuction.html'
print(datetime.now())
with open(DisplayFile,'w') as f:
    f.write(dphtml1)
    #f.save()
    f.close()

print(datetime.now())