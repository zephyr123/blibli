def Fun1():
    x = [5]

    def Fun2():
        x[0] *= x[0]
        return x[0]

    return Fun2()


Fun1()
