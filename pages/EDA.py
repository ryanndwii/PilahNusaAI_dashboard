import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

.main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #061809 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background-color: #030f06 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.03) !important;
}

[data-testid="stSidebarNav"] {
    display: none !important;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff !important;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #8bb38f !important;
    font-weight: 400;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: #ffffff !important;
    margin-top: 35px;
    margin-bottom: 15px;
}

.insight-box {
    background-color: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(139, 179, 143, 0.15) !important;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.2);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.insight-box b {
    color: #ffffff !important;
    font-size: 16px;
    font-weight: 700;
}

.insight-box br {
    margin-bottom: 10px;
}

.insight-box div, .insight-box p, .insight-box li {
    color: #b8d4bb !important;
    line-height: 1.7;
    font-size: 15px;
}

.insight-box ul {
    margin-top: 10px;
    padding-left: 20px;
}

.stImage img {
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0px 12px 40px rgba(0, 0, 0, 0.4);
}

.footer {
    text-align: center;
    color: #537557;
    margin-top: 60px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h3 style='color: #ffffff; font-weight: 700; margin-top:10px; margin-bottom: 25px; letter-spacing: -0.5px;'>🌿 PilahNusa AI</h3>", unsafe_allow_html=True)
    
    menu_select = option_menu(
        menu_title=None,
        options=["Data Summary", "Exploratory Data Analysis", "Business Questions"],
        icons=["box", "bar-chart", "question-circle"],
        menu_icon="cast",
        default_index=1,
        styles={
            "container": {"padding": "0px !important", "background-color": "transparent"},
            "icon": {"color": "#8bb38f", "font-size": "15px"}, 
            "nav-link": {
                "font-size": "14px", 
                "text-align": "left", 
                "margin": "0px 0px 8px 0px", 
                "color": "#8bb38f",
                "background-color": "rgba(255, 255, 255, 0.03)",
                "border-radius": "12px",
                "font-weight": "500",
                "padding": "12px 16px"
            },
            "nav-link-selected": {
                "background-color": "#ffffff", 
                "color": "#061809", 
                "font-weight": "700",
                "box-shadow": "0px 8px 24px rgba(0, 0, 0, 0.4)"
            }
        }
    )
    
    if menu_select == "Data Summary":
        st.switch_page("app.py")
    elif menu_select == "Business Questions":
        st.switch_page("pages/Business_Questions.py")

st.markdown(
    '<div class="main-title">📊 Exploratory Data Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analisis karakteristik visual dataset klasifikasi sampah rumah tangga berbasis AI</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown('<div class="section-title">📈 Distribusi Dataset</div>', unsafe_allow_html=True)
col_img1, col_txt1 = st.columns([5, 4], gap="large")
with col_img1:
    st.image("charts/eda/distribusi_data.png", use_container_width=True)
with col_txt1:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Analisis:</b><br>
        <div>Distribusi yang cukup merata ini menunjukkan bahwa dataset memiliki kualitas yang baik untuk proses training model CNN karena dapat membantu mengurangi risiko bias terhadap kelas tertentu.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🎨 Dominant Color Analysis</div>', unsafe_allow_html=True)
col_img2, col_txt2 = st.columns([5, 4], gap="large")
with col_img2:
    st.image("charts/eda/dominant_color.png", use_container_width=True)
with col_txt2:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Analisis:</b><br>
        <div>Analisis channel RGB menunjukkan bahwa kategori B3 memiliki intensitas warna paling tinggi dan seimbang pada seluruh channel, sedangkan kategori Organik memiliki channel biru paling rendah yang menandakan dominasi warna alami seperti coklat dan hijau tua. Perbedaan distribusi warna ini menunjukkan bahwa warna dapat menjadi fitur visual awal yang membantu CNN mengenali pola antar kategori sampah.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">☀️ Brightness Analysis</div>', unsafe_allow_html=True)
col_img3, col_txt3 = st.columns([5, 4], gap="large")
with col_img3:
    st.image("charts/eda/brightness_mean.png", use_container_width=True)
with col_txt3:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Analisis:</b><br>
        <div>Kategori Organik memiliki rata-rata edge intensity tertinggi (48.12) dibanding Anorganik (30.37) dan B3 (26.69). Hal ini menunjukkan bahwa sampah organik memiliki tekstur dan pola tepi yang lebih kompleks akibat bentuk objek yang tidak beraturan. Kondisi ini mengindikasikan bahwa fitur tekstur dan edge kemungkinan menjadi salah satu fitur utama yang dimanfaatkan model CNN dalam membedakan jenis sampah.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🧩 Edge / Texture Analysis</div>', unsafe_allow_html=True)
col_img4, col_txt4 = st.columns([5, 4], gap="large")
with col_img4:
    st.image("charts/eda/edge_mean_per_class.png", use_container_width=True)
with col_txt4:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Analisis:</b><br>
        <div>Hasil analisis menunjukkan bahwa kategori B3 memiliki rata-rata brightness tertinggi (192.9), diikuti Anorganik (161.6) dan Organik (146.4). Perbedaan ini menunjukkan bahwa tiap kategori memiliki karakteristik pencahayaan yang berbeda, dimana sampah B3 cenderung memiliki permukaan lebih terang dan reflektif.</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown('<div class="section-title">📌 Ringkasan Analisis Karakteristik</div>', unsafe_allow_html=True)
st.markdown("""
<div class="insight-box">
    <b>📋 Kesimpulan Kualitas Visual Dataset:</b><br>
    <p>Berdasarkan hasil Exploratory Data Analysis (EDA), dataset klasifikasi sampah memiliki kualitas yang cukup baik untuk pengembangan model Computer Vision berbasis CNN. Dataset terdiri dari 9.241 gambar dengan distribusi data antar kelas yang relatif seimbang sehingga mampu mengurangi risiko bias selama proses training. Analisis brightness menunjukkan adanya perbedaan karakteristik pencahayaan antar kategori, sedangkan analisis channel warna memperlihatkan bahwa tiap kelas memiliki pola distribusi warna yang berbeda. Selain itu, hasil edge intensity menunjukkan bahwa tekstur dan kompleksitas bentuk objek menjadi salah satu karakteristik visual yang cukup dominan pada beberapa kategori sampah.</p>
    <p>Beberapa karakteristik penting yang ditemukan meliputi:</p>
    <ul>
        <li>Analisis brightness menunjukkan adanya perbedaan karakteristik pencahayaan antar kategori, dimana kelas B3 memiliki tingkat kecerahan paling tinggi dibanding kategori lainnya.</li>
        <li>Perbedaan distribusi channel warna (RGB) menunjukkan bahwa warna berpotensi menjadi fitur visual awal yang membantu model dalam mengenali pola antar jenis sampah.</li>
        <li>Kategori Organik memiliki nilai edge intensity tertinggi, yang menunjukkan bahwa tekstur dan kompleksitas bentuk objek kemungkinan menjadi fitur paling penting dalam proses klasifikasi oleh model CNN.</li>
        <li>ombinasi fitur warna, brightness, dan edge menunjukkan bahwa proses klasifikasi sampah memerlukan lebih dari satu karakteristik visual agar model dapat bekerja secara optimal.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
🌿 PilahNusaAI Dashboard • EDA Page
</div>
""", unsafe_allow_html=True)