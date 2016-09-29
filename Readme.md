# PyMain

### Motivation
I've never liked the python accepted practice of using:
```sh
if __name__=='__main__':
   #do something
```

I thought it would look nicer to create a simple module so one could write code like this:

```sh
@Main
def main():
   #do something
```

Of course the function above, "main" could also take variables such as "sys.args".

### Usage
To get started with PyMain, one needs only do install the package and perform the following in the python script:
```sh
from pymain import Main

@Main
def main():
   #do something
```

And Voila! You are there!

### Caveats
* This package requires the python module "inspect" 
* It will not run in python's interactive mode