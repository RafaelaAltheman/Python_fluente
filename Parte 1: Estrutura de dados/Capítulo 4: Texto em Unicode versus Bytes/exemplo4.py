# A string "El Niño" codificada com três codecs, gerando sequências de bytes muito diferentes


for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')