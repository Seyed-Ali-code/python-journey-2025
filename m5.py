while True:
    amal = input("yek amalgar vared konid ( + - * /) baraye khoroj exit ")
    if amal == "exit":
        print("khodanegahdar")
        break
    adad1 = float(input("adad aval ra vared konid"))
    adad2 = float(input("adad dovom ra vared konid"))
    if amal == "+":
        print(f"{adad1} + {adad2} = {adad1+adad2}")
    elif amal == "-":
        print(f"{adad1} - {adad2} = {adad1-adad2}")
    elif amal == "*":
        print(f"{adad1} + {adad2} = {adad1*adad2}")
    elif amal == "/":
        print(f"{adad1} + {adad2} = {adad1+adad2}")
    