print("Liczby podzielne przez 5 oraz ich sześciany")
for i in range(100):
    if i % 5 == 0 and i != 0:
        print(i)
        print(i**3)
