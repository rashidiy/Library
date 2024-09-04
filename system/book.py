class Book:
    def __init__(self, title, author, ISBN, publication_year, available):
        """
        Kitob obyekti yaratish uchun konstruktor funksiyasi. 
        Kitobning nomi, muallifi, ISBN, nashr yili va mavjudligi parametrlarini qabul qiladi.
        
        Args:
            title (str): Kitobning nomi.
            author (str): Kitobning muallifi.
            ISBN (str): Kitobning ISBN raqami.
            publication_year (int): Kitobning nashr yili.
            available (bool): Kitobning mavjudligi holati (True - mavjud, False - mavjud emas).
        """
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_year = publication_year
        self.available = available

    def borrow(self):
        """
        Kitobni qarzga olish funksiyasi. Agar kitob mavjud bo'lsa, uni qarzga olish imkonini beradi 
        va kitobning mavjudlik holatini yangilaydi.
        
        Returns:
            bool: Agar kitob muvaffaqiyatli qarzga olingan bo'lsa True, aks holda False.
        """
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """
        Kitobni qaytarish funksiyasi. Kitobni qaytarib, uning mavjudlik holatini yangilaydi.
        """
        self.available = True

    def to_dict(self):
        """
        Kitob obyekti ma'lumotlarini lug'at (dictionary) ko'rinishida qaytaradi.
        
        Returns:
            dict: Kitob ma'lumotlarini o'z ichiga olgan lug'at.
        """
        return {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "publication_year": self.publication_year,
            "available": self.available
        }
