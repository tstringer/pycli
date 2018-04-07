import sys
from .classmodule import MyClass
from .funcmodule import my_function


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_function('hello world')

    my_object = MyClass('Mark')
    my_object.say_name()


if __name__ == '__main__':
    main()
