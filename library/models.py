from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

class Author(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
