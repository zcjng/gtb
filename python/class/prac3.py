def function(csv: str, indices: str):

    indexes = list(map(int, indices.split()))
    rows = csv.split('\n')

    total = []

    for i in rows:
        columns = i.split(',')
        selected = [columns[i] for i in indexes]
        total.append(','.join(selected))
    return '\n'.join(total)


csv = []
while True:
    try:
        lines = input()
        csv.append(lines)
    except EOFError:
        break

ind_line = csv[0]
csv_line = '\n'.join(csv[1:])

print(function(csv_line, ind_line))
