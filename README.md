# Basit Diferansiyel Denklem Çözücü

Birinci dereceden bir diferansiyel denklemi
    dy/dx = f(x, y),   y(x0) = y0
sayısal olarak çözen Python kodu. **Euler** ve **Runge-Kutta 4** yöntemlerini karşılaştırır.

## Dosyalar
- `diferansiyel_cozucu.py` Sonuç tablosunu yazdırır ve grafiğini çizer (matplotlib gerektirir).

## Kullanım

### Python
```bash
pip install matplotlib
python diferansiyel_cozucu.py
```

## Kendi denkleminizi çözmek için
Dosyanın başında:
- `f(x, y)` fonksiyonunu (denkleminizin dy/dx = ... şeklindeki sağ tarafı),
- `x0`, `y0` (başlangıç koşulu),
- `x_son` (çözümün hesaplanacağı son nokta),
- `h` (adım büyüklüğü)
değerlerini değiştirmeniz yeterlidir.

### Örnek: y' + 3y = 5, y(0) = 1
```
def f(x, y):
    return 5 - 3*y

x0 = 0.0
y0 = 1.0
x_son = 2.0
h = 0.1
```
