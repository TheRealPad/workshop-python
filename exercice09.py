def division(a, b):
    if b == 0:
        raise Exception("division by 0")
    else:
        print(a / b)

if __name__ == "__main__":
    try:
        division(10, 0)
    except Exception as error:
        print(error)