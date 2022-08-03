while True:
    print("Selamat datang di Sate Pachill Pak Depe!")
    print("--------------------------------------------------------------")
    a = int(input("Masukkan jumlah pesanan yang ingin dibeli: "))
    b=[]
    if a >= 1:    
        for i in range (0,a):   
            print("--", "PESANAN", i+1, "--")
            print("Berapa banyak tusuk sate yang ingin dibeli (1 tusuk = 1800)")
            b.append(int(input("Berapa banyak jumlah tusuk sate yang ingin dibeli: ")))
        total=sum(b)
        print("\n--Ringkasan Pesanan--")
        print("Berikut ringkasan pesanan Sate Pachill kamu dari ", a, " pesanan")
        print("Jumlah tusuk sate yang di pesan : ", total)
        biaya=total*1800
        print("Biaya yang harus dibayar sebesar", biaya)
        
        print("\n--BAYAR--")
        def checkout():
            uang=int(input("Masukkan jumlah pembayaran anda (dalam rupiah): "))
            if uang < biaya and uang > 1:
                    print("Maaf uang anda tidak cukup")
                    checkout()
            elif uang == biaya and uang > 1:
                    print("Terima Kasih, Selamat menikmati Sate Pachill Anda!")
            elif uang > biaya and uang > 1:
                    print("Terima Kasih, Selamat menikmati Sate Pachill Anda! \nTotal Kembalian Anda adalah Rp ", uang-biaya)
            else:
                print("uang masa minus!!!")
                return checkout()
        checkout()
        maulagi=input("Apakah anda ingin memesan lagi (iya/tidak)")
        if maulagi.lower()=="iya":
            continue
        print("\nTerima kasih telah makan di Sate Pachill Pak Depe!")
        break

    else:
        print("Mesen makanan masa minus!!!")