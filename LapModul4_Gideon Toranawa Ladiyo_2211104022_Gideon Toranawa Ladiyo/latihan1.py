username = "dee"
password = "awokawok"

login_att = 0

while login_att < 4:
    user1 = input("masukkan username : ")
    pass1 = input("masukkan password : ")
    
    if login_att == 3:
        print("Login gagal! silahkan coba lagi nanti!")
        break
        
    elif user1 == username and pass1 == password:
        print(f"Selamat datang {user1}!")
        break

    else:
        print("coba cek kembali, username dan password anda mungkin salah")
        login_att += 1