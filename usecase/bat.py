from interfaces.ml import DataFrame
from interfaces.ml.model import BatterModel
from entities import AtBat
from entities.form import Form


class Bat:

    def __init__(self, model: BatterModel):
        self.model = model

    def predict_hr(self, form: Form, df: DataFrame) -> AtBat:
        """
        本塁打かどうか予測する
        :param form: フォームの入力値
        :param df: 予測に使うデータセット
        :return: 打撃結果
        """
        # 欲しいデータのみに絞る
        df = df[df['game_date'].between('2021-08-01', '2021-11-30')]
        # 利き腕
        df = df[df['p_throws'] == form.throws]
        # カーブの時は2つの種別で見る
        if form.pitch_type == 'CU':
            pitch_types = ('CU', 'CS')
        else:
            pitch_types = (form.pitch_type,)
        df = df[df['pitch_type'].isin(pitch_types)]
        if len(df) == 0:
            # 0件だったらアウト
            return AtBat.OUTS
        # 球速で絞る
        df = df[df['release_speed'].between(form.pitch_speed_mph - 5, form.pitch_speed_mph + 5)]
        if len(df) == 0:
            # 0件だったらアウト
            return AtBat.OUTS
        # 予測する
        data = df[['scale_minmax_effective_speed', 'scale_minmax_pitch_type_id']]
        pre = self.model.predict_proba(data.to_numpy())[:, 1]
        # スコア結果を見て判定
        for r in pre:
            if float(r) >= 0.042 and float(r) < 0.043:
                return AtBat.HOME_RUN
            elif float(r) >= 0.0414 and float(r) < 0.0416:
                return AtBat.HOME_RUN
            elif float(r) >= 0.038 and float(r) < 0.0386:
                return AtBat.HOME_RUN
            elif float(r) >= 0.029 and float(r) < 0.029:
                return AtBat.HOME_RUN
        return AtBat.OUTS
