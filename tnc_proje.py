import os

# --- 1. BÖLÜM: CLASS (ROBOT) KODLARI ---
class YapilacaklarListesi:
    def __init__(self):
        self.dosya_adi = "todolist.txt"
        self.gorevler = []
        
        # Dosya yoksa oluştur, varsa oku listeye at
        if not os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, "w", encoding="utf-8") as f:
                pass
        else:
            with open(self.dosya_adi, "r", encoding="utf-8") as f:
                for satir in f:
                    self.gorevler.append(satir.strip())

    def gorev_ekleme(self, eklenecek_gorev):
        self.gorevler.append(eklenecek_gorev)
        with open(self.dosya_adi, "a", encoding="utf-8") as f:
            f.write(f"{eklenecek_gorev}\n")
        print(f"'{eklenecek_gorev}' başarıyla eklendi")

    def gorev_silme(self, silinecek_gorev):
        silinen = self.gorevler.pop(silinecek_gorev - 1)
        with open(self.dosya_adi, "w", encoding="utf-8") as f:
            for gorev in self.gorevler:
                f.write(f"{gorev}\n")
        print(f"'{silinen}' başarıyla silindi.")

    def gorev_duzenle(self, numara, yeni_metin):
        index = numara - 1
        if 0 <= index < len(self.gorevler):
            eski_metin = self.gorevler[index]
            self.gorevler[index] = yeni_metin
            with open(self.dosya_adi, "w", encoding="utf-8") as f:
                for gorev in self.gorevler:
                    f.write(f"{gorev}\n")
            print(f"'{eski_metin}' görevi -> '{yeni_metin}' olarak güncellendi.")
        else:
            print("Hata: Girdiğiniz numarada bir görev yok!")

    def gorev_listeleme(self):
        if len(self.gorevler) == 0:
            print("Listelenecek görev yok.")
        else:
            for x, y in enumerate(self.gorevler, start=1):
                print(f"{x}. {y}")

# --- 2. BÖLÜM: ANA PROGRAM (KUMANDA) KODLARI ---

uygulama = YapilacaklarListesi()

while True:
    print("\nTO-DO LIST UYGULAMASINA HOŞGELDİNİZ:")
    print("1. Görev Ekle")
    print("2. Görev Sil")
    print("3. Görevleri Listele")
    print("4. Görev Düzenle")
    print("5. Çıkış")

    islem = input("Lütfen yapmak istediğiniz işlem numarasını giriniz (1-5): ")

    if islem == "1":
        eklenecek_gorev = input("Lütfen eklemek istediğiniz görevi giriniz: ").strip()
        if eklenecek_gorev:
            uygulama.gorev_ekleme(eklenecek_gorev)
        else:
            print("Boş görev eklenemez!")

    elif islem == "2":
        uygulama.gorev_listeleme() 
        try:
            silinecek_gorev = int(input("Silinecek görev numarası: "))
            uygulama.gorev_silme(silinecek_gorev)
        except ValueError:
            print("Lütfen bir sayı girin!")
        except IndexError:
            print("Geçersiz görev numarası!")

    elif islem == "3":
        uygulama.gorev_listeleme()

    elif islem == "4": 
        uygulama.gorev_listeleme() 
        try:
            girilen_no = int(input("Düzenlenecek görev numarası: "))
            yeni_icerik = input("Yeni görev metni: ").strip()
            
            if yeni_icerik:
                uygulama.gorev_duzenle(girilen_no, yeni_icerik)
            else:
                print("Görev metni boş olamaz!")
        except ValueError:
            print("Lütfen bir sayı girin!")

    elif islem == "5":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Lütfen geçerli işlem yapınız")