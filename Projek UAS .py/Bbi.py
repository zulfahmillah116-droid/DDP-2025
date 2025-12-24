# ==================================================
# Aplikasi Penghitung Berat Badan Ideal Berbasis Python
# Menggunakan Streamlit
# ==================================================

import streamlit as st  # MODULE

# ------------------ CSS THEME ------------------
st.markdown("""
<style>
/* ================= BACKGROUND ================= */
.stApp {
    background: linear-gradient(135deg, #e5e7eb, #d1d5db);
    font-family: 'Segoe UI', sans-serif;
    color: #111827;
}

/* ================= HEADINGS ================= */
h1 {
    color: #000000;
    text-align: center;
    font-weight: 700;
}
h2, h3 {
    color: #000000;
}

/* ================= SIDEBAR ================= */
section[data-testid="stSidebar"] {
    background-color: #9ca3af;
}
section[data-testid="stSidebar"] * {
    color: #000000 !important;
    font-weight: 500;
}

/* ================= INPUT & SELECTBOX ================= */
input {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 10px !important;
}
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 10px !important;
}
div[data-baseweb="select"] span {
    color: #000000 !important;
}
div[data-baseweb="menu"] * {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* ================= BUTTON ================= */
.stButton > button {
    background-color: #000000;
    color: #ffffff;
    border-radius: 14px;
    padding: 10px 22px;
    font-size: 16px;
    border: none;
}
.stButton > button:hover {
    background-color: #1f2937;
}
</style>
""", unsafe_allow_html=True)

# ------------------ FUNCTION ------------------
def hitung_bbi(jenis_kelamin, tinggi_cm):
    tinggi_m = tinggi_cm / 100
    if jenis_kelamin == "Laki-laki":
        bbi = (tinggi_m * 100 - 100) - ((tinggi_m * 100 - 100) * 0.10)
    else:
        bbi = (tinggi_m * 100 - 100) - ((tinggi_m * 100 - 100) * 0.15)
    return bbi

def kategori_bb(berat, bbi):
    if berat < bbi - 5:
        return "Kurus"
    elif berat > bbi + 5:
        return "Berlebih"
    else:
        return "Ideal"

# ------------------ HALAMAN ------------------
st.title("⚖ Aplikasi Penghitung Berat Badan Ideal")
st.write("Projek Mata Kuliah Dasar-Dasar Pemrograman")

# MENU / LOOPING
halaman = st.sidebar.selectbox(
    "Pilih Halaman",
    [
        "1. Beranda",
        "2. Hitung Berat Badan Ideal",
        "3. Hasil & Kategori",
        "4. Tips Kesehatan",
        "5. Tentang Aplikasi"   # ✅ Tambahan slide baru
    ]
)

# ------------------ VARIABLE ------------------
if "data" not in st.session_state:
    st.session_state.data = {}

# ------------------ LOGIKA IF ------------------
if halaman == "1. Beranda":
    st.subheader("👋 Selamat Datang")
    st.write("Aplikasi ini digunakan untuk menghitung berat badan ideal berdasarkan tinggi badan dan jenis kelamin.")
    st.image(
        "https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/p1/358/2024/11/28/Berat-Badan-2-1240746704.jpg",
        caption="Menjaga Berat Badan Ideal",
        use_container_width=True
    )

elif halaman == "2. Hitung Berat Badan Ideal":
    st.subheader("📥 Input Data Pengguna")
    nama = st.text_input("Masukkan Nama")
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=100, max_value=250)
    berat = st.number_input("Berat Badan (kg)", min_value=30, max_value=200)

    if st.button("Hitung"):
        bbi = hitung_bbi(jenis_kelamin, tinggi)
        kategori = kategori_bb(berat, bbi)
        st.session_state.data = {
            "nama": nama,
            "jenis_kelamin": jenis_kelamin,
            "tinggi": tinggi,
            "berat": berat,
            "bbi": bbi,
            "kategori": kategori
        }
        st.success("✅ Data berhasil dihitung, silakan buka halaman hasil")

elif halaman == "3. Hasil & Kategori":
    st.subheader("📊 Hasil Perhitungan")
    if st.session_state.data:
        data = st.session_state.data
        st.write(f"Nama: {data['nama']}")
        st.write(f"Jenis Kelamin: {data['jenis_kelamin']}")
        st.write(f"Tinggi Badan: {data['tinggi']} cm")
        st.write(f"Berat Badan: {data['berat']} kg")
        st.write(f"Berat Badan Ideal: {data['bbi']:.2f} kg")
        st.write(f"Kategori Berat Badan: {data['kategori']}")
    else:
        st.warning("⚠ Silakan isi data terlebih dahulu")

elif halaman == "4. Tips Kesehatan":
    st.subheader("💡 Tips Menjaga Berat Badan Ideal")
    tips = [
        "🥗 Konsumsi makanan bergizi seimbang",
        "💧 Minum air putih minimal 8 gelas per hari",
        "🏃‍♂ Rutin berolahraga minimal 30 menit",
        "😴 Tidur dan istirahat yang cukup",
        "🍽 Hindari makan berlebihan dan junk food"
    ]
    for tip in tips:
        st.write(tip)

elif halaman == "5. Tentang Aplikasi":
    st.subheader("ℹ Tentang Aplikasi")
    st.write("""
    *Aplikasi Penghitung Berat Badan Ideal* adalah aplikasi berbasis Python menggunakan *Streamlit* 
    yang dibuat untuk membantu pengguna mengetahui apakah berat badan mereka sudah ideal 
    berdasarkan tinggi badan dan jenis kelamin.

    ### 🔧 Fitur Utama:
    - Menghitung *Berat Badan Ideal (BBI)* dengan rumus Broca.
    - Menentukan kategori: *Kurus, Ideal, atau Berlebih*.
    - Menyediakan *Tips Kesehatan* untuk menjaga berat badan ideal.
    - Tampilan modern dengan tema sederhana dan elegan.

    ### 🎯 Tujuan:
    - Membantu pengguna memahami kondisi tubuh mereka.
    - Memberikan edukasi tentang pentingnya menjaga berat badan ideal.
    - Menjadi projek pembelajaran mata kuliah *Dasar-Dasar Pemrograman*.

    ### 👩‍💻 Teknologi:
    - *Python*
    - *Streamlit*
    - *CSS Custom Theme*
    """)