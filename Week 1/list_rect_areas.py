lengths = [1, 5, 2, 7, 9, 5, 3, 7]
widths = [9, 2, 1, 7, 5, 6, 4, 1]
areas = []
if len(lengths) == len(widths):
    for q in range(0, len(lengths)):
        areas.append(lengths[q] * widths[q])
    print(areas)
else:
    print('lengths of lists not the same')