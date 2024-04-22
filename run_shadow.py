#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        # NEW: инициализация полиэдра
        poly = Polyedr(f"data/{name}.geom")
        poly.draw(tk=tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        # NEW: вывод в консоль "суммы длин рёбер...""
        print("Сумма длин рёбер, середина и оба из концов которых —", end="")
        print(f" «хорошие» точки: {poly.good_sum}")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
