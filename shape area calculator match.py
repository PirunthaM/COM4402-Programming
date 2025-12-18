shape = input("circle, square, triangle, rectangle? ")

match shape:
    case "circle":
        radius = float(input("Radius? "))
        area = 3.14 * radius ** 2
        print("Area is ", area)
    case "square":
        side = float(input("side "))
        area = side ** 2
        print("Area is ", area)
    case "triangle":
        base = float(input("base? "))
        height = float(input ("height? "))
        area = 0.5 * base * height
        print("Area is ", area)
    case "rectangle":
        length = float(input("length? "))
        width = float(input ("width? "))
        area = length * width
        print("Area is ", area)
    case shape:
        print("invalid shape")