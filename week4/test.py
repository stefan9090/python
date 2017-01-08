# Een bedrag gepast betalen met zo min mogelijk euromunten

bedrag = input ( 'Geef bedrag tussen 0 en 500 eurocent: ' )

for munt in [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]:
    aantal = 0
    bedrag = int(bedrag)
    while bedrag >= munt :
        aantal = aantal + 1
        bedrag = bedrag - munt
    
    if aantal > 0 :
        print (aantal, 'x', munt)
