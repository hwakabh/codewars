import sys


def to_table(data, header=True, index=False):
    h = ''
    b = '<tbody>'
    if header:
        h += '<thead><tr>'
        if index:
            h += '<th></th>'
        for i in data[0]:
            h += '<th>{}</th>'.format(i)
        h += '</tr></thead>'
        for k, j in enumerate(data[1:]):
            b += '<tr>'
            s = ['<td>{}</td>'.format(c) if not c == None else '<td></td>' for c in j]
            if index:
                b += '<td>{}</td>'.format(k + 1)
            b += ''.join(s)
            b += '</tr>'
    else:
        for k, j in enumerate(data):
            b += '<tr>'
            s = ['<td>{}</td>'.format(c) if not c == None else '<td></td>' for c in j]
            if index:
                b += '<td>{}</td>'.format(k + 1)
            b += ''.join(s)
            b += '</tr>'
    b += '</tbody>'
    return '<table>{0}{1}</table>'.format(h, b)


if __name__ == "__main__":
    pass
  