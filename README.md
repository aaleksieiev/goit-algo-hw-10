# goit-algo-hw-10

# Обчислення визначеного інтеграла методом Монте-Карло

`f(x) = x^2 + x^3 + x^4` на інтервалі `[0.5, 2]`.


| Метод                          | Результат        
---------------------------------|-------------------
| Монте-Карло                    | 1.0674000000000001
| Quad                           | 1.06321

## Висновки

Експеримент показує наближення результату розрахованого за методом Монье-Карло до функції "quad" з підмодуля "integrate" бібліотеки SciPy. при збільшенні кількость точок. Метод монтекарло дає достатню точність при розрахунку визначеного інтегралу.