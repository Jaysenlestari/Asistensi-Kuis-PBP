from django.db import models


class Book(models.Model):
    """Lengkapi model ini sesuai kontrak pada readme.txt."""

    # TODO 1: definisikan field title, author, dan stock.
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        # TODO 2: kembalikan judul buku.
        return self.title

    @property
    def is_available(self):
        # TODO 3: buku tersedia hanya jika stock lebih besar dari nol.
        return self.stock > 0

    @property
    def is_low_stock(self):
        # BONUS: True hanya jika stok berada pada rentang 1 sampai 3.
        return 1 <= self.stock <= 3
