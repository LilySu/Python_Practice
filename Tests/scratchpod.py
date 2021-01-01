import numpy as np

def transform_image(array, shift):
    print(array)
    # return np.rot90(array)
    # print(np.flip(array, 0))
    # print(np.roll(array, 3))

    # n = [row[-shift::] + row[:-shift] for row in array]
    #     # n.append(a)
    # print(n)

    np.random.seed(0)
    # i = np.random.randint(0, initial, size = (4,4))
    # print(np.random.randint(0, 0.5, size = (4,4)))
    noise = np.random.normal(0, 0.05, ((len(array))**2))
    print(noise)
    b = []
    for row in array:
        for element in row:
            for no in noise:
                a.append(element + no)
        if len(a) == len(array):
            b.append(a)
            a = []

    print(b)


array = [[0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0]]


print(transform_image(array, 1))