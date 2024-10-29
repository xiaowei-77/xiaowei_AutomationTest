import pytest


class Test:

    def test12(self):
        print(12 * 15)


    @pytest.mark.usefixtures
    def test_fibon(self, print_text):
        fib_list = []
        for i in range(10):
            if i == 0 or i == 1:
                fib_list.append(1)
            else:
                fib_list.append(fib_list[i - 2] + fib_list[i - 1])
        print(fib_list, '\t', print_text)


if __name__ == '__main__':
    t = Test()
    t.test12()
    t.fibon()
