from system.models import Member


class Librarian(Member):
    def __init__(self, name, member_id):
        """
        Kutubxona kutubxonachisi obyekti yaratish uchun konstruktor funksiyasi. 
        Kutubxonachi a'zo sifatida faqat ismi va a'zolik ID'si talab qilinadi.
        
        Args:
            name (str): Kutubxonachining ismi.
            member_id (str): Kutubxonachining a'zolik ID'si.
        """
        super().__init__(name, member_id)

    def add_book(self, book, library):
        """
        Kutubxonaga yangi kitob qo'shadi.
        
        Args:
            book (Book): Qo'shiladigan kitob obyekti.
            library (Library): Kitob qo'shiladigan kutubxona obyekti.
        """
        library.add_book(book)

    def remove_book(self, book, library):
        """
        Kutubxonadan kitob olib tashlaydi.
        
        Args:
            book (Book): Olib tashlanadigan kitob obyekti.
            library (Library): Kitob olib tashlanadigan kutubxona obyekti.
        """
        library.remove_book(book)

    def max_books(self):
        """
        Kutubxona kutubxonachisining qarzga olish mumkin bo'lgan maksimal kitoblar sonini belgilaydi.
        
        Returns:
            float: Cheksiz kitoblar sonini ifodalovchi qiymat.
        """
        return float('inf')
