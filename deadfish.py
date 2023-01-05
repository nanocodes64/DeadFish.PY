class Program:
    #instructions
    I_INC = 'i'
    I_DEC = 'd'
    I_SQR = 's'
    I_OUT = 'o'

    def __init__(self, data):
        self.accumulator = 0
        self.data = data
    def CheckOverflow(self):
        if self.accumulator == 256 or self.accumulator == -1:           
            self.accumulator = 0
    def Run(self): # the actual interpreter
        for i in self.data:
            curr_instruction = i.lower()
            if curr_instruction == Program.I_INC:
                self.Increment()
            elif curr_instruction == Program.I_DEC:
                self.Decrement()
            elif curr_instruction == Program.I_SQR:
                self.Square()
            elif curr_instruction == Program.I_OUT:
                self.Output()
            self.CheckOverflow()
    def Increment(self):
        self.accumulator += 1

    def Decrement(self):
        self.accumulator -= 1

    def Square(self):
        self.accumulator **= 2

    def Output(self):
        print(self.accumulator)
if __name__ == '__main__':
    prg = input("deadfish1.0\nWhich file to load? X for manual input>")
    if prg != "X":
        try:
            with open(prg, 'r') as f:
                prg = f.read()
        except:
            print("Failed to load! Entering manual input mode.")
            prg = input("Enter deadfish program:")
    else:
        prg = input("Enter deadfish program:")
    x = Program(prg)
    x.Run()
