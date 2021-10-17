import streamlit as st
from joblib import load
import pandas as pd
from PIL import Image

from entities import AtBat
from entities.form import Form
from interfaces.view.label import PITCH_TYPES, THROWS
from usecase.bat import Bat

st.write('# オオタニサン本塁打予測 :baseball:')
st.write('オオタニサンがホームランを打てるボールか占ってみよう')
# サイドバーを使ってみる

st.sidebar.markdown(
    """
    # ボールを決める
    """
)

p_throw = st.sidebar.selectbox(
    "利き腕",
    THROWS.keys(),
    format_func=lambda x: THROWS[x]
)

pitch_speed = st.sidebar.slider(
    '球速（km/h）', 70, 170, 150, 5
)

pitch_type = st.sidebar.selectbox(
    "球種",
    PITCH_TYPES.keys(),
    format_func=lambda x: PITCH_TYPES[x]
)
# 球種の検索用にkm/h -> mp/h変換
pitch_speed_mph = round(pitch_speed / 1.609, 1)

# 入力値を一旦書き出す
st.write('## 投球・球種・球速')
st.write(
    f"""
    - {p_throw}(name: {THROWS.get(p_throw)})
    - {pitch_speed} km/h({pitch_speed_mph} mph)
    - {pitch_type}(name: {PITCH_TYPES.get(pitch_type, 'Unknown')})
    """
)

# 結果を予測する

model = load('model/ohtani_hr_model_app.joblib')


atbat = AtBat.READY

usecase = Bat(model=model)
df = pd.read_csv('dataset/predict_shohei_ohtani_features03_app_dataset.csv')

st.write('## 結果')

# 確率を出す
if st.sidebar.button('投げる'):
    form = Form(pitch_type=pitch_type, throws=p_throw, pitch_speed_kmh=pitch_speed,
                pitch_speed_mph=pitch_speed_mph)
    atbat = usecase.predict_hr(form=form, df=df)

    if atbat == AtBat.READY:
        st.image(Image.open('assets/img/baseball_homerun_yokoku.png'), caption='勝負')
    elif atbat == AtBat.HOME_RUN:
        st.image(Image.open('assets/img/baseball_homerun_man.png'), caption='オオタニサン！')
    else:
        st.image(Image.open('assets/img/baseball_strike_man.png'), caption='残念')
else:
    # リセット
    atbat = AtBat.READY
    st.image(Image.open('assets/img/baseball_homerun_yokoku.png'), caption='勝負')
