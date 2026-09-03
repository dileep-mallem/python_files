# Keyword Args = an arg preceded by an Identifier helps with readability 
#                 order of ags doesn't matter 

def hello(greeting , title , first , last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello","MR","dileep" ,"kumar") #Postional Args
hello("Hello",title="MR.",last="Kumar",first="Dileep") #KeyWord Ars (Order doesn't) matter and postional args should follow Keyword Args

                