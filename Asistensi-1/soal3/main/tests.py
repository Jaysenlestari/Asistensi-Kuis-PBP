from django.test import TestCase
from django.urls import reverse
from unittest import skip

from main.models import Book


class BookCatalogTest(TestCase):
    def setUp(self):
        # TODO 1: buat satu buku berjudul "Django Dasar", penulis "Alya", stok 2,
        # lalu simpan objeknya pada self.book.
        self.fail("TODO 1 belum dikerjakan")

    def test_book_availability(self):
        # TODO 2: pastikan buku pada setUp tersedia.
        self.fail("TODO 2 belum dikerjakan")

    def test_book_list_uses_correct_template(self):
        # TODO 3: request named route main:book_list, lalu periksa status 200
        # dan template main/book_list.html.
        self.fail("TODO 3 belum dikerjakan")

    def test_book_data_appears_on_page(self):
        # TODO 4: pastikan judul, penulis, dan teks "Tersedia" muncul di response.
        self.fail("TODO 4 belum dikerjakan")

    def test_empty_book_list(self):
        # TODO 5: hapus semua Book, request halaman katalog, lalu pastikan teks
        # "Belum ada buku." muncul dan "Django Dasar" tidak muncul.
        self.fail("TODO 5 belum dikerjakan")

    @skip("Bonus belum dikerjakan; hapus decorator ini saat mengerjakan bonus")
    def test_stock_change_updates_availability(self):
        # BONUS: hapus decorator @skip, ubah stock self.book menjadi 0, simpan,
        # lalu pastikan is_available False dan halaman menampilkan "Stok habis".
        self.fail("Test bonus belum dikerjakan")
