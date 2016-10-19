from inspect import stack, getmodule

class Main:
  @staticmethod
  def __init__(func,*args,**kwargs):
    frm = stack()[1]
    mod = getmodule(frm[0])
    if (mod.__name__ == '__main__'):
      func(*args,**kwargs)

__all__=["Main"]