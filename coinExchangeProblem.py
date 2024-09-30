import os

coin = [1, 2, 5, 10]  # Coin awal
totalTargetCoin = 33   # Target total coin awal

def judul():
    print('''     
        ╔═╗╔═╗╦╔╗╔  ╔═╗═╗ ╦╔═╗╦ ╦╔═╗╔╗╔╔═╗╔═╗  ╔═╗╦═╗╔═╗╔╗ ╦  ╔═╗╔╦╗
        ║  ║ ║║║║║  ║╣ ╔╩╦╝║  ╠═╣╠═╣║║║║ ╦║╣   ╠═╝╠╦╝║ ║╠╩╗║  ║╣ ║║║
        ╚═╝╚═╝╩╝╚╝  ╚═╝╩ ╚═╚═╝╩ ╩╩ ╩╝╚╝╚═╝╚═╝  ╩  ╩╚═╚═╝╚═╝╩═╝╚═╝╩ ╩
    ''')

def solveCEP():
    solusiCoin = []
    coinTersedia = coin[:]  

    os.system("cls")
    while sum(solusiCoin) != totalTargetCoin:
        if not coinTersedia:  
            break
        
        maks = max(coinTersedia)
        if sum(solusiCoin) + maks <= totalTargetCoin:
            solusiCoin.append(maks)
        else:
            coinTersedia.remove(maks) 

    if sum(solusiCoin) == totalTargetCoin: 
        solusi_dict = {}
        for koin in solusiCoin:
            if koin in solusi_dict:
                solusi_dict[koin] += 1
            else:
                solusi_dict[koin] = 1
        
        print("Solusi Coin:")
        for koin, jumlah in solusi_dict.items():
            print(f"{koin} : {jumlah} keping")
    else:
        print("Tidak ada solusi yang ditemukan")

    print("")
    os.system("pause")
    menu()

def updateCoin():
    global coin
    os.system("cls")
    while True:
        coin_temp = input("Masukkan Coin yang Tersedia (Pisahkan dengan spasi, contoh: 1 2 5 10): ")
        try:
            coin_list = list(map(int, coin_temp.split()))
            if any(koin <= 0 for koin in coin_list):
                print("Nilai koin harus bilangan positif. Tidak ada nilai negatif atau nol yang diizinkan.")
            else:
                coin = coin_list
                os.system("cls")
                print(f"Coin berhasil diperbarui menjadi: {coin}")
                break
        except ValueError:
            print("Input tidak valid. Pastikan Anda hanya memasukkan angka. Silakan coba lagi.")

    print("")
    os.system("pause")
    menu()

def updateTargetCoin():
    global totalTargetCoin
    os.system("cls")
    while True:
        try:
            targetCoin_temp = int(input("Masukkan Target Coin: "))
            if targetCoin_temp <= 0:
                print("Target Coin harus lebih besar dari 0. Silakan coba lagi.")
            else:
                totalTargetCoin = targetCoin_temp
                os.system("cls")
                print(f"Target Coin diperbarui menjadi: {totalTargetCoin}")
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")

    print("")
    os.system("pause")
    menu()

def about():
    os.system("cls")
    print('''About:      
• Muhamad Afrian Suwandi - L0123087 - Sebelas Maret University
• Muhammad Rafli Werizky - L0123097 - Sebelas Maret University
    ''')

    os.system("pause")
    menu()

def exitProgram():
    os.system("cls")
    print("Terima kasih!! Semoga Selamat Dunia Akhirat")
    exit()

# Dictionary untuk opsi menu
opsiMenu = {
    "1": solveCEP,
    "2": updateCoin,
    "3": updateTargetCoin,
    "4": about,
    "5": exitProgram,
}

def menu():
    os.system("cls")
    judul()

    # Menampilkan nilai awal dan target coin
    print(f"Nilai Coin yang tersedia: {coin}")
    print(f"Target Jumlah Coin: {totalTargetCoin}")

    print("\n1. Solve Problem")
    print("2. Update Coin Values")
    print("3. Update Total Target Coin")
    print("4. About")
    print("5. Exit")

    pilihan = input("\nMasukkan pilihan (1 - 5): ")
    action = opsiMenu.get(pilihan)
    if action:
        action()
    else:
        print("Pilihan Tidak Valid")
        menu()

menu()
