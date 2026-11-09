def test_create_book_success():
    """Проверяем, что книга с корректными данными создается."""
    def create_book(title, author, genre):
        if not title or not author:
            return None
        return {"title": title, "author": author, "genre": genre}
    
    book = create_book("Война и мир", "Толстой", "Роман")
    assert book is not None
    assert book["title"] == "Война и мир"

def test_create_book_empty_title():
    def create_book(title, author, genre):
        if not title or not author:
            return None
        return {"title": title, "author": author, "genre": genre}
    
    book = create_book("", "Толстой", "Роман")
    assert book is None
