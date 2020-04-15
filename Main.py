from steam import *

id_url = 'https://steamcommunity.com/id/Kadravor'
api = WebAPI(key="194A600C4357E8560BCCCA2BA69377BA")
account_id = steam.steamid.steam64_from_url(id_url)

print(account_id)


Owned_games = api.IPlayerService.GetOwnedGames(steamid=account_id, format='json', include_appinfo=1, include_played_free_games=1, appids_filter=0)
Owned_games['response']['games'][1]['name']

game_list = []
for n in range(0,Owned_games['response']['game_count']):
    game_list.append(Owned_games['response']['games'][n]['name'])
game_list
