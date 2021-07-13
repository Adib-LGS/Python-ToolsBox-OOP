def land(title, ending = 'Finito', **kwargs):
    print(title)
    for key, value in kwargs.items():
        print(f"Capital : {key} --> Country: {value}")
    print(ending)

land('List of capitals: ',Paris="France", Jerusalem="Israel")
