def FunX(x):
    def FunY(y):
        return x * y
    return FunY

i = FunX(8)
print(i(5))
print(FunX(8)(5))