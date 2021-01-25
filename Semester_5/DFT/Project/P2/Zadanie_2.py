def huffman(freqtable):
    """
    Z racji, że w poprzednim puncie otrzymana czętość jest różna
    od wartości z instrukcji to przyjąłem wartości domyślne"""
    from collections import defaultdict 
    from heapq import heappush, heappop, heapify

    code = defaultdict(list)

    heap = [ ( freq, [ ltr ] ) for ltr,freq in freqtable.items() ]
    heapify(heap)

    while len(heap) > 1:
        freq0,letters0 = heappop(heap)
        for ltr in letters0:
            code[ltr].insert(0,'0')

        freq1,letters1 = heappop(heap)
        for ltr in letters1:
            code[ltr].insert(0,'1')

        heappush(heap, ( freq0+freq1, letters0+letters1))

    for k,v in code.items():
        code[k] = ''.join(v)

    return code

freqtable = dict(A=10,B=10,C=15,D=20,E=45)
print(sorted(huffman(freqtable).items()))