from datetime import datetime

DUMMY_UNDANGAN = {
    'slug': 'preview',
    'nama_mempelai': 'Budi & Ani',
    'mempelai_pria': 'Budi Santoso',
    'bio_pria': 'Lulusan Teknik Informatika, pecinta kopi.',
    'ayah_pria': 'Sutarno',
    'ibu_pria': 'Siti Aminah',
    'instagram_pria': 'https://instagram.com/budi_santoso',
    'foto_pria': 'images/dummy_pria.jpg',
    'mempelai_wanita': 'Ani Lestari',
    'bio_wanita': 'Desainer grafis, suka traveling.',
    'ayah_wanita': 'Hadi Wijaya',
    'ibu_wanita': 'Rina Susanti',
    'instagram_wanita': 'https://instagram.com/ani_lestari',
    'foto_wanita': 'images/dummy_wanita.jpg',
    'tanggal_akad': datetime(2025, 12, 25, 10, 0),
    'tempat_akad': 'Masjid Al-Hikmah',
    'lokasi_akad': 'Jl. Raya No. 123, Jakarta',
    'maps_akad': 'https://maps.google.com',
    'tanggal_resepsi': datetime(2025, 12, 25, 18, 0),
    'tempat_resepsi': 'Gedung Serbaguna',
    'lokasi_resepsi': 'Jl. Raya No. 456, Jakarta',
    'maps_resepsi': 'https://maps.google.com',
    'penerima_kado': 'Budi & Ani',
    'alamat_kado': 'Jl. Bahagia No. 789, Jakarta',
    'wa': '+6281234567890',
    'audio': 'audio/dummy_audio.mp3',
    'bg_sampul': 'images/dummy_sampul.jpg',
    'bg_undangan': 'images/dummy_undangan.jpg',
    'tema': {'nama': 'Minimalis'}
}

DUMMY_TAMU = {
    'nama': 'Tamu Preview',
    'kode': 'PREVIEW1',
    'rsvp_status': None,
    'ucapan': None,
    'waktu_rsvp': None
}

DUMMY_REKENING_LIST = [
    {'nama_bank': 'BCA', 'nomer_rekening': '1234567890', 'atas_nama': 'Budi Santoso'},
    {'nama_bank': 'Mandiri', 'nomer_rekening': '0987654321', 'atas_nama': 'Ani Lestari'}
]

DUMMY_GALERI_LIST = [
    {'url': 'images/dummy1.jpg', 'alt': 'Foto Prewedding 1'},
    {'url': 'images/dummy2.jpg', 'alt': 'Foto Prewedding 2'}
]

DUMMY_CERITA_LIST = [
    {'judul': 'Pertemuan Pertama', 'tanggal': datetime(2023, 1, 15), 'isi': 'Kami bertemu di kafe favorit.'},
    {'judul': 'Lamaran', 'tanggal': datetime(2024, 6, 20), 'isi': 'Budi melamar Ani di tepi pantai.'}
]