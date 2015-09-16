import pprint

def sortXvsY(data, index1, index2):
    if index1 or index2 >= len(data[0]):
        print 'Cannot Use Indices'
        return
    data = sorted(data, key = lambda x: x[index2])
    X = []
    Y = []
    [X.append(data[i][index1]) for i in range(len(data))]
    [Y.append(data[i][index2]) for i in range(len(data))]
    if index2 == 0:
        print 'Ranked by Name:'
    elif index2 == 1:
        print 'Ranked by Distance:\n'
    elif index2 == 2:
        print 'Ranked by Apparent Brightness:\n'
    elif index2 == 3:
        print 'Ranked by Absolute Brightness:\n'
    else:
        print 'Ranked by {:}:\n'.format(str(index2))
    pprint.pprint(X), pprint.pprint(Y)
    print
    

data2 = [
('Alpha Centauri A',    4.3,    0.26,       1.56),
('Alpha Centauri B',    4.3,    0.077,      0.45),
('Alpha Centauri C',    4.2,    0.00001,    0.00006),
("Barnard's Star",      6.0,    0.00004,    0.0005),
('Wolf 359',            7.7,    0.000001,   0.00002),
('BD +36 degrees 2147', 8.2,    0.0003,     0.006),
('Luyten 726-8 A',      8.4,    0.000003,   0.00006),
('Luyten 726-8 B',      8.4,    0.000002,   0.00004),
('Sirius A',            8.6,    1.00,       23.6),
('Sirius B',            8.6,    0.001,      0.003),
('Ross 154',            9.4,    0.00002,    0.0005),
]

sortXvsY(data2, 0, 1)
sortXvsY(data2, 0, 2)
sortXvsY(data2, 0, 3)
sortXvsY(data2, 4, 1)