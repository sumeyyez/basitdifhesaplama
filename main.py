"""
        ---------------
Basit Diferansiyel Denklem Çözücü
        ---------------
Bu program, birinci dereceden bir diferansiyel denklemi:
    dy/dx = f(x, y),   y(x0) = y0
sayısal olarak çözer. İki yöntem içerir:
1) Euler Yöntemi
2) Runge-Kutta 4 (RK4)

Sonucu bir tablo halinde yazdırır ve isterseniz grafiğini çizer.
"""

import matplotlib.pyplot as plt


def f(x, y):
    """Çözülecek diferansiyel denklem: dy/dx = f(x, y)"""
    return x + y


x0 = 1     # başlangıç x değeri
y0 = 3       # başlangıç y değeri (y(x0) = y0)
x_son =5    # çözümün hesaplanacağı son x değeri
h =3        # adım büyüklüğü (küçük h -> daha hassas ama daha yavaş)
#


def euler_yontemi(f, x0, y0, x_son, h):
    """Euler yöntemi ile dy/dx = f(x, y) denklemini çözer."""
    xs = [x0]
    ys = [y0]

    x, y = x0, y0
    n_adim = int(round((x_son - x0) / h))

    for _ in range(n_adim):
        y = y + h * f(x, y)
        x = x + h
        xs.append(x)
        ys.append(y)

    return xs, ys


def rk4_yontemi(f, x0, y0, x_son, h):
    """4. Mertebeden Runge-Kutta yöntemi ile çözer."""
    xs = [x0]
    ys = [y0]

    x, y = x0, y0
    n_adim = int(round((x_son - x0) / h))

    for _ in range(n_adim):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

        xs.append(x)
        ys.append(y)

    return xs, ys


def sonuclari_yazdir(xs_euler, ys_euler, xs_rk4, ys_rk4):
    print(f"\ndy/dx = f(x, y),   y({x0}) = {y0}   |   x: {x0} -> {x_son},  h = {h}\n")
    print(f"{'x':>8} | {'Euler y':>12} | {'RK4 y':>12}")
    print("-" * 38)
    for x, ye, yr in zip(xs_euler, ys_euler, ys_rk4):
        print(f"{x:8.3f} | {ye:12.6f} | {yr:12.6f}")


def grafik_ciz(xs_euler, ys_euler, xs_rk4, ys_rk4, dosya_adi="cozum_grafigi.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(xs_euler, ys_euler, "o--", label="Euler Yöntemi", alpha=0.7)
    plt.plot(xs_rk4, ys_rk4, "o-", label="Runge-Kutta 4 (RK4)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Diferansiyel Denklem Çözümü: dy/dx = f(x, y)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(dosya_adi, dpi=150)
    print(f"\nGrafik '{dosya_adi}' olarak kaydedildi.")
    plt.show()  # grafiği ekranda açar.


if __name__ == "__main__":
    xs_e, ys_e = euler_yontemi(f, x0, y0, x_son, h)
    xs_r, ys_r = rk4_yontemi(f, x0, y0, x_son, h)

    sonuclari_yazdir(xs_e, ys_e, xs_r, ys_r)
    grafik_ciz(xs_e, ys_e, xs_r, ys_r)