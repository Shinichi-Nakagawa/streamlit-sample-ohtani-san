import pytest
from joblib import load

from entities import AtBat
from entities.form import Form
from usecase.bat import Bat
from interfaces.ml import DataFrame


@pytest.fixture
def usecase() -> Bat:
    model = load('./model/ohtani_hr_model_app.joblib')
    return Bat(model=model)


TESTCASE = [
    (Form(throws='R', pitch_speed_kmh=160, pitch_speed_mph=100, pitch_type='FF'), AtBat.HOME_RUN),
    (Form(throws='L', pitch_speed_kmh=150, pitch_speed_mph=93.2, pitch_type='FF'), AtBat.OUTS),
    (Form(throws='R', pitch_speed_kmh=145, pitch_speed_mph=90.1, pitch_type='SL'), AtBat.HOME_RUN),
    (Form(throws='L', pitch_speed_kmh=145, pitch_speed_mph=90.1, pitch_type='SI'), AtBat.HOME_RUN),
    (Form(throws='R', pitch_speed_kmh=135, pitch_speed_mph=83.9, pitch_type='SI'), AtBat.OUTS),
]


@pytest.mark.parametrize('form, result', TESTCASE)
def test_predict_hr(
        df: DataFrame,
        usecase: Bat,
        form: Form,
        result: AtBat
):
    """
    ホームラン判定
    :param df: データセット
    :param usecase: 判定モデル
    :param form: 入力値
    :param result: 結果
    """
    assert usecase.predict_hr(form, df) == result
