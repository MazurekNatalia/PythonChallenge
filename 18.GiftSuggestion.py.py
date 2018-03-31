class collecting_informations:
    mom = {"lolipop": 1, "candy box" : 10, "bag" : 75, "branded bag" : 250, "silver necklace" : 90, "gold necklace" : 145,
           "silver earrings" : 50, "gold earrings" : 135, "flowers" : 40, "perfumes" : 100,
           "branded perfumes" : 350, "scarf" : 35, "wine" : 70}
    dad = {"lolipop": 1, "candy box" : 10,  "set of kraft beers": 45, "whisky": 80, "low cost belt": 30, "leather belt": 90,
           "wallet": 150, "toolkit": 150, "one ride in ferrari": 450}
    brother = {"lolipop": 1, "candy box" : 10,  "set of kraft beers": 45, "whisky": 80, "funny gadget": 50, "book": 65,
               "computer game": 120, "CD of favourite band": 100, "gamer mouse": 125,
               "gamer headphones": 175}
    sister = {"lolipop": 1, "candy box" : 10,  "book": 65, "set of jewelerry": 250, "perfumes": 100, "branded perfumes": 350,
              "make-up brushes": 80, "make-up palette": 145, "manicure coupon": 45}
 
    def for_who(self, receiver, amount):
        presents = {}
        if receiver.lower() in ["mom", "dad", "brother", "sister"]:
            print("\nThis is your list of possible presents and its costs for " + receiver + ":\n")
            if receiver.lower() == "mom":
                presents = self.mom
            if receiver.lower() == "dad":
                presents = self.dad
            if receiver.lower() == "brother":
                presents = self.brother
            if receiver.lower() == "sister":
                presents = self.sister
 
            for k, v in presents.items():
                if v <= amount:
                    print("Present: " + str(k) + "\nPrice: " + str(v) + " zl.\n")
        else:
            print('\nThere is no such person as "' + receiver + '" on the list.')
 
 
receiver = input("Who do you want to give a present to ?\nMom\nDad\nBrother\nSister\n\n")
amount = int(input("\nWhat is a maximum amount of money you want to spend on a present ?\n"))
a = collecting_informations()
a.for_who(receiver, amount)