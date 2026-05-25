import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Business Questions",
    page_icon="📈",
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

.question-title {
    font-size: 20px;
    font-weight: 700;
    color: #ffffff !important;
    margin-top: 35px;
    margin-bottom: 15px;
    line-height: 1.4;
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
        default_index=2,
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
    elif menu_select == "Exploratory Data Analysis":
        st.switch_page("pages/EDA.py")

st.markdown(
    '<div class="main-title">📈 Business Questions Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analisis pertanyaan bisnis berdasarkan karakteristik visual dataset</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown('<div class="question-title">1️⃣ Fitur visual apa yang paling berpotensi digunakan model dalam membedakan jenis sampah?</div>', unsafe_allow_html=True)
col_img1, col_txt1 = st.columns([5, 4], gap="large")
with col_img1:
    st.image("charts/business_questions/feature_comparison.png", use_container_width=True)
with col_txt1:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Strategis:</b><br>
        <div>Hasil analisis menunjukkan bahwa fitur tekstur (edge) memiliki nilai variasi yang jauh lebih tinggi (17.38) dibanding fitur warna (5.83). Hal ini mengindikasikan bahwa model CNN kemungkinan lebih banyak memanfaatkan pola tekstur, bentuk tepi, dan kompleksitas visual objek dibanding hanya distribusi warna dalam proses klasifikasi sampah.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="question-title">2️⃣ Apakah terdapat indikasi bias akibat perbedaan pencahayaan atau kompleksitas visual?</div>', unsafe_allow_html=True)
col_img2, col_txt2 = st.columns([5, 4], gap="large")
with col_img2:
    st.image("charts/business_questions/brightness_edge_comparison.png", use_container_width=True)
with col_txt2:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Strategis:</b><br>
        <div>Hasil analisis menunjukkan adanya perbedaan brightness dan edge antar kategori, dimana kelas B3 memiliki brightness tertinggi (192.9) sedangkan kelas Organik memiliki edge intensity tertinggi (48.1). Meskipun terdapat variasi karakteristik visual, perbedaannya masih berada pada rentang yang wajar dan tidak menunjukkan ketimpangan ekstrem.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="question-title">3️⃣ Apakah terdapat overlap antar kelas berdasarkan fitur brightness dan edge?</div>', unsafe_allow_html=True)
col_img3, col_txt3 = st.columns([5, 4], gap="large")
with col_img3:
    st.image("charts/business_questions/overlap_brightness.png", use_container_width=True)
with col_txt3:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Strategis:</b><br>
        <div>Hasil visualisasi menunjukkan adanya overlap distribusi brightness antar beberapa kategori, terutama pada rentang nilai menengah hingga tinggi. Kondisi ini mengindikasikan bahwa sebagian kelas memiliki karakteristik kecerahan yang saling mirip sehingga fitur brightness saja belum cukup diskriminatif untuk memisahkan seluruh kategori sampah secara optimal</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="question-title">4️⃣ Seberapa konsisten karakteristik visual dalam masing-masing kelas?</div>', unsafe_allow_html=True)
col_img4, col_txt4 = st.columns([5, 4], gap="large")
with col_img4:
    st.image("charts/business_questions/consistency_cv.png", use_container_width=True)
with col_txt4:
    st.markdown("""
    <div class="insight-box">
        <b>💡 Insight Strategis:</b><br>
        <div>Hasil analisis coefficient of variation (CV) menunjukkan bahwa nilai brightness pada seluruh kategori memiliki variasi yang relatif rendah dibanding edge, sehingga pencahayaan dataset cenderung cukup konsisten di dalam masing-masing kelas. Sementara itu, fitur edge memiliki variasi yang lebih tinggi, terutama pada kategori Anorganik, yang menunjukkan adanya keragaman bentuk dan tekstur objek pada kelas tersebut.<div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown('<div class="question-title">📌 Kesimpulan Analisis Operasional</div>', unsafe_allow_html=True)
st.markdown("""
<div class="insight-box">
    <b>📋 Kesimpulan dan Temuan Business Question:</b><br>
    <p>Berdasarkan hasil analisis fitur visual pada dataset, dapat disimpulkan bahwa tekstur (edge) menjadi fitur yang paling berpengaruh dalam membedakan jenis sampah dibanding warna. Meskipun terdapat perbedaan brightness dan distribusi warna antar kategori, variasinya masih berada dalam batas yang wajar sehingga tidak menunjukkan indikasi bias visual yang ekstrem pada dataset. Analisis overlap juga menunjukkan bahwa beberapa kelas memiliki karakteristik brightness yang saling berdekatan, sehingga model CNN perlu memanfaatkan kombinasi fitur seperti tekstur, bentuk objek, dan pola tepi agar klasifikasi dapat dilakukan secara lebih optimal.</p>
    <ul>
        <li>Fitur tekstur/edge memiliki variasi paling tinggi sehingga diperkirakan menjadi fitur utama yang digunakan model CNN dalam membedakan jenis sampah.</li>
        <li>Perbedaan brightness antar kategori tidak terlalu ekstrem sehingga dataset tidak menunjukkan indikasi bias pencahayaan yang signifikan.</li>
        <li>Terdapat overlap pada distribusi brightness antar kelas, yang menandakan bahwa satu fitur saja belum cukup untuk melakukan klasifikasi secara optimal.</li>
        <li>Model klasifikasi kemungkinan akan bekerja lebih optimal jika memanfaatkan kombinasi fitur warna, brightness, tekstur, dan bentuk objek secara bersamaan.</li>
    </ul>
    <p>Hasil ini menegaskan bahwa kualitas visual dataset sangat mumpuni untuk mendukung deployment model computer vision PilahNusa AI ke tengah masyarakat.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    🌿 PilahNusaAI Dashboard • Business Questions Page
</div>
""", unsafe_allow_html=True)