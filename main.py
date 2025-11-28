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

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age 
        

class Puppy:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed
    # 기본적으로 python에서 class만 호출하면 메모리값을 리턴함. __str__은 그 대신에 표시할 메시지를 설정하게 함
    def __str__(self):
        return f"{self.breed} Puppy named {self.name}"
    def woof_woof(self):
        print("woof woof")



ruffus = Puppy("Ruffus", "Beagle")
bibi = Puppy("Bibi", "Dalmatian")



print(ruffus, bibi)