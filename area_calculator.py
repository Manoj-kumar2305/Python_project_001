
while True:
    print("===============")
    print("Area Calculator")
    print("===============")
    print("1)Triangle\n2)Rectangle\n3)Square\n4)Circle\n5)Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")
    elif choice == 2:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = length * breadth
        print(f"The area of the rectangle is: {area}")
    elif choice == 3:
        side = float(input("Enter the side: "))
        area = side ** 2
        print(f"The area of the square is: {area}")
    elif choice == 4:
        radius = float(input("Enter the radius: "))
        area = 3.14 * radius ** 2
        print(f"The area of the circle is: {area}")
    elif choice == 5:
        break

