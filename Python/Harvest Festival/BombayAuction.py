# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 02:27:49 2019

@author: sibuj
"""

import pandas as pd
import time as tm
import keyboard

try:
    
    while True:
        df=pd.read_csv('./BombayAuction.csv', sep=',', dtype={"Difference": int, "Total-Bid": int}, usecols=["Name-of-Bidder","Total-Bid","Difference"])
        grouped_s=df["Difference"].groupby([df["Name-of-Bidder"]]).sum()
        grouped_df=pd.DataFrame(grouped_s).reset_index()
        grouped_df.columns = ["Name-of-Bidder", "Total-Bid"]
        grouped_df.sort_values(by=["Total-Bid"], inplace=True, ascending=False)
        
        dfhtml="""
        <!DOCTYPE html>
        <html>
          <head>
            <meta http-equiv="refresh" content="3" charset="utf-8">
            <title>Harvest Festival {year} - Bombay Auction</title>
            <link rel="stylesheet" href="./styleB.css">
          </head>
          <body>
              <div class="table" align="center"><br>
                  <span class="text1">Last Refreshed: {time}</span><br>
                  <span class="text4">Bombay Auction Status</span><br><br><br>
                  <span class="text3">{table}</span>
              </div>
          </body>
        </html>
        """
        
        DisplayFile='./BombayAuction{}.html'.format(tm.strftime('%Y'))
        with open(DisplayFile,'w') as f:
            f.write(dfhtml.format(table=grouped_df.to_html(classes='text4', index=False), year=tm.strftime('%Y'), time=tm.strftime('%Y-%m-%d %H:%M:%S')))
            f.close()
        
        print("refreshed.. ", tm.strftime('%Y-%m-%d %H:%M:%S'))
        tm.sleep(5)
        if keyboard.is_pressed('esc'):
            break
    
    print("Done! ", tm.strftime('%Y-%m-%d %H:%M:%S'))


except Exception as e:
    print(e)