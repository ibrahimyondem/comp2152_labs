# Heart class for composition
class Heart:
    def _init__(self):
        print("Composition: Heart is created")
        self.beats_per_minute = 72
    def beat(self):
        print("Composition: Heart is beating...")

    def __del__(self):
        print("Composition: Heart is destroyed")
