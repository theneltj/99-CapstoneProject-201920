# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
def main():
    x = 0
    print(x)
    temp_array = [0, 0, 0, 0, 0]
    if x < 11:
        while True:
            for k in range(len(temp_array)):
                temp_array[k] = x
            temp_array[0] = 12
            print(temp_array)
            bad = 0
            for k in range(len(temp_array)):
                if temp_array[k] >= 11:
                    pass
                else:
                    bad = 1
            if bad == 0:
                break
    print('Completed!')

main()

