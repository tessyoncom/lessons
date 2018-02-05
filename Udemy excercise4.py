


def celsius_far(celsius):
    far_degree = celsius*(9/5)+32
    return far_degree


temperatures=[10,-20,-289,100]
for celsius in temperatures:
    if celsius < -273.15:
        print ("No matter can survive at this temperature.")
    else:
        print ("Your Farenheight temperature is: ", celsius_far(celsius) )
