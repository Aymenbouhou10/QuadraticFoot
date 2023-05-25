import pandas as pd
import requests
import re

season_dfs = {}
#['2017-2018', '2018-2019', '2019-2020', '2020-2021']
for season in ['2017-2018']:
    url = f'https://fbref.com/en/comps/Big5/{season}/stats/players/{season}-Big-5-European-Leagues-Stats'
    res = requests.get(url).text
    htmlStr = res.replace('<!--', '')
    htmlStr = htmlStr.replace('-->', '')
    
    dfs = pd.read_html(htmlStr, header=1)
    
    team_table = dfs[0]
    player_table = dfs[1]
    player_table = player_table[player_table['Rk'].ne('Rk')]
    player_table['Season'] = season
    
    for cat in ['shooting', 'passing', 'gca', 'defense', 'possession', 'misc', 'keepers', 'keepersadv', 'passing_types']:
        print(cat)
        cat_url = f'https://fbref.com/en/comps/Big5/{season}/{cat}/players/{season}-Big-5-European-Leagues-Stats'
        resp = requests.get(cat_url).text
        htmlStr = res.replace('<!--', '')
        htmlStr = htmlStr.replace('-->', '')
        temp_df = pd.read_html(htmlStr, header=1)[1]
        temp_df = temp_df[temp_df['Rk'].ne('Rk')]
        
        newCols = ['Player'] + [x for x in temp_df.columns if x not in player_table.columns]
        temp_df = temp_df[newCols]
        
        player_table = pd.merge(player_table, temp_df, how='outer', on='Player')
        
    season_dfs[season] = player_table
    print('Collected: ', season)

results = pd.concat([df for x, df in season_dfs.items()])
results = results.drop_duplicates()
results = results.reset_index(drop=True)


https://fbref.com/en/comps/Big5/2017-2018/stats/players2017-2018-Big-5-European-Leagues-Stats