import sys


def to_table(data, header=True, index=False):
    thead = ''
    d = []
    if header:
        # If include header, should be omit first element
        d = data[1:]
        # Generate thead if needed
        h = ''.join(['<th>{}</th>'.format(i) for i in data[0]])
        if index:
            thead = '<thead><tr><th></th>{}</tr></thead>'.format(h)
        else:
            thead = '<thead><tr>{}</tr></thead>'.format(h)
    else:
        d = data
    # Generate tbody
    tbody = '<tbody>'
    for k, j in enumerate(d):
        tbody += '<tr>'
        s = ['<td>{}</td>'.format(c) if not c == None else '<td></td>' for c in j]
        if index:
            tbody += '<td>{}</td>'.format(k + 1)
        tbody += ''.join(s)
        tbody += '</tr>'
    tbody += '</tbody>'

    return '<table>{0}{1}</table>'.format(thead, tbody)


if __name__ == "__main__":
    pass
  