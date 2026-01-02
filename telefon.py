from p import phoneBook
pb=phoneBook()

while True:
    print("Kişi listesi:")
    print("Kişi eklemek için 1'e bas:")
    print("Kişi silmek için 2'ye bas:")
    print("Kişileri listelemek için 3'e bas:")
    print("Çıkış için 4'e bas:")

    işlem=int(input("Yapmak istediğin işlem numarasını giriniz:"))

    if(işlem==1):
        isim=input("kişi adı:")
        soyad=input("kişi soyadı:")
        numara=input("kişi numarası:")

        pb.kişi_ekleme(isim,soyad,numara)
    elif(işlem==2):
        silenecek_isim=input("Silinecek ismi giriniz")
        pb.del_name(silenecek_isim)
    elif(işlem==3):
        pb.kişi_listeleme()
    elif(işlem==4):
        print("Çıkış yaptınız")
        break
    else:
        print("Geçersiz işlem")

