class FlyBehavior:
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlynoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class QuackBehavior:
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")

class Duck:
    def __init__(self) -> None:
        self.fly_behavior = FlynoWay()
        self.quack_behavior = Quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def setFlyBehavior(self, fly_behavior):
        self.fly_behavior = fly_behavior
    
    def display(self):
        pass

    def setQuackBehavior(self, quack_behavior):
        self.quack_behavior = quack_behavior
    
class RedheadDuck(Duck):
    def display(self):
        print("I'm a real Redhead duck")

class RubberDuck(Duck):
    def display(self):
        print("I'm a rubber duck")
    
class DecoyDuck(Duck):
    def display(self):
        print("I'm a decoy duck")

class MallardDuck(Duck):
    def display(self):
        print("I'm a real Mallard duck")

class Main:
    def main(self):

        mallard = MallardDuck()
        mallard.display()
        mallard.perform_quack()
        mallard.perform_fly()
        mallard.setFlyBehavior(FlyWithWings())
        mallard.perform_fly()
        mallard.setQuackBehavior(Squeak())
        mallard.perform_quack()
        print("\n\n")

        decoy = DecoyDuck()
        decoy.display()
        decoy.perform_quack()
        decoy.perform_fly()
        decoy.setFlyBehavior(FlynoWay())
        decoy.setQuackBehavior(MuteQuack())
        decoy.perform_fly()
        decoy.perform_quack()

if __name__ == "__main__":
    Main().main()