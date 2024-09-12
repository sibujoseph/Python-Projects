# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:33:36 2019

@author: sibuj
"""
import pandas as pd

#Read the Raffle data range
df=pd.read_excel('C:\Sibu\Personal\Church\Harvest Festival 2019\Harvest Festival 2019 Food Raffle Tickets Tracking Final.xlsx', sheet_name='All Series')
df['Start']=df['Start'].astype(int)
df['End']=df['End'].astype(int)

Prize=int(input(r"Raffle Prize#: "))
if Prize==1:
    Prize='1st' 
elif Prize==2:   
    Prize='2nd' 
elif Prize==3:
    Prize='3rd' 
else:
    Prize="" 
    
SelectedTicket=int(input(r"Enter selected Ticket#: "))
dfWinner=df[(df["Start"]<=SelectedTicket) & (SelectedTicket<=df["End"])]["Name"]
dfWinner=pd.DataFrame(dfWinner).reset_index()
Winner=dfWinner["Name"].to_string(index=False)

dphtml1="""
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="5" charset="utf-8">
    <title>Harvest Festival 2019 - Raffle Draw</title>
    <link rel="stylesheet" href="C:\Sibu\Personal\Church\Harvest Festival 2019\Display\style.css">
  </head>
  <body>
      <div class="container">
          <span class="text1">Congratulations!! Raffle {} Prize Winner!!!</span>
          <span class="text2">{} - Ticket#:{} </span>
      </div>
  </body>
</html>
""".format(Prize, Winner, SelectedTicket)

dphtml1 += dfWinner.to_html()

DisplayFile='C:\Sibu\Personal\Church\Harvest Festival 2019\Display\RaffleWinner{}.html'.format(Prize)

with open(DisplayFile,'w') as f:
    f.write(dphtml1)
    #f.save()
    f.close()
