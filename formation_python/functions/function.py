def main():

    # * specify infinit number of arguments
    def fn(*arg):
        for i in arg:
            print(i)
    fn('hello', 'Gym', 'sin', 'Chin', 2, 2.5)

    # return result function
    def rt(number1, number2):
        return number1 + number2
    print(rt(10,30))


# Function Lambda anonymous do only One thing
    chacal = lambda a, b: a + b
    print("TOP LAMBDA STYLE",chacal(5,5))



if __name__ == '__main__':
    main()