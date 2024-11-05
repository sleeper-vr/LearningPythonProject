def test_function(x):

    def inner_function(y=1):
        print('Я в области видимости функции test_function')

    inner_function()
    return x**2

print(test_function(3))
#inner_function()
