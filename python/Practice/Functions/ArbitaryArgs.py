def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    print(f"{kwargs.get('street')}")
    for value in kwargs.values():
        print(value,end=" ")
    print()

shipping_label("Dr.","Dileep","kumar","I", #Positional args follow key word args
               street="Rajampet",
              city="Kadapa",
              state="AP",
              zip="516115")