from django.db import models


class Book(models.Model):
    """Lengkapi model ini sesuai kontrak pada readme.txt."""

    # TODO 1: definisikan field title, author, dan stock.

    def __str__(self):
        # TODO 2: kembalikan judul buku.
        raise NotImplementedError

    @property
    def is_available(self):
        # TODO 3: buku tersedia hanya jika stock lebih besar dari nol.
        raise NotImplementedError

    @property
    def is_low_stock(self):
        # BONUS: True hanya jika stok berada pada rentang 1 sampai 3.
        raise NotImplementedError
