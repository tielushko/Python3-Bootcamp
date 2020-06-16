def GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    def __missing__(self, key):
        print(f"YOU WANT {key}? Well TOO DAMN BAD IT'S NOT HERE!")
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE TE DICTIONARY?!?!....")
        print("OKAY FINE I GUESS!...")
        super().__setitem__(key,value)
        
data = GrumpyDict({"first":"Tom", "animal":"Cat"})
print(data)
