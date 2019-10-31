a, b, c = input().split()
d, e, f = input().split()
result = (float(c) * int(b)) + (float(f) * int(e))
print("VALOR A PAGAR: R$ {0:.2f}".format(result))
