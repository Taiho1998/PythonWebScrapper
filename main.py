# from requests import get

# websites = {
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com",
# }

# results = {}

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     response = get(website)
#     if response.status_code == 200:
#         results[website] = "OK"
#     else:
#         results[website] = "FAILED"

# print(results)

class player:

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def introduce(self):
        print(f"Hello, I'm {self.name} from team {self.team}")

class team:

    def __init__(self, teamName):
        self.teamName = teamName
        self.players = []

    def introduce(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = player(name, self.teamName)
        self.players.append(new_player)

team_x = team("x")
team_y = team("y")

team_x.add_player("alex")
team_y.add_player("beaver")

team_y.introduce()