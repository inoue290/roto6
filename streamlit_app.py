import streamlit as st
import numpy as np
import tensorflow as tf

# モデル読み込み（.keras ファイル）
model = tf.keras.models.load_model('lotto_model.keras')

st.title("ロト予測AI 🎯")
st.write("過去の傾向から次のロト6数字を予測します（※AI搭載用）")

# ボタンを押すと予測実行
if st.button("予測する"):
    # 仮の入力（例：ランダムな1行）※本来は実データで置き換えるべき
    dummy_input = np.random.randint(0, 2, size=(1, 43))  # 43個のワンホット

    prediction = model.predict(dummy_input)[0]
    top6 = prediction.argsort()[-6:][::-1]  # 上位6個を抽出
    numbers = sorted([int(i + 1) for i in top6])  # インデックス → ロト番号

    st.success(f"予測されたロト6数字: {numbers}")
