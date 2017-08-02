
class fruit(object): #declared class --> makes no objects, inherits from object
    #class has a functionality and is a data structure
    #constructor (__init__): a class method, function that is called when something is created
    #only get inout from parameters
    def __init__(self, color, shape, size): # two underscores mean a dunder
    #'self' is a hidden parameter;
    #'self' sends object(the class fruit) into function
    #variable name doesn't matter bc it can be named anything
    #fruit_color (Variable) is relabeled to 'color'
    #order matters --> keep it consistent
        """ # docstrings
        input: string color, string shape, int size
        output: none
        """
        #self.something only used in a class constructor or methods
        #self.__ are private, *** only accessible within __init__
        #it is a member variable
        self.color = color
        #self.color is a class variable; sets the first parameter 'color' to string from fruit_color
        self.shape = shape
        self.size = size
        self.names = [] # this a list

    def add_name(self, name): #"sets name"; adds to the list
            #checks if the name is already in the list
        if name in self.names:
            print("The name is already taken.")
        else:
                # otherwise the name is added to the list
            self.names.append(name)

    def get_color(self): #getters return; ***access methods
        return self.color #accesses color

    def set_color(self, color): #setters redefine, reset to parameters, do not return
        self.color = color

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_names(self):
        return self.names

fruit_name = input("What fruit do you want?")
fruit_color = input("What color is your fruit?")
fruit_shape = "circle"
fruit_size = 1

#calls class "fruit", only function called is __init__
Fruit = fruit(fruit_color, fruit_shape, fruit_size)
Fruit.add_name(fruit_name)

#for anything that returns something, you must store the info
n = Fruit.get_names() #names that the class has
c = Fruit.get_color()
sh = Fruit.get_shape()
si = Fruit.get_size()
print("The names are " + str(n) + " and the color is " + str(c) + ". \n")
