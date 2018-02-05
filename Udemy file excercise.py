


def celsius_far(celsius):
    far_degree = celsius*(9/5)+32
    return far_degree


temperatures=[10,-20,-289,100]
with open("myfile.txt","w") as file:
    for celsius in temperatures:

        if celsius < -273.15:
            print("")
        else:
            content = file.write(str(celsius_far(celsius))+"\n")
