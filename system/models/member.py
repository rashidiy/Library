class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        """
        Member klassining konstruktor funksiyasi.
        
        Args:
            name (str): A'zoning ismi.
            member_id (str): A'zoning identifikatori.
            borrowed_books (list of Book, optional): Qarzdorlikdagi kitoblar ro'yxati. Agar berilmasa, bo'sh ro'yxat bo'ladi.
        """
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books or []

    def borrow_book(self, book):
        """
        Kitobni qarzga olish jarayonini amalga oshiradi.
        
        Args:
            book (Book): Qarzdorlikka olinayotgan kitob.
        
        Returns:
            bool: Kitob muvaffaqiyatli qarzga olingan bo'lsa True, aks holda False.
        """
        if len(self.borrowed_books) < self.max_books() and book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        """
        Kitobni qaytarish jarayonini amalga oshiradi.
        
        Args:
            book (Book): Qaytarilayotgan kitob.
        
        Returns:
            bool: Kitob muvaffaqiyatli qaytarilgan bo'lsa True, aks holda False.
        """
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                return True
        return False

    def view_borrowed_books(self, library):
        """
        A'zoning qarzdorlikdagi kitoblarini ko'rsatadi.
        
        Args:
            library (Library): Kitoblar va tranzaksiyalarni o'z ichiga olgan kutubxona obyekti.
        
        Returns:
            list of Book: Qarzdorlikdagi kitoblar ro'yxati.
        """
        borrowed_books = [transaction.book for transaction in library.transactions
                          if transaction.member == self and transaction.return_date is None]
        return borrowed_books

    def max_books(self):
        """
        A'zo maksimal qancha kitob qarzga olishi mumkinligini aniqlaydi.
        
        Raises:
            NotImplementedError: Agar bu metod chaqirilsa, xatolik yuz beradi, chunki konkret klassda aniqlanishi kerak.
        """
        raise NotImplementedError

    def to_dict(self):
        """
        Member ob'ektini lug'at (dictionary) formatiga o'tkazadi.
        
        Returns:
            dict: Member ma'lumotlarini o'z ichiga olgan lug'at.
        """
        return {
            "name": self.name,  # A'zoning ismi
            "member_id": self.member_id,  # A'zoning identifikatori
            "borrowed_books": [book.ISBN for book in self.borrowed_books]  # Qarzdorlikdagi kitoblarning ISBN raqamlari
        }
