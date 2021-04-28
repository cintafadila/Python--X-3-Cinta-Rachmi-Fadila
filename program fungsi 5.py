def penjumlahan( *vartuple ):
    print ("Jumlahnya adalah: ")
    jumlah = 0
    for var in vartuple:
        jumlah = jumlah + var
    print(jumlah)

def rata(*vartuple) :
    print("Rata-ratanya adalah : ")
    rerata = 0
    tot = 0
    for var in vartuple:
        tot = tot + var
    rerata = tot / len(vartuple)
    print(rerata)

penjumlahan( 35, 45, 87, 97 )
rata( 35, 45, 87, 97 )
