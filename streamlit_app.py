import streamlit as st
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('lotto_model.keras')

st.title("ロト予測AI 🎯")
st.write("過去の傾向から次のロト6数字を予測します（※AI搭載用）")

# スマホ向けにフォントサイズを少し大きくしてみる（参考）
st.markdown("""
<style>
    @media (max-width: 600px) {
        h1 {
            font-size: 1.5rem !important;
        }
        p {
            font-size: 1.2rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

if st.button("予測する"):
    dummy_input = np.random.randint(0, 2, size=(1, 43))
    prediction = model.predict(dummy_input)[0]
    top6 = prediction.argsort()[-6:][::-1]
    numbers = sorted([int(i + 1) for i in top6])
    st.success(f"予測されたロト6数字: {numbers}")


