import sys

class Program:
    #instructions
    I_INC = 'i'
    I_DEC = 'd'
    I_SQR = 's'
    I_OUT = 'o'
    I_OCH = '*'
    I_SDE = '\\'
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
            elif curr_instruction == Program.I_OCH:
                self.OutputASCII()
            elif curr_instruction == Program.I_SDE:
                self.ClearAccumulator()
            self.CheckOverflow()
    def Increment(self):
        self.accumulator += 1

    def Decrement(self):
        self.accumulator -= 1

    def Square(self):
        self.accumulator **= 2

    def Output(self):
        print(self.accumulator, end='')
    
    def OutputASCII(self):
        print(chr(self.accumulator), end='')
    
    def ClearAccumulator(self):
        self.accumulator = 0

flag = False

if __name__ == '__main__':
    try:
        prg = sys.argv[1]
    except:
        flag = True    
    if flag == False:
        if prg:
            try:
                with open(prg, 'r') as f:
                    prg = f.read()
                x = Program(prg)
                x.Run()
            except:
                print("File not found.")
    else:
        raise Exception("File not specified")
