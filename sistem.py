from not_defteri import NotDefteri

def main():
    notebook = NotDefteri()

    while True:
        print("\n*** Not Defteri ***")
        print("1. Not Ekle")
        print("2. Notları Listele")
        print("3. Not Sil")
        print("4. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            content = input("Not içeriği: ")
            notebook.add_note(content)
        elif choice == "2":
            print("\nKaydedilmiş Notlar:")
            notebook.list_notes()
        elif choice == "3":
            content = input("Silinecek not içeriği: ")
            notebook.delete_note(content)
        elif choice == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
