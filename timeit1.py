#Note: You can safely ignore all the code written here. Basically it are three different ways to achieve the same thing, we want to see how performance differs.
#Two ways to let timeit run: turn all the three for loops into functions, or turn them into strings. Turning into functions is easy, so we use strings here.
#Watch indentation, code must start with no indentation, and be indented correct relative to the first line. Incorrect indentation causes an error when timeit tries to
#execute code, but because it's a string you won't get any help from your IDE. gc.enable() enables garbage collection.
import timeit

setup = """\
gc.enable() 
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""


print("nested for loops")
print("----------------")
nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)
print()
"""

print("List comprehension inside a for loop")
print("------------------------------------")
list_comp_loop = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)
print()
"""

print("nested comprehension")
print("--------------------")
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                          for loc in sorted(locations)]
for index, loc in enumerate(exits_to_destination_3):
    print("Locations leading to {}".format(index), end='\t')
    print(loc)
"""

result_1 = timeit.timeit(nested_loop, setup = setup, number=10000)      #timeit doesn't know of anything defined in your programs, except for arguments passed to it...
result_2 = timeit.timeit(list_comp_loop, setup = setup, number=10000)   #That's why it provides the setup and global parameters to allow us to setup the environment
result_3 = timeit.Timer(list_comp_loop, setup=setup)                    #the code will execute in. If you use globals code will execute in global namespace, which means
print("Nested loop:\t{}".format(result_1))                              #that everything defined in module will be available to snippet. This might be overkill, for testing small snippets
print("Loop and comp:\t{}".format(result_2))                            #of code. But can be useful with env to complex to setup in single block of code. Generally though, setup
print("Nested comp: \t{}".format(result_3))                             #argument is better because it works with earlier versions and allows you to be more specific about the env
                                                                        #the code will run in. Store variables in string again, and pass them to setup parameter.
