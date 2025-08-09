import sympy as sp

# Definir variables simbólicas
x, y = sp.symbols('x y')

# Expresión algebraica
expr = x**2 + 2*x + 1

# Expandir y factorizar
print("Factorización:", sp.factor(expr))
print("Expansión:", sp.expand((x + 1)**2))

# Derivar
print("Derivada:", sp.diff(expr, x))

# Integrar
print("Integral:", sp.integrate(expr, x))

# Resolver ecuaciones
ecuacion = sp.Eq(x**2 - 4, 0)
soluciones = sp.solve(ecuacion, x)
print("Soluciones:", soluciones)
