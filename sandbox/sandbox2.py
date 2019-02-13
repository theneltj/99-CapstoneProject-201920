# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
def main():
    inches = 11
    self = 0


    def for_sure(self, inches):
        print(self)
        temp_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if self < 11:
            for k in range(len(temp_array)):
                 temp_array[k] = self
            temp_array[0] = 12
            print(temp_array)
            for k in range(len(temp_array)):
                if temp_array[k] >= inches:
                    pass
                else:
                    return False


    while True:
        if for_sure(self, inches) != False:
            print('Completed!')
            break
        else:
            self = self + 1





main()

