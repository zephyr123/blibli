class Bird:
    def fly(self):
        print("Fly away!")

class Penguin(Bird):
    def fly(self):
        pass
bird = Bird()
penguin = Penguin()
bird.fly()
penguin.fly()