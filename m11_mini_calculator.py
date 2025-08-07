def calculator(amal,num1,num2):
    if amal =="+":
        cal =  num1+num2
    elif amal=="-":
        cal =   num1 - num2
    elif amal=="*":
        cal = num1 * num2
    elif amal=="/":
        if num2 == 0 :
            return 'Error : divide by zero'
        cal = num1 / num2
    else:
        return "Error : invalid operator"

    return cal

while True:

        amalgar = input("lotfan amalgar ra vared koni + - * / baraye khoroj 'exit' vared konid")
        if amalgar.lower()=='exit':
             print('Bye!')
             break
        elif amalgar not in {'+','-','*','/'}:
             print("amalgare eshtebah vared kardid")
             continue
        try:
            num_1 = float(input("lotfan adad aval ra vared kon"))
            num_2 = float(input("lotfan adad dovom ra vared kon"))

        except ValueError:
            print("adad vared shode namoatabar ast")
            continue


        print(f'Natije = {calculator(amalgar,num_1,num_2)}')

             







