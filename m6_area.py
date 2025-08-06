
def circle_status(r):
    masahat = r * r * 3.14
    mohit = r * 2 * 3.14
    return mohit,masahat

rad = float(input("shoae : "))
per,area = circle_status(rad)
print("Mohit =",per)
print("Masahat = ",area)