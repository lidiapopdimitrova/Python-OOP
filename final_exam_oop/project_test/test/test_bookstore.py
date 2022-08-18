from project_test.bookstore import Bookstore

from unittest import TestCase, main

class TestBookstore(TestCase):

    def test_store_init(self):
        bookstore = Bookstore(10)
        self.assertEqual(10, bookstore.books_limit)
        self.assertEqual({}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, bookstore._Bookstore__total_sold_books)

    def test_books_limit(self):
        with self.assertRaises(ValueError) as ex:
            bookst = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_books_limit2(self):
        with self.assertRaises(ValueError) as ex:
            bookst = Bookstore(-6)
        self.assertEqual("Books limit of -6 is not valid", str(ex.exception))

    def test_total_books_len(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 1)
        bookst.receive_book("TITLE2", 3)
        bookst.receive_book("TITLE3", 1)
        self.assertEqual(5, len(bookst))

    def test_receive_book_starting_check(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE1", 3)
        bookst.receive_book("TITLE2", 2)
        with self.assertRaises(Exception) as ex:
            bookst.receive_book("TITLE3", 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual(5, len(bookst))

    def test_total_number(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE1", 3)
        self.assertEqual(3, bookst.availability_in_store_by_book_titles["TITLE1"])

    def test_receive_book(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 1)
        message = bookst.receive_book("TITLE", 1)
        self.assertEqual("2 copies of TITLE are available in the bookstore.", message)
        self.assertEqual(2, bookst.availability_in_store_by_book_titles["TITLE"])

    def test_receive_a_book_again(self):
        bookst = Bookstore(5)
        message = bookst.receive_book("TITLE", 1)
        self.assertEqual("1 copies of TITLE are available in the bookstore.", message)
        with self.assertRaises(Exception) as ex:
            bookst.receive_book("NEW", 6)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))


    def test_recieve_book_is_too_much(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 1)
        with self.assertRaises(Exception) as ex:
            bookst.receive_book("TITLE", 10)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))


    def test_if_title_hasnt_been_in_the_store_yet(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 1)
        self.assertEqual(1, bookst.availability_in_store_by_book_titles["TITLE"])

    def test_sell_book_not_avaliable(self):
        bookst = Bookstore(5)
        with self.assertRaises(Exception) as ex:

            bookst.sell_book("TITLE", 1)
        self.assertEqual("Book TITLE doesn't exist!", str(ex.exception))

    def test_not_enoght_to_sell(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 1)
        with self.assertRaises(Exception) as ex:
            bookst.sell_book("TITLE", 5)

        self.assertEqual("TITLE has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sells_correctly(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 4)
        bookst.sell_book("TITLE", 2)
        self.assertEqual(2, bookst.availability_in_store_by_book_titles["TITLE"])
        self.assertEqual(2, bookst._Bookstore__total_sold_books)

    def test_sells(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 4)
        message = bookst.sell_book("TITLE", 2)
        self.assertEqual("Sold 2 copies of TITLE", message)

    def test_exist(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 4)
        with self.assertRaises(Exception) as ex:

            bookst.sell_book("OO", 1)
        self.assertEqual("Book OO doesn't exist!", str(ex.exception))

    def test_message_sells(self):
        bookst = Bookstore(5)
        bookst.receive_book("TITLE", 4)
        message = bookst.sell_book("TITLE", 2)
        self.assertEqual("Sold 2 copies of TITLE", message)

    def test_str(self):
        bookst = Bookstore(15)
        bookst.receive_book("TITLE", 4)
        bookst.receive_book("TITLE2", 1)
        bookst.receive_book("TITLE3", 2)

        result = str(bookst)
        expected = f"Total sold books: 0\n" + "Current availability: 7\n" + \
        f" - TITLE: 4 copies\n" + f" - TITLE2: 1 copies\n" + f" - TITLE3: 2 copies"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()