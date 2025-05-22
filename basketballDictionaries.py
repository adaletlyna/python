class Player:
    def __init__(self, playerDict):
        self.name = playerDict['name']
        self.age = playerDict['age']
        self.position = playerDict['position']
        self.team = playerDict['team']
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

players = [
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age": 32, "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age": 33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age": 32, "position": "Power Foward", "team": "Philidelphia 76ers"},
    {"name": "", "age": 16, "position": "P", "team": "en"}
]

new_team = []

for player_data in players:
    new_player = Player(player_data)
    new_team.append(new_player)

for player in new_team:
    print(f"Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {player.team}")