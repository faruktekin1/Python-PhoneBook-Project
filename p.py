import os

class phoneBook:
    dosya_adı="phonebook.txt"
    def __init__(self):
        if not os.path.exists(self.dosya_adı):
            with open(self.dosya_adı,"w",encoding="utf-8") as f:
                pass
        
    def kişi_ekleme(self,name,surname,number):
        with open(self.dosya_adı,"a",encoding="utf-8") as f:
            f.write(f"{name},{surname},{number}\n")
        print(f"{name}{surname} is added")

    def del_name(self,silinecek_isim):
        with open(self.dosya_adı,"r",encoding="utf-8") as f:
            lines=f.readlines()
        with open(self.dosya_adı,"w",encoding="utf-8") as f:
            for i in lines:
                ilkad,ikinciad,no=i.strip().split(",")
                if ilkad==silinecek_isim:
                    print("İstediğiniz kişi silindi")
                else:
                    f.write(i)
    
    def kişi_listeleme(self):
        print("--------------")
        with open(self.dosya_adı,"r",encoding="utf-8") as f:
            new_lines=f.readlines()
            if not new_lines:
                print("Kişi listesi boş")
            else:
                for x in new_lines:
                    ilk_eleman,ikinci_eleman,üçüncü_eleman=x.strip().split(",")
                    
                    print(f"{ilk_eleman} {ikinci_eleman}--{üçüncü_eleman}")
                    




