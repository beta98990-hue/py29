# class Kinozal:
#     def __init__(self, nomi, jami=0):
#         self.nomi = nomi
#         self.__jami = jami       
#         self.__band = []         
    
#     def band_qilish(self, raqam):
#         if raqam in self.__band:
#             print("allaqachon band!")
#         elif raqam > self.__jami or raqam < 1:
#             print("bunday joy yo'q!")
#         else:
#             self.__band.append(raqam)
#             print("band qilindi!")
    
#     def bekor_qilish(self, raqam):
#         if raqam in self.__band:
#             self.__band.remove(raqam)
#             print("bekor qilindi!")
    
#     def bosh_orinlar(self):
#         bosh = self.__jami - len(self.__band)
#         print(f"Hozirda bo'sh o'rinlar soni {bosh} ta")
    
#     def holat(self):
#         bosh = self.__jami - len(self.__band)
#         print(f"Kinozal nomi: {self.nomi}\nJami joylar: {self.__jami}\nBand joylar: {self.__band}\nBo'sh joylar: {bosh}")

# kinozal1 = Kinozal('Navo', 5)
# kinozal1.band_qilish(1)
# kinozal1.band_qilish(2)
# kinozal1.band_qilish(3)
# kinozal1.band_qilish(4)
# kinozal1.band_qilish(5)
# kinozal1.band_qilish(9)   
# kinozal1.bekor_qilish(1)
# kinozal1.bosh_orinlar()
# kinozal1.holat()





# class Abonement:
#     def __init__(self, azo, kirish_soni):
#         self.azo = azo
#         self.__qolgan = kirish_soni
#         self.__muzlatilgan = False
#         self.__muzlatish_ishlatilgan = False

#     def kirish(self):
#         if self.__muzlatilgan:
#             return "Abonement muzlatilgan!"
#         if self.__qolgan == 0:
#             return "Kirishlar tugagan!"
#         self.__qolgan -= 1
#         return f"{self.azo} kirdi, {self.__qolgan} ta qoldi"

#     def muzlatish(self):
#         if self.__muzlatish_ishlatilgan:
#             return "Muzlatish faqat 1 marta mumkin!"
#         self.__muzlatilgan = True
#         self.__muzlatish_ishlatilgan = True
#         return "Abonement muzlatildi!"

#     def eritish(self):
#         self.__muzlatilgan = False
#         return "Abonement eritildi!"

#     def uzaytirish(self, son):
#         if son > 0:
#             self.__qolgan += son
#             return f"{son} ta qo'shildi, endi {self.__qolgan} ta qoldi"
#         return "Faqat musbat son qo'shish mumkin!"

#     def holat(self):
#         return f"{self.azo}: {self.__qolgan} ta kirish qoldi"

# a = Abonement('Jasur', 2)
# a.kirish()
# a.muzlatish()
# a.kirish()
# a.eritish()
# a.muzlatish()
# a.kirish()
# a.kirish()
# print(a.kirish())
# print(a.muzlatish())
# print(a.kirish())
# print(a.eritish())
# print(a.muzlatish())
# print(a.kirish())
# print(a.kirish())
# print(a.holat())
