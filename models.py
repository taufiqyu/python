from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    temas = db.relationship('Tema', backref='category', lazy=True)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_superadmin = db.Column(db.Boolean, default=False)
    undangan_id = db.Column(db.Integer, db.ForeignKey('undangan.id'), nullable=True)
    undangan = db.relationship('Undangan', backref='admin', lazy=True, uselist=False)

class Tema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False, unique=True)
    template_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    undangan = db.relationship('Undangan', backref='tema_ref', lazy=True)

class Undangan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    tema_id = db.Column(db.Integer, db.ForeignKey('tema.id'), nullable=False)
    tema = db.relationship('Tema', backref='undangans', lazy=True)
    nama_mempelai = db.Column(db.String(200), nullable=True)
    mempelai_pria = db.Column(db.String(100), nullable=True)
    bio_pria = db.Column(db.Text, nullable=True)
    ayah_pria = db.Column(db.String(100), nullable=True)
    ibu_pria = db.Column(db.String(100), nullable=True)
    instagram_pria = db.Column(db.String(100), nullable=True)
    mempelai_wanita = db.Column(db.String(100), nullable=True)
    bio_wanita = db.Column(db.Text, nullable=True)
    ayah_wanita = db.Column(db.String(100), nullable=True)
    ibu_wanita = db.Column(db.String(100), nullable=True)
    instagram_wanita = db.Column(db.String(100), nullable=True)
    tanggal_akad = db.Column(db.DateTime, nullable=True)
    tempat_akad = db.Column(db.String(100), nullable=True)
    lokasi_akad = db.Column(db.Text, nullable=True)
    maps_akad = db.Column(db.Text, nullable=True)
    tanggal_resepsi = db.Column(db.DateTime, nullable=True)
    tempat_resepsi = db.Column(db.String(100), nullable=True)
    lokasi_resepsi = db.Column(db.Text, nullable=True)
    maps_resepsi = db.Column(db.Text, nullable=True)
    penerima_kado = db.Column(db.String(100), nullable=True)
    alamat_kado = db.Column(db.Text, nullable=True)
    wa = db.Column(db.String(20), nullable=True)
    foto_pria = db.Column(db.String(200), nullable=True)
    foto_wanita = db.Column(db.String(200), nullable=True)
    audio = db.Column(db.String(200), nullable=True)
    bg_sampul = db.Column(db.String(200), nullable=True)
    bg_undangan = db.Column(db.String(200), nullable=True)
    tamu = db.relationship('Tamu', backref='undangan', lazy=True)
    rekening = db.relationship('Rekening', backref='undangan', lazy=True)
    galeri = db.relationship('Galeri', backref='undangan', lazy=True)
    cerita = db.relationship('Cerita', backref='undangan', lazy=True)

class Tamu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kode = db.Column(db.String(8), nullable=False, unique=True)
    undangan_id = db.Column(db.Integer, db.ForeignKey('undangan.id'), nullable=False)
    rsvp_status = db.Column(db.String(20), nullable=True)
    ucapan = db.Column(db.Text, nullable=True)
    waktu_rsvp = db.Column(db.DateTime, nullable=True)

class Rekening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_bank = db.Column(db.String(50), nullable=False)
    nomer_rekening = db.Column(db.String(50), nullable=False)
    atas_nama = db.Column(db.String(100), nullable=False)
    undangan_id = db.Column(db.Integer, db.ForeignKey('undangan.id'), nullable=False)

class Galeri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    alt = db.Column(db.String(200), nullable=True)
    undangan_id = db.Column(db.Integer, db.ForeignKey('undangan.id'), nullable=False)

class Cerita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    tanggal = db.Column(db.DateTime, nullable=True)
    isi = db.Column(db.Text, nullable=False)
    undangan_id = db.Column(db.Integer, db.ForeignKey('undangan.id'), nullable=False)