from .member import Member


class Teacher(Member):
    def __init__(self, name, member_id, borrowed_books=None):
        """
        Teacher klassining konstruktor funksiyasi.
        
        Args:
            name (str): O'qituvchining ismi.
            member_id (str): O'qituvchining identifikatori.
            borrowed_books (list of Book, optional): Qarzdorlikdagi kitoblar ro'yxati. Agar berilmasa, bo'sh ro'yxat bo'ladi.
        """
        super().__init__(name, member_id, borrowed_books)

    def to_dict(self):
        """
        Teacher ob'ektini lug'at (dictionary) formatiga o'tkazadi.
        
        Returns:
            dict: Teacher ma'lumotlarini o'z ichiga olgan lug'at.
        """
        return {
            "name": self.name,  # O'qituvchining ismi
            "member_id": self.member_id,  # O'qituvchining identifikatori
            "borrowed_books": [book.ISBN for book in self.borrowed_books]  # Qarzdorlikdagi kitoblarning ISBN raqamlari
        }
