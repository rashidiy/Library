from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, book, member, borrow_date, return_date=None):
        """
        Transaction klassining konstruktor funksiyasi.
        
        Args:
            transaction_id (str): Transaction identifikatori.
            book (Book): Kitob obyekti.
            member (Member): A'zo obyekti.
            borrow_date (str or datetime): Qarzdorlik sanasi. Yoki string (YYYY-MM-DD formatida) yoki datetime obyekti.
            return_date (str or datetime, optional): Qaytarish sanasi. Yoki string (YYYY-MM-DD formatida) yoki datetime obyekti. Agar berilmasa, None bo'ladi.
        """
        self.transaction_id = transaction_id
        self.book = book
        self.member = member

        # Agar borrow_date string bo'lsa, uni datetime ob'ektiga o'tkazamiz
        if isinstance(borrow_date, str):
            self.borrow_date = datetime.strptime(borrow_date, '%Y-%m-%d')
        else:
            self.borrow_date = borrow_date

        # Agar return_date berilgan bo'lsa
        if return_date:
            # Agar return_date string bo'lsa, uni datetime ob'ektiga o'tkazamiz
            if isinstance(return_date, str):
                self.return_date = datetime.strptime(return_date, '%Y-%m-%d')
            else:
                self.return_date = return_date
        else:
            # Agar return_date berilmagan bo'lsa, None bo'ladi
            self.return_date = None

    def to_dict(self):
        """
        Transaction ob'ektini lug'at (dictionary) formatiga o'tkazadi.
        
        Returns:
            dict: Transaction ma'lumotlarini o'z ichiga olgan lug'at.
        """
        return {
            "transaction_id": self.transaction_id,
            "book": self.book.ISBN,  # Kitobning ISBN raqami
            "member": self.member.member_id,  # A'zoning identifikatori
            "borrow_date": self.borrow_date.strftime('%Y-%m-%d'),  # Qarzdorlik sanasi YYYY-MM-DD formatida
            "return_date": self.return_date.strftime('%Y-%m-%d') if isinstance(self.return_date, datetime) else None
            # Qaytarish sanasi yoki None
        }
