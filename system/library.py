import json
from datetime import datetime
from .book import Book
from system.models import Member
from system.transaction import Transaction


class Library:
    def __init__(self):
        """
        Kutubxona klassining konstruktor funksiyasi. 
        Kutubxona obyekti yaratishda kitoblar, a'zolar va tranzaksiyalarni yuklaydi.
        """
        self.books = self.load_books()  # Kitoblarni yuklash
        self.members = self.load_members()  # A'zolarni yuklash
        self.transactions = self.load_transactions()  # Tranzaksiyalarni yuklash

    def load_books(self):
        """
        Kitoblar ma'lumotlarini JSON fayldan yuklaydi va `Book` ob'ektlariga o'tkazadi.
        
        Returns:
            list of Book: Kutubxona kitoblarining ro'yxati.
        """
        with open('datas/books.json', 'r') as file:
            books_data = json.load(file)
        return [Book(**data) for data in books_data]

    def load_members(self):
        """
        A'zolar ma'lumotlarini JSON fayldan yuklaydi va `Member` ob'ektlariga o'tkazadi.
        
        Returns:
            list of Member: Kutubxona a'zolarining ro'yxati.
        """
        with open('datas/members.json', 'r') as file:
            members_data = json.load(file)
        return [Member(**data) for data in members_data]

    def load_transactions(self):
        """
        Tranzaksiyalar ma'lumotlarini JSON fayldan yuklaydi va `Transaction` ob'ektlariga o'tkazadi.
        
        Returns:
            list of Transaction: Kutubxona tranzaksiyalarining ro'yxati.
        """
        try:
            with open('datas/transactions.json', 'r') as file:
                transactions_data = json.load(file)
            transactions = []
            for data in transactions_data:
                book = next((b for b in self.books if b.ISBN == data["book"]), None)
                member = next((m for m in self.members if m.member_id == data["member"]), None)
                if book and member:
                    transactions.append(Transaction(
                        transaction_id=data["transaction_id"],
                        book=book,
                        member=member,
                        borrow_date=data["borrow_date"],
                        return_date=data["return_date"]
                    ))
            return transactions
        except json.JSONDecodeError:
            return []

    def add_book(self, book):
        """
        Yangi kitobni kutubxonaga qo'shadi va kitoblar faylini yangilaydi.
        
        Args:
            book (Book): Qo'shiladigan kitob obyekti.
        """
        self.books.append(book)
        self.save_books()

    def remove_book(self, book):
        """
        Kitobni kutubxonadan olib tashlaydi va kitoblar faylini yangilaydi.
        
        Args:
            book (Book): Olib tashlanadigan kitob obyekti.
        """
        self.books = [b for b in self.books if b.ISBN != book.ISBN]
        self.save_books()

    def save_books(self):
        """
        Kitoblarni JSON faylga saqlaydi.
        """
        with open('datas/books.json', 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def save_members(self):
        """
        A'zolarni JSON faylga saqlaydi.
        """
        with open('datas/members.json', 'w') as file:
            json.dump([member.to_dict() for member in self.members], file, indent=4)

    def save_transactions(self):
        """
        Tranzaksiyalarni JSON faylga saqlaydi.
        """
        with open('datas/transactions.json', 'w') as file:
            json.dump([transaction.to_dict() for transaction in self.transactions], file, indent=4)

    def borrow_book(self, book, member):
        """
        Kitobni qarzga oladi va tranzaksiyalar ro'yxatiga qo'shadi.
        
        Args:
            book (Book): Qarzdorlikka olinayotgan kitob obyekti.
            member (Member): Kitobni qarzga olayotgan a'zo obyekti.
        
        Returns:
            bool: Kitob muvaffaqiyatli qarzga olingan bo'lsa True, aks holda False.
        """
        transaction_id = len(self.transactions) + 1
        transaction = Transaction(
            transaction_id=transaction_id,
            book=book,
            member=member,
            borrow_date=datetime.now().strftime('%Y-%m-%d')
        )
        self.transactions.append(transaction)
        book.available = False
        self.save_books()
        self.save_transactions()
        return True

    def return_book(self, book, member):
        """
        Kitobni qaytaradi va tranzaksiyalar ro'yxatidagi qaytarilgan deb belgilaydi.
        
        Args:
            book (Book): Qaytarilayotgan kitob obyekti.
            member (Member): Kitobni qaytarayotgan a'zo obyekti.
        
        Returns:
            bool: Kitob muvaffaqiyatli qaytarilgan bo'lsa True, aks holda False.
        """
        transaction = next(
            (t for t in self.transactions if
             t.book.ISBN == book.ISBN and t.member.member_id == member.member_id and t.return_date is None),
            None
        )
        if transaction:
            transaction.return_date = datetime.now().strftime('%Y-%m-%d')
            book.available = True
            self.save_books()
            self.save_transactions()
            return True
        return False

    def get_member(self, id_: 'str'):
        for member in self.members:
            if member.member_id == id_:
                return member
        return None
