import matplotlib.pyplot as plt

unit_price = 90

x = [ x for x in range(1, 11) ]
y = [ unit_price * y for y in x ]
plt.plot(x, y,'-*')
plt.title('relation between weight and price')
plt.xlabel('weight(kg)')
plt.ylabel('price($)')
plt.show()