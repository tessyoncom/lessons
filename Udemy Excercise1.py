def celsius_far(celsius):
    far_degree = float(celsius)*(9/5)+32
    return far_degree

celsius = input("Enter your celsius temperature: ")
print ("Your Farenheight temperatur is: ")
print(celsius_far(celsius))