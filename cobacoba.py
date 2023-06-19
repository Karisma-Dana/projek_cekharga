
#print ('=====TITIK KORDINAT GRAFIK PUNGSI KUADRAT=====')

#print ("masukan angka variabel A,B, dan C. dari fungsi kuadar anda.\ncontoh : 2x² + 3x + 2 = 0 \nA = 2\nB = 3\nC = 2\n====================")
#VariableA = (float(input('masukan variable A = ')))
#VariableB = (float(input('masukan variable B = ')))
#VariableC = (float(input('masukan variable C = ')))

#deskriminan = (VariableB * VariableB)  - 4 * VariableA * VariableC 

#akardeskriminan = deskriminan ** 0.5 
#x1 = (-VariableB + akardeskriminan) / 2 * VariableA
#x2 = (-VariableB - akardeskriminan) / 2 * VariableA


#sumbusimen = (-VariableB) / (2*VariableA)
#ticakX = (-VariableB) / (2*VariableA)
#ticaky = (-deskriminan) / (4*VariableA)

#print ('==========HASIL==========')
#print ('Kordinat x1   = ',x1)
#print ('Kordinat x2   = ',x2)
#print ('Tipot Sumbu Y = ',VariableC)
#print ('Sumbu Simetri = ',sumbusimen)
#print ('Titik Puncak (',ticakX,',',ticaky,')')
#

#nama = 'dana ganteng'
#cek = 'da'
#status = cek in nama 
#print (str(status))

#print(max(nama))


#tono = 'kok ribet sih '
#print (tono + 'dana')
#print ('==========cek berat badan laki laki==========')
#masuk = float(input("masukan berat badan anda (CM): " ))
#laki_laki = (masuk - 100) - (masuk - 100) * 0.1 
#print (laki_laki, 'kg')


print("\tSELAMAT DATANG DI DENNA MART")
print("\t============================")
print(""" DAFTAR BUAH
1. semangka   6. mangga    11. stroberi 
2. apel       7. salak     12. jeruk
3. durian     8. pepaya
4. leci       9. anggur
5. manggis    10. alpukat 
""")

print ("SILAKAN CEK HARGA BUAH YANG AKAN ANDA BELI")
DATA1 = input('Nama Buah = ')
jumlah1 = input('Jumlah Belanjaan Anda = ')

def hasil ():
    barang = str(DATA1)
    banyak = int(jumlah1)

    if DATA1 == 'apel':
        harga_total = 4000*banyak
    elif DATA1 == 'semangka':
        harga_total = 3000*banyak
    elif DATA1 == 'salak':
        harga_total = 3500*banyak
    elif DATA1 == 'durian':
        harga_total = 5500*banyak
    elif DATA1 == 'pepaya':
        harga_total = 3800*banyak
    elif DATA1 == 'leci':
        harga_total = 2000*banyak
    elif DATA1 == 'anggur':
        harga_total = 5000*banyak
    elif DATA1 == 'manggis':
        harga_total = 2500*banyak
    elif DATA1 == 'mangga':
        harga_total = 4000*banyak
    elif DATA1 == 'jeruk':
        harga_total = 3900*banyak
    elif DATA1 == 'alpukat':
        harga_total = 4500*banyak
    elif DATA1 == 'stroberi':
        harga_total = 5200*banyak
    else : 
        harga_total = 10000
        
    return harga_total

harga_total = hasil()
print("Total belanjaan Anda adalah: {:,d} RUPIAH".format(harga_total))
print("\t============================\n\tpengecekan harga selesai")
print('    selamat berbelanja di DENNA MART\n \t     Have a good day')










