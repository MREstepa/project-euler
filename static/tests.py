def pascal_generator(n):
    """
    Yield up to row ``n`` of Pascal's triangle, one row at a time.

    The first row is row 0.
    """
    def newrow(row):
        "Calculate a row of Pascal's triangle given the previous one."
        prev = 0
        for x in row:
            yield prev + x
            prev = x
        yield 1

    prevrow = [1]
    yield prevrow
    for x in range(n):
        prevrow = list(newrow(prevrow))
        yield prevrow


pascal_gen = pascal_generator(pow(10,9) - 1)
count = 0
for idx, line in enumerate(pascal_gen):
    print(idx)
    for x in line:
        if x % 7 != 0:
            count += 1

print(count)
