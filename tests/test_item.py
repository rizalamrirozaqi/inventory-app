from app import tambah_item

def test_tambah_item_berhasil():
    assert tambah_item("Laptop", 5) == True