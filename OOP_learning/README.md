# PEP8 -> https://peps.python.org/pep-0008/
# Notes
- A python class should be defined using CapWords style
- self is a keyword which represent the object istance (like this in JS)
- def \__init__\(self) is the constructor in Python
# Example class definition
### 
```
class Class(self, name):
    self.name = name
if __name__ == "__main__":
    c1 = Class("Test")
```