import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="ZEIN ZARKA AI", layout="centered")

# الربط مع المفتاح السري الآمن
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("خطأ في إعداد المفتاح السري، تأكد من وضعه في إعدادات Streamlit Secrets.")

st.title("📊 ZEIN ZARKA | AI Market Analyzer")

uploaded_file = st.file_uploader("ارفع صورة شاشة السوق هنا...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة المرفوعة', use_container_width=True)
    
    if st.button('بدء التحليل'):
        with st.spinner('جاري التحليل الذكي بواسطة ZEIN ZARKA AI...'):
            try:
                response = model.generate_content([
                    "حلل هذا الرسم البياني للسوق، حدد الاتجاه العام، واذكر أهم مستويات الدعم والمقاومة.",
                    image
                ])
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء التحليل: {e}")
