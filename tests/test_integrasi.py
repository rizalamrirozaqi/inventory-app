from app import tambah_item, cek_stok

def test_tambah_dan_cek_stok():
    tambah_item("Mouse", 10)
    assert cek_stok("Mouse") == 10