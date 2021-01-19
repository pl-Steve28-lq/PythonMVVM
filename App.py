from utils.MVVM import *
from utils.Livedata import LiveData

class MyViewModel(ViewModel):
    def __init__(self):
        self.count = LiveData(0)

class MyView(View):
    def __init__(self):
        self.mv = MyViewModel.instance
        self.mv.count.setListener(
            lambda val: print(f'You clicked {val} times!')
        )

    def a(self):
        self.mv.count.value += 1

a = MyView()
s = __import__('time').sleep

for i in [0]*30:
    a.a()
    s(0.1)
