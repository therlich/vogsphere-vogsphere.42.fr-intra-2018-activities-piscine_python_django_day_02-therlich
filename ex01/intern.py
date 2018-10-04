class Intern(object):
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name=name

    def __str__():
        return self.name

    class Coffee(object):
        @staticmethod
        def __str__():
            return "This is the worst coffee you ever tasted."

    @staticmethod
    def work():
        try:
            raise Exception("Go back to work!")
            return
        except Exception:
            return "I’m just an intern, I can’t do that..."

    @staticmethod
    def make_coffee():
        coffee=Intern().Coffee()
        return coffee

if __name__=="__main__":
    intern1=Intern()
    intern2=Intern("Mark")

    print(intern1.name)
    print(intern2.name)
    print(intern2.make_coffee())
    print(intern1.work())
