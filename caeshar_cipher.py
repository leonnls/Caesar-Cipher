def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

def main():
    while True:
        print("\nCaesar Cipher:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            plain_text = input("Masukkan plaintext: ")
            shift = int(input("Masukkan jumlah pergeseran (angka): "))

            encrypted_text = caesar_encrypt(plain_text, shift)

            with open('encrypted_text.bin', 'w') as file:
                file.write(encrypted_text)

            print("Teks terenkripsi telah disimpan dalam file 'encrypted_text.bin'")
            input("Tekan Enter untuk melanjutkan...")
            # Membersihkan log terminal
            print("\033c")
        elif choice == '2':
            file_name = input("Masukkan nama file enkripsi beserta ekstensinya (contoh: encrypted_text.bin): ")

            try:
                with open(file_name, 'r') as file:
                    encrypted_text = file.read()
                    shift = int(input("Masukkan jumlah pergeseran (angka): "))
                    decrypted_text = caesar_decrypt(encrypted_text, shift)
                    print("Teks terdekripsi:", decrypted_text)
            except FileNotFoundError:
                print(f"File '{file_name}' tidak ditemukan.")
            except ValueError:
                print("Masukkan angka yang valid untuk jumlah pergeseran.")
            
            input("Tekan Enter untuk melanjutkan...")
            # Membersihkan log terminal
            print("\033c")
        elif choice == '3':
            print("Terima kasih telah menggunakan program Caesar Cipher. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()