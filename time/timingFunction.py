import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print(f'The result is {len(str(prod))} digits long')
print(f'Took {endTime - startTime} seconds to calculate.')
