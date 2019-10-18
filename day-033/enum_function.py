from enum import Enum

class Mood(Enum):
    FUNKY = (1, "hello")
    HAPPY = (3, "world")

    def describe(self):
        return self.name, self.value

    def __init__(self, num, nice):
        self.num = num
        self.nice = nice

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY

    @property
    def testValue(self):
        return self.nice + ':' + str(self.num)

print(Mood.favorite_mood())     # my custom str! (3, 'world')
print(Mood.HAPPY.describe())    # ('HAPPY', (3, 'world'))
print(str(Mood.FUNKY))          # my custom str! (1, 'hello')
print(Mood.FUNKY.testValue)     # hello:1
