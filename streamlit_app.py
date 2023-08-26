import streamlit as st
import cv2
import numpy as np
import csv

def main():
    st.title("人口メッシュマップデータ抽出アプリ")

    uploaded_file = st.file_uploader("人口メッシュマップ画像をアップロード", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="アップロードされた画像", use_column_width=True)
        st.write("画像を処理してデータを抽出中...")

        # 画像データの読み込み
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        # 画像処理およびデータ抽出処理を実装
        # 以下に適切な画像処理コードを挿入

        # 座標と人口データのリストを想定
        coordinates = [(latitude1, longitude1, population1),
                       (latitude2, longitude2, population2),
                       # ... 他の座標と人口データ ...
                      ]

        # CSV ファイルにデータを書き込む
        csv_file = "extracted_data.csv"
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Latitude", "Longitude", "Population"])  # ヘッダー行
            for lat, lon, pop in coordinates:
                writer.writerow([lat, lon, pop])

        st.write("データを抽出し、ファイルに保存しました。")

if __name__ == "__main__":
    main()
