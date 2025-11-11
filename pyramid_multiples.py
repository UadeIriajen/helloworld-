def main():
    height = int(input("Height: "))
    left_pyramid(height)
    right_pyramid(height)
    central_pyramid(height)

def left_pyramid(n):
    for i in range (1, n+1):
        print("#" * i)

def right_pyramid(n):
    for i in range (1, n + 1):
        print(" " * (n - i) + "#" * i )

def central_pyramid(n):
    for i in range (1, n + 1):
        print(" " * (n - i) + "#" * i + "  " + "#" * i )


if __name__ == "__main__":
    main()








