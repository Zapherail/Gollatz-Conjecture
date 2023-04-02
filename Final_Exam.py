num = int(input('Input a whole number:'))
def up_and_down(num):
    num_list = []
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            num_list.append(num)
        else:
            num = int(3 * num + 1)
            num_list.append(num)
    return num_list



print(up_and_down(num))




