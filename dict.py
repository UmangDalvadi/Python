dict={"umang":"dalvadi",
      "keval":"sonagra",
      "virat":"kohli"}
print(type(dict))
print(dict)
print(dict["umang"])

dict1={"umang":"dalvadi",
       "keval":"sonagra",
       "virat":{"first":"morning",
                "second":"afternoon",
                "third":"night"}
       }

print(dict1)
print(dict1["virat"])
print(dict1["virat"]["second"])

dict1["kohli"]=["run"] #"run"
print(dict1)

del dict1["kohli"]
print(dict1)

dict2=dict1.copy()
del dict2["umang"] 
print(dict1)

dict2=dict1
del dict2["umang"] 
print(dict1)

dict1.update({"umang":"dalvadi"})
print(dict1)

print(dict1.keys())
print(dict1.items())