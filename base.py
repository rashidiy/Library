import time

from extra_func import make_menu
from system.models import Librarian, Member, Student, Teacher
from system.library import Library

library = Library()
Librarian(name="Alice", member_id="lib001")


class Base:
    existing_member: Member = None

    def run(self):
        member_id = input("Ro'yxatdan o'tilganlikni tekshirish uchun identifikatsiya raqamingizni kiriting: ")
        self.existing_member = library.get_member(member_id)
        if self.existing_member:
            print(f"Xush kelibsiz, {self.existing_member.name}!")
            self.show_main_menu()
        else:
            print("Siz ro'yxatdan o'tmagansiz. Iltimos, ro'yxatdan o'tish uchun variantni tanlang:")
            while True:
                print(make_menu(
                    title="Registratsiya",
                    **{
                        "1": "Talaba sifatida ro'yxatdan o'tish",
                        "2": "Ustoz sifatida ro'yxatdan o'tish"
                    }
                ))

                choice = input("Optsiya tanlang (1 or 2): ")

                if choice == "1":
                    name = input("Ismingizni kiriting: ")
                    self.existing_member = Student(name=name, member_id=member_id)
                    library.members.append(self.existing_member)
                    library.save_members()
                    print(f"Talaba sifatida ro'yxatdan o'tdi: {name}")
                    break

                elif choice == "2":
                    name = input("Ismingizni kiriting: ")
                    self.existing_member = Teacher(name=name, member_id=member_id)
                    library.members.append(self.existing_member)
                    library.save_members()
                    print(f"Ustoz sifatida ro'yxatdan o'tdi: {name}")
                    break

                else:
                    print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")
            self.show_main_menu()

    def show_main_menu(self):
        """
        Asosiy menyuni ko'rsatadi va foydalanuvchidan variantni tanlashni so'raydi.
        """
        while True:
            print(make_menu(
                title="Menu",
                **{
                    "1": "Kitoblarni ko'rish",
                    "2": "Kitobni qarzga olish",
                    "3": "Kitobni qaytarish",
                    "4": "Qarzga olingan kitoblarni ko'rish",
                    "5": "Chiqish"
                }
            ))

            choice = input("Optsiya tanlang (1-5): ")

            if choice == "1":
                self.view_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.view_borrowed_books()
            elif choice == "5":
                print("Dasturdan chiqilmoqda, kuting...")
                time.sleep(3)  # 5 soniya kutish
                print("Xayr, Salomat bo'ling!")
                break
            else:
                print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")

    @staticmethod
    def view_books():
        """
        Kitoblarni ko'rsatadi.
        """
        print("Kitoblar ro'yxati:")
        for book in library.books:
            availability = "Mavjud" if book.available else "Mavjud emas"
            print(f"{book.title} by {book.author} (ISBN: {book.ISBN}) - {availability}")

    def borrow_book(self):
        """
        Kitobni qarzga olish jarayonini boshqaradi.
        """
        isbn = input("Qarzga olish uchun kitobning ISBN raqamini kiriting: ")
        book = next((b for b in library.books if b.ISBN == isbn), None)
        if book and book.available:
            if library.borrow_book(book, self.existing_member):
                print(f"`{book.title}` kitobi qarzga olindi.")
            else:
                print("Kitobni qarzga olishda xatolik yuz berdi.")
        else:
            print("Bunday kitob mavjud emas yoki kitob allaqachon qarzga olingan.")

    def return_book(self):
        """
        Kitobni qaytarish jarayonini boshqaradi.
        """
        isbn = input("Qaytarish uchun kitobning ISBN raqamini kiriting: ")
        book = next((b for b in library.books if b.ISBN == isbn), None)
        if book and not book.available:
            if library.return_book(book, self.existing_member):
                print(f"{book.title} kitobi qaytarildi.")
            else:
                print("Kitobni qaytarishda xatolik yuz berdi.")
        else:
            print("Bunday kitob mavjud emas yoki kitob allaqachon qaytarilgan.")

    def view_borrowed_books(self):
        """
        Foydalanuvchining qarzga olingan kitoblarini ko'rsatadi va qaytarish imkoniyatini beradi.
        """
        borrowed_books = self.existing_member.view_borrowed_books(library)  # Pass `library`

        if borrowed_books:
            print("Sizning qarzga olingan kitoblaringiz:")
            for idx, book in enumerate(borrowed_books):
                print(f"{idx + 1}. {book.title} by {book.author} (ISBN: {book.ISBN})")

            while True:
                choice = input("Qaytarish uchun kitob raqamini kiriting yoki bekor qilish uchun '0' ni bosing: ")
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 0:
                        print("Qaytarish bekor qilindi.")
                        break
                    elif 1 <= choice <= len(borrowed_books):
                        selected_book = borrowed_books[choice - 1]
                        if self.existing_member.return_book(selected_book):
                            print(f"{selected_book.title} kitobi qaytarildi.")
                        else:
                            print("Kitobni qaytarishda xatolik yuz berdi.")
                        break
                    else:
                        print("Noto'g'ri raqam. Iltimos, qayta urinib ko'ring.")
                else:
                    print("Iltimos, raqam kiriting.")
        else:
            print("Hozirda qarzga olingan kitoblaringiz mavjud emas.")


base = Base()
