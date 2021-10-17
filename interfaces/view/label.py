# アプリケーション上で使うラベル
from collections import OrderedDict

# TODO フロントエンドを実装する時はいらなくなるかもしれない

# 順番をちゃんと決めたいので敢えてOrderdDictで実装
THROWS = OrderedDict()
THROWS['R'] = '右'
THROWS['L'] = '左'

PITCH_TYPES = OrderedDict()
# まっすぐ系→次に早い系→遅い系の順番で
PITCH_TYPES['FF'] = '4シーム'
PITCH_TYPES['FT'] = '2シーム'
PITCH_TYPES['SI'] = 'シンカー'
PITCH_TYPES['FS'] = 'スプリット'
PITCH_TYPES['SL'] = 'スライダー'
PITCH_TYPES['SC'] = 'スクリュー'
PITCH_TYPES['CH'] = 'チェンジアップ'
PITCH_TYPES['CU'] = 'カーブ'
PITCH_TYPES['KN'] = 'ナックル'
PITCH_TYPES['KC'] = 'ナックルカーブ'
PITCH_TYPES['EP'] = '遅球（イーファス）'
