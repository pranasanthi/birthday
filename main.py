import streamlit as st
from PIL import Image

# Fungsi untuk memuat gambar dari file lokal
def load_image(file_path):
    return Image.open(file_path)

# Custom CSS untuk mempercantik font dan layout
st.markdown("""
    <style>
    .main {
        background-image: url('bg.jpg'); /* Path relative to your project folder */
        background-size: cover; /* Scale the background image to cover the entire screen */
        background-repeat: no-repeat; /* Prevent the background from repeating */
        background-position: center; /* Center the background image */
    }
    h1 {
        font-family: 'Comic Sans MS', sans-serif;
        color: #FF4500; /* Warna judul */
        text-align: center;
        font-size: 40px;
    }
    .birthday-msg {
        font-family: 'Caveat';
        font-size: 28px;
        color: #5C4033; /* Warna ucapan ulang tahun */
        text-align: center;
    }
    .wish {
        font-family: 'Caveat';
        font-size: 24px;
        color: #FF4500; /* Warna harapan */
        text-align: center;
        margin-top: -20px;
    }
    .treats {
        font-family: 'Comic Sans MS', sans-serif;
        font-size: 24px;
        color: #2E8B57; /* Warna bagian treat */
        text-align: center;
    }
    .confirm-button {
        background-color: #FF4500;
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 20px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown("<h1>🎉HAPPY BIRTHDAY GEKTU! 🎉</h1>", unsafe_allow_html=True)

# Ucapan ulang tahun dan harapan
st.markdown("""
<div class="birthday-msg">
    Congratulesyen tiup lilin yang ke-21 kali yahahaha🎂! Semoga tahun ini isinya full lucky 100000%🍀💫
</div>
""", unsafe_allow_html=True)

# Ilustrasi gambar balon dari file lokal
balloon_img = load_image(r"IMG_0248.JPG")
st.image(balloon_img, caption="🎂🎈MENAKLUKKAN DUNIA KEPALA DUAAA(R)🎂🎈", use_column_width=True)

# Bentuk dekoratif tambahan
st.markdown("<div style='text-align: center;'>🎁 🎉 🎊 🥳 🎁 🎉 🎊 🥳 🎁 🎉 🎊 🥳</div>", unsafe_allow_html=True)

# Halaman untuk memilih hadiah
st.markdown("<div class='treats'>Choose your treat today!!🎁</div>", unsafe_allow_html=True)

# Memuat gambar treat dari file lokal
latte_img = load_image(r"latte.jpg")
tiramisu_img = load_image(r"tiramisu.jpg")
sushi_img = load_image(r"sushi.jpg")

# Menampilkan gambar dalam kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.image(tiramisu_img, caption="Tiramisu cake🍰", use_column_width=True)
with col2:
    st.image(latte_img, caption="Seasalt latte☕", use_column_width=True)
with col3:
    st.image(sushi_img, caption="Sushi mentai🍣", use_column_width=True)

# Memilih treat
treats = ['Sushi mentai🍣', 'Seasalt latte☕', 'Tiramisu cake🍰']
choice = st.radio("", treats)

# Tombol untuk mengonfirmasi pilihan
if st.button("Confirm", key="confirm_button"):
    st.success(f"Got it, {choice} on the way! 🎁")

    # Memuat gambar tiket dan gambar lainnya
    ticket_img = load_image(r"ticket.jpg")
    right_img = load_image(r"IMG_0257.JPG")

    # Menampilkan gambar di kolom
    col_ticket, col_right = st.columns(2)

    # Mengubah ukuran gambar agar sama dengan gambar treat
    with col_ticket:
        if ticket_img is not None:
            st.image(ticket_img.resize((300, 300)), caption="Your Treat Ticket 🎫", use_column_width=True)
    with col_right:
        if right_img is not None:
            st.image(right_img.resize((300, 300)), caption="Cie ultah🎂🍰", use_column_width=True)

    # Pesan screenshot dan kirim via WhatsApp
    st.markdown("""
        <div style='text-align: center; font-family: "Comic Sans MS", sans-serif; font-size: 20px; color: #FF6347;'>
            Screenshot this ticket and send to me via WhatsApp! 📱
        </div>
    """, unsafe_allow_html=True)

# Bentuk dekoratif tambahan di bagian bawah
st.markdown("<div style='text-align: center;'>🎁 🎉 🎊 🥳 🎁 🎉 🎊 🥳 🎁 🎉 🎊 🥳</div>", unsafe_allow_html=True)
