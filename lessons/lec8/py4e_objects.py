# stuff = list()

# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print(stuff[0])
# print(stuff.__getitem__(0))
# print(list.__getitem__(stuff, 0))

# print(dir(stuff))
class Animal:
    pass


class PartyAnimal(Animal):
    x = 0

    def __init__(self, x, y):
        print('I am constructed')

    def party(self):  # function / method
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnimal(3,4)
an.party()
# # an.party()
# # an.party()
# # PartyAnimal.party(an)  # print ???
# # # PartyAnimal.party() #??
# # an2 = PartyAnimal()
# # an2.party()
