from models.buku_model import BukuModel

def test_get_all_buku():
    model = BukuModel()
    data = model.get_all_buku()
    
    # Memastikan bahwa hasil yang dikembalikan adalah sebuah list (berhasil mengambil data/terhubung ke DB)
    assert isinstance(data, list)