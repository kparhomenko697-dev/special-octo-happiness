"""
def black_hole(*args):
print(f"args = {args},\n\t type(args) = {type(args)})")
for argument in args:
        print(f"{argument} --> {type(argument)}")

 black_hole( 8, 4, 6,"25","name",2*5,[8,24])
arg = 8, 4, 6,"25","name",2*5,[8,24]
print(f"arg = {type(arg)}")
"""
from symbol import pass_stmt

"""



def black_hole_named(**kwargs):
    print(f"kwargs = {kwargs},\n\t type(kwargs) = {type(kwargs)})")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")

black_hole_named(name="Nick", planet="Earth", school=217, lst=[2, "0"])

kw_arg = {'name': "Nick", 'planet':"Earth", 'school':217, 'lst':[2, "0"]}
print(f"kw_arg = {kw_arg}, \n\ttype(kw_arg) - {type(kw_arg)}")
"""



"""
def black_hole_full(*args, **kwargs):
    print(f"args - {args}")
    print(f"kwargs - {kwargs}")
    for arg in args:
        print(f"{arg} --> {arg}")
        for key, value in kwargs.items():
            print(f"key - {key}, value - {value}")

black_hole_full(12,45,["a", 25], name="Nick",planet="Earth", school=217, )
"""



"""
def black_hole_mixed(var_1, var_2=5, *args, **kwargs):
    print(f"var_1 = {var_1}")
    print(f"var_2 ={var_2}")
    for arg in args:
        print(f"arg - {arg}")
    for key, value in kwargs.items():
        print(f"key - {key}, value - {value}")
        
black_hole_mixed( 0.5, name="Nick", planet="Earth", school=217)
black_hole_mixed( 0.5, 12,  12, 'strings', 2*5, 
                name="Nick", planet="Earth", school=217)
"""




"""
lst = [60,3] # v,a,t --> s = v*t=60*3=180  (км/ч) * ч = (км * ч) / ч
tpl = [60,3] 
dct = {"t": 3, "v":60}

def way(v, t):
        print(f"S = {v} * {t} = {v * t}")
    
way(*lst)
way(*tpl)
way(**dct)
"""


"""
# f-string f-рядки
f_name = "Sarhii"
l_name = "Pustovoit"
school = 217
cls = "8-A"
print("My name -", f_name, "l_name -", l_name,"school -", school, "cls -", cls, '.')
print(f"My name - {f_name}, l_name - {l_name},school - {school}, cls - {cls}.")
print(f"My name - {f_name:121}, l_name - {l_name:15},school - {school:6}, cls - {cls:6}.")
print(f"My name - {f_name:<12}, l_name - {l_name:^15},school - {school:>6}, cls - {cls:^6}.")
print(f"My name - {f_name:^12}, l_name - {l_name:^15},school - {school:>6}, cls - {cls:*^6}.")

day = 28
print(f"Today is {day:7d}.")
print(f"Today is {day:7n}.")

pi = 3.14159265
print(f"pi = {pi:_^10.3f}")

income = 202336
costs = 143274
profit = income /  costs - 1
print(f"profit = {profit:_^10.3f}")
print(f"income = {profit:_^10.3f}")
print(f"profit = {(income / costs - 1):^10.3%}")

print()

#format()

f_name = "Sarhii"
l_name = "Pustovoit"
school = 217
cls = "8-A"
print("My name -", f_name, "l_name -", l_name,"school -", school, "cls -", cls, '.')
print("".format( f_name, l_name, school, cls))
print("My name - {}, l_name - {}, school - {}.".format(f_name, l_name, school))
print("My name - {:.^10}, l_name - {:.^15}, school - {:_>8d}.".format(f_name, l_name, school))
print("My l_name - {1:^15}, name - {0:^10}, school - {2:_>8d}.".format(l_name, f_name, school))


print("Today: {day:^6} {month:_^16}".format(month="februare", day=28))

# use --> %
month = "february"
day = 28
print("Today: %d %s" % (day, month))
day = "second"
s_bool = True
print("Today: %d %s" % (day, month))
"""



"""
# \t - табуляція (4 пробілів); \n - перехідів на новий рядок

print("За час нашого навчання ми постійно стикалися з рядками.")
print("За час нашого навчання\n\t\tми постійно\n\t\t\tстикалися з рядками.")
"""

"""
print("Nothing\n will work\n unless you do.")
"""

"""
print("\"Anyone who\n\tstops\n\tlearning is old,\n\twhether or eighty\"\n\t "Henry Ford")
"""

