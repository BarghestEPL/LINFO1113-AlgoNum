def newton_raphson(f, a, b, tol=1.0e-9):
    def df(px):
        return ((f(px + tol) - f(px - tol)) / (2 * tol)) + np.power(tol, 2)

    fa = f(a)
    x = 0.5 * (a + b)
    for i in range(30):
        fx = f(x)
        if fx == 0.0:
            return fx
        if np.sign(fa) != np.sign(fx):
            b = x
        else:
            a = x
        dfx = df(x)
        dx = -fx / dfx if dfx else b - a
        x += dx
        if (b - x) * (x - a) < 0.0:
            dx = 0.5 * (b - a)
            x = a + dx
        if abs(dx) < tol * max(abs(b), 1.0):
            print(i)
            return x
    print('Too many iterations in Newton-Raphson')


def plot_me(f, n, px):
    vx = np.arange(-n, n + 1, 1)
    v_func = np.vectorize(f)
    vy = v_func(vx)
    print(vy)