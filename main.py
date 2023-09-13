import  random
def main():

    """
    code your program here 
    """
      num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    num3 = random.randint(0,100)

    if num1 < num3:
        if num1 < num2:
            minval = num1
        else:
            minval = num2
    else:
        if num3 < num2:
            minval = num3 
        else:
            minval = num2
    print (num1, num2, num3, minval)
   ################################################## 
   # Do not delete the return statement 
   ################################################## 
    return num1, num2, num3, minval


if __name__ == '__main__':
    main()
