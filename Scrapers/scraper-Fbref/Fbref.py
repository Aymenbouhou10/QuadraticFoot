import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import warnings

# Ignorer les avertissements
warnings.filterwarnings("ignore")

# Liste des ligues
my_liste = [
    ('9', 'Premier-League', 'England1'),
    ('12', 'La-Liga', 'Spain'),
    ('11', 'Serie-A', 'Italy'),
    ('13', 'Ligue-1', 'France'),
    ('20', 'Bundesliga', 'Germany'),
    ('10', 'Championship', 'England2'),
    ('23', 'Eredivisie', 'Netherlands'),
    ('32', 'Primeira-Liga', 'Portugal'),
    ('37', 'Belgian-First-Division-A', 'Belgium')
]

# Catégories des statistiques
cats = [
    ('stats', '#stats_standard'),
    ('shooting', '#stats_shooting'),
    ('passing', '#stats_passing'),
    ('gca', '#stats_gca'),
    ('defense', '#stats_defense'),
    ('possession', '#stats_possession'),
    ('misc', '#stats_misc'),
    ('keepers', '#stats_keeper'),
    ('keepersadv', '#stats_keeper_adv'),
    ('passing_types', '#stats_passing_types'),
    ('playingtime', '#stats_playing_time')
]

dataset = {}
Tablenontrouve = 0

for ligue in my_liste:
    season_dfs = {}

    for season in ['2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']:
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||',ligue[1],  season, 'started','||||||||||||||||||||||||||||||||||||||||||||||||||||')
        
        # Obtenir l'URL de la saison
        url = f'https://fbref.com/en/comps/{ligue[0]}/{season}/stats/{season}-{ligue[1]}-Stats'
        res = requests.get(url).text
        htmlStr = res.replace('<!--', '')
        htmlStr = htmlStr.replace('-->', '')
        
        # Extraire les tableaux HTML
        dfs = pd.read_html(htmlStr, header=1)
        team_table = dfs[0]
        player_table = dfs[2]
        
        # Supprimer les lignes avec "Rk" dans la colonne "Rk"
        player_table = player_table[player_table['Rk'].ne('Rk')]
        
        # Ajouter les colonnes "Season" et "League"
        player_table['Season'] = season
        player_table['League'] = ligue[2]

        for cat in cats:
            # Obtenir l'URL de la catégorie
            cat_url = f'https://fbref.com/en/comps/{ligue[0]}/{season}/{cat[0]}/players/{season}-{ligue[1]}-Stats'
            res = requests.get(cat_url).text
            htmlStr = res.replace('<!--', '')
            htmlStr = htmlStr.replace('-->', '')
            
            # Utiliser BeautifulSoup pour analyser le HTML
            soup = BeautifulSoup(htmlStr, "html.parser")
            table_selector = cat[1]
            #print(table_selector)
            
            # Sélectionner le tableau correspondant à la catégorie
            table = soup.select_one(table_selector)
            
            if table is None:
                print(table_selector,"Tableau non trouvé.")
                Tablenontrouve = Tablenontrouve + 1
                continue
                
            
            # Lire le tableau HTML en DataFrame
            temp_df = pd.read_html(str(table), header=1)[0]
            
            # Supprimer les lignes avec "Rk" dans la colonne "Rk"
            temp_df = temp_df[temp_df['Rk'].ne('Rk')]
            
            # Supprimer les lignes en doublon
            temp_df = temp_df.drop_duplicates()

            # Sélectionner les colonnes qui ne sont pas déjà présentes dans player_table
            newCols = ['Player'] + [x for x in temp_df.columns if x not in player_table.columns]
            temp_df = temp_df[newCols]

            # Fusionner les DataFrames en utilisant la colonne 'Player' comme clé et spécifier un suffixe pour les colonnes en doublon
            player_table = pd.merge(player_table, temp_df, how='outer', on='Player', suffixes=('', f'_{cat[0]}'))
            
            # Supprimer les lignes en doublon
            player_table = player_table.drop_duplicates()
            
            # Attendre 5 secondes avant de continuer la boucle
            time.sleep(5)

        season_dfs[season] = player_table
        player_table = player_table.drop_duplicates()
        player_table = player_table.drop_duplicates(subset=['Rk'], keep='first')
        
        # Enregistrer le DataFrame en fichier CSV
        player_table.to_csv(ligue[1] + ' ' + season + '.csv', index=False)
        print('####################################################',ligue[1],  season, 'Collecté','####################################################')
        
        # Attendre 10 secondes avant de passer à la prochaine saison
        time.sleep(10)

print('Nombre de tables non trouvées est: ', Tablenontrouve)