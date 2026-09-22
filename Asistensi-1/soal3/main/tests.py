from django.test import TestCase
from django.urls import reverse
from unittest import skip

from main.models import Book


class BookCatalogTest(TestCase):
    def setUp(self):
        # TODO 1: buat satu buku berjudul "Django Dasar", penulis "Alya", stok 2,
        # lalu simpan objeknya pada self.book.
        self.book = Book.objects.create(title="Django Dasar", author="Alya", stock=2)

    def test_book_availability(self):
        # TODO 2: pastikan buku pada setUp tersedia.
        self.assertTrue(self.book.is_available)

    def test_book_list_uses_correct_template(self):
        # TODO 3: request named route main:book_list, lalu periksa status 200
        # dan template main/book_list.html.
        response = self.client.get(reverse("main:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/book_list.html")

    def test_book_data_appears_on_page(self):
        # TODO 4: pastikan judul, penulis, dan teks "Tersedia" muncul di response.
        response = self.client.get(reverse("main:book_list"))
        self.assertContains(response, "Django Dasar")
        self.assertContains(response, "Alya")
        self.assertContains(response, "Tersedia")

    def test_empty_book_list(self):
        # TODO 5: hapus semua Book, request halaman katalog, lalu pastikan teks
        # "Belum ada buku." muncul dan "Django Dasar" tidak muncul.
        Book.objects.all().delete()
        response = self.client.get(reverse("main:book_list"))
        self.assertContains(response, "Belum ada buku.")
        self.assertNotContains(response, "Django Dasar")

    def test_stock_change_updates_availability(self):
        # BONUS: hapus decorator @skip, ubah stock self.book menjadi 0, simpan,
        # lalu pastikan is_available False dan halaman menampilkan "Stok habis".
        self.book.stock = 0
        self.book.save()
        self.book.refresh_from_db()
        self.assertFalse(self.book.is_available)
        response = self.client.get(reverse("main:book_list"))
        self.assertContains(response, "Stok habis")
