def celsius_far(celsius):
    far_degree = celsius*(9/5)+32
    return far_degree


celsius = float(input("Enter your celsius temperature: "))
if celsius < -273.15:
    print ("No matter can survive at this temperature. Please enter another: ")
else:
    print ("Your Farenheight temperatur is: ")
    print(celsius_far(celsius))