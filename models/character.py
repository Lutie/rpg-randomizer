import json

class Character:
    def __init__(self):
        race = Race()
        apparence = Appareance()
        attributes = Attributes()
        persona = Persona()
        job_class = Class()
        self.name = 'John Doe'
        self.race = race
        self.occupation = 'short description'
        self.apparence = apparence
        self.mania = 'attitude or gesture that characterizes the character'
        self.distinctive = 'physical or mental distinctive sign'
        self.persona = persona
        self.talents = ['some distinctive talent if any']
        self.quality = 'highest primary attribute'
        self.default = 'lowest primary attribute'
        self.attributes = attributes
        self.adversity = 'level of adversity'
        self.job_class = job_class

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

class Race:
    def __init__(self):
        self.race = 'Human'
        self.ethnic = 'Emperian'
        self.cultural = 'n/a'

class Appareance:
    def __init__(self):
        self.hearcolor = 'brown'
        self.hearstyle = 'long'

class Attributes:
    def __init__(self):
        primary = PrimaryAttributes()
        secondary = SecondaryAttributes()
        self.primary = primary
        self.secondary = secondary

class PrimaryAttributes:
    def __init__(self):
        self.strenght = 10
        self.dexterity = 10
        self.constitution = 10
        self.agility = 10
        self.perception = 10
        self.charisma = 10
        self.intelligence = 10
        self.willpower = 10
        self.wisdom = 10
        self.cunning = 10

class SecondaryAttributes:
    def __init__(self):
        self.stature = 10
        self.size = 10
        self.ego = 10
        self.appareance = 10
        self.luck = 10
        self.balance = 10
        self.magic = 10
        self.logic = 10

class Persona:
    def __init__(self):
        self.character = ''
        self.alignment = ''
        self.personality = ''
        self.attitude = ''

class Class:
    def __init__(self):
        self.attributes = {'first': 'whatever', 'second': 'whatever'}
        self.mastery = 'n/a'
