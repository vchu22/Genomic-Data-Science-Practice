"""
    Measure the efficiency of each algorithm given a large input
"""
import random, time

# generate random string of DNA with a length of 10000000
# reduce the number when running on a low-memory computer
string = ''
char = 't'
for i in range(0,10000000):
    char = random.choice('atcg')
    string += char

# functions to be tested on
def func1(string, char):
    i = 0
    for c in string:
        if c == char:
            i += 1
    return i
def func2(string, char):
    i = 0
    for j in range(len(string)):
        if string[j] == char:
            i += 1
    return i
def func3(string, char):
    match = [c == char for c in string]
    return sum(match)
def func4(string, char):
    return string.count(char)
def func5(string, char):
    return len([i for i in range(len(string)) if string[i] == char])
def func6(string,char):
    return sum(c == char for c in string)

# start test
max = 0
min = 10000

start = time.clock()
func1(string, char)
time.clock()
end = time.clock()
interval = (end - start)
max = (max,interval)[max < interval]
min = (min,interval)[min > interval]
print ("Time for func1 = %f"%(interval))

start = time.clock()
func2(string, char)
time.clock()
end = time.clock()
interval = (end - start)
max = (max,interval)[max < interval]
min = (min,interval)[min > interval]
print ("Time for func2 = %f"%(interval))

start = time.clock()
func3(string, char)
time.clock()
end = time.clock()
interval = (end - start)
max = (max,interval)[max < interval]
min = (min,interval)[min > interval]
print ("Time for func3 = %f"%(interval))

start = time.clock()
func4(string, char)
time.clock()
end = time.clock()
interval = (end - start)
max = (max,interval)[max < interval]
min = (min,interval)[min > interval]
print ("Time for func4 = %f"%(interval))

start = time.clock()
func5(string, char)
time.clock()
end = time.clock()
interval = (end - start)
max = (max,interval)[max < interval]
min = (min,interval)[min > interval]
print ("Time for func5 = %f"%(interval))

start = time.clock()
func6(string, char)
time.clock()
end = time.clock()
interval = (end - start)
max = (max,interval)[max < interval]
min = (min,interval)[min > interval]
print ("Time for func6 = %f"%(interval))

print "Longest time = ", max
print "Shortest time = ", min