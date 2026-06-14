import streamlit as st
from PIL import Image

# إعدادات صفحة الموقع
st.set_page_config(page_title="ZEIN ZARKA AI", layout="centered")

# العنوان
st.title("📊 ZEIN ZARKA | AI Market Analyzer")
st.subheader("أهلاً بك في منصتك للتحليل الذكي")

# رفع الصورة
uploaded_file = st.file_uploader("ارفع صورة شاشة السوق هنا...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # عرض الصورة
    image = Image.open(uploaded_file)
    st.image(image, caption='تم رفع الصورة بنجاح', use_container_width=True)
    
    # زر التحليل
    if st.button('بدء التحليل'):
        st.write("---")
        st.success("جاري معالجة البيانات بواسطة نموذج ZEIN ZARKA AI...")
        st.info("التحليل قيد التطوير، انتظر التحديث القادم!")
