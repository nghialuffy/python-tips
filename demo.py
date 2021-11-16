
# coding: utf-8

# In[2]:


b'\xf0\xf1\xf2'.hex()


# In[24]:


bytearray(b'nghialuffy')
bytearray.fromhex('f0f1f2').hex()


# In[67]:


a = compile('print("Hello World")', '', 'exec')
dir(a)
for x in dir(a):
    print(x, a.__getattribute__(x))
    # print(getattr(a, x))


# In[41]:


complex(1, 2)


# In[42]:


dir()


# In[51]:


t, d = divmod(123, 3)
t*3 + d


# In[56]:


# eval('1/0')


# In[58]:


exec('x = 10')


# In[63]:


complex(1, 2).conjugate()


# In[68]:


globals()


# In[76]:


help(x)


# In[77]:


class Test:
    def __init__(self):
        self.x = 10
    
    @classmethod
    def test(cls):
        print(cls.x)


# In[87]:


isinstance(Test, object)


# In[88]:


# demo iter method
class Test:
    def __init__(self):
        self.x = 10
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.x == 0:
            raise StopIteration
        self.x -= 1
        return self.x


for x in Test():
    print(x)
    


# In[90]:


locals() == globals()


# In[99]:


# Demo memoryview method
import array


a = array.array('d', [1, 2, 3])
m = memoryview(a)
m.hex()
# m.tolist()
# m.tobytes()
# m.tobytes() == a.tobytes()


# In[106]:


# Demo print method with flush True/False
import sys


sys.stdout.write('Hello World')
sys.stdout.flush()


# In[146]:


class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


# In[114]:


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


# In[123]:


a = C()


# In[132]:


a.x = 1


# In[133]:


a.x


# In[136]:


# Demo repr method
class C:

    def __init__(self, x):
        self._x = x

    def __repr__(self):
        return 'HIHIC(%r)' % self._x


c = C(10)
str(c)


# In[137]:


# Demo reversed method
list(reversed([1, 2, 3]))


# In[138]:


# Demo super method
class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        super().spam()
        print('B.spam')


b = B()
b.spam()


# In[142]:


# Demo type method
class X:
    a = 1

X = type('X', (object,), {'a': 1})
X


# In[143]:


# Demo vars method
vars(X)


# In[164]:


class MyClass:

    public_attr = "Public Attribute"
    _protected_attr = "Protected Attribute"
    __private_attr = "Private Attribute"

    def method(self, param_1, param_2):
        """
        Epytext http://epydoc.sourceforge.net/manual-epytext.html
        Method explaintation

        @type  param_1: number
        @param param_1: param_1 Description.
        @type  param_2: string
        @param param_2: param_2 Description.
        @rtype:  number
        @return: return description
        """
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'

    @classmethod
    def _protected_method(cls):
        return 'class protected method'

    @classmethod
    def __private_method(cls):
        """
        Python performs name mangling of private variables. Every member with double underscore will be changed to _object._class__variable.
        If so required, it can still be accessed from outside the class, but the practice should be refrained.
        """
        return 'class private method'

# How to call them
MyClass().method(1, "sample")
MyClass.class_method()
MyClass().static_method()
# MyClass.__private_method()
# MyClass._MyClass__private_method()


# In[169]:


# Demo classmethod and staticmethod decorators
class C:
    @classmethod
    def foo(cls):
        cls.bar()
        print('class method called')

    @staticmethod
    def bar():
        
        print('static method called')


C.foo()
C.bar()


# In[14]:


class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return super().toDashDate(self.date)
        # return Dates.toDashDate(self.date)
        # return self.toDashDate(self.date)

    # def toDashDate(self, date):
    #     return date.replace("/", "--")

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

date.getDate() == dateFromDB.getDate()


# In[176]:


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("I'm thanos!")


# In[179]:


from contextlib import contextmanager
@contextmanager
def my_context():
    try:
        yield
    finally:
        pass

with my_context():
    print("I'm Spiderman")

@my_context()
def some_function():
    print("I'm Hulk")


some_function()


# In[183]:


# Learn more: https://www.geeksforgeeks.org/context-manager-in-python/?ref=rp
# https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator
from contextlib import ContextDecorator
class my_context(ContextDecorator):
    
    def __init__(self):
        print('init')

    def __enter__(self):
        print('Enter')

    def __exit__(self, *args):
        print('Exit')

with my_context():
    print("I'm Spiderman")

@my_context()
def some_function():
    print("I'm Hulk")


some_function()


# In[186]:


# Demo Counter class
from collections import Counter

dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'a': 1, 'b': 2, 'c': 3}

dict_3 = dict(Counter(dict_1) + Counter(dict_2))
dict_3


# In[193]:


set(x ** 2 for x in range(5) if True)
m = (x ** 2 for x in range(5) if True)
list(m)


# In[200]:


from collections import OrderedDict

d = OrderedDict.fromkeys('abc')
d.move_to_end('b')
d.keys()
d.move_to_end('b')
d


# In[213]:


# Demo deque class from collections
from collections import deque


d = deque(range(5))
d.append(5)
print(d)
d.appendleft(5)
print(d)
d.extend([7, 8]) # <-- merge list
print(d)
d.extendleft([8, 7])
print(d)

#  'append',
#  'appendleft',
#  'clear',
#  'copy',
#  'count',
#  'extend',
#  'extendleft',
#  'index',
#  'insert',
#  'maxlen',
#  'pop',
#  'popleft',
#  'remove',
#  'reverse',
#  'rotate'


# In[221]:


# Demo SimpleNamespace class from types
from types import SimpleNamespace


namespace = SimpleNamespace(a=1, b=2)
namespace.a
namespace.b


# In[223]:


# generator fibonaaci with yield
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


for x in fib(10):
    print(x)


# In[23]:




# In[34]:


from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

print(a_function_requiring_decoration())


# In[36]:


class logit(object):
    
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit only logs, no more
        print("I am notifying you")

logit._logfile = 'out2.log' # if change log file
@logit
def myfunc1():
    pass

myfunc1()

