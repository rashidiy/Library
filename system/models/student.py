from .member import Member

class Student(Member):
    def __init__(self, name, member_id):
        """
        Student klassining konstruktor funksiyasi.
        
        Args:
            name (str): Talabaning ismi.
            member_id (str): Talabaning identifikatori.
        """
        super().__init__(name, member_id)

    def view_borrowed_books(self, library):
        """
        Talabaning qarzdorlikdagi kitoblarini ko'rsatadi.

        Args:
            library (Library): Kitoblar va tranzaktsiyalar bilan bog'liq ma'lumotlarni saqlovchi kutubxona ob'ekti.

        Returns:
            list: Qarzdorlikdagi kitoblar ro'yxati.
        """
        return super().view_borrowed_books(library)

    def max_books(self):
        """
        Talabaning maksimal qarzga olishi mumkin bo'lgan kitoblar sonini qaytaradi.

        Returns:
            int: Maksimal qarzga olishi mumkin bo'lgan kitoblar soni (3).
        """
        return 3

    def to_dict(self):
        """
        Student ob'ektini lug'at (dictionary) formatiga o'tkazadi.
        
        Returns:
            dict: Student ma'lumotlarini o'z ichiga olgan lug'at.
        """
        return {
            "name": self.name,  # Talabaning ismi
            "member_id": self.member_id,  # Talabaning identifikatori
            "borrowed_books": [book.ISBN for book in self.borrowed_books]  # Qarzdorlikdagi kitoblarning ISBN raqamlari
        }
