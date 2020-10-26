import os
import pandas as pd
import numpy as np

def load_chart_data_data(fpath):
    chart_data = pd.read_csv(fpath, thousands=',', header=None)
    chart_data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    return chart_data


def preprocess(chart_data):
    prep_data = chart_data
    windows = [5, 10, 20, 60, 120]
    for window in windows:
        prep_data['close_ma{}'.format(window)] = prep_data['close'].rolling(window).mean()
        prep_data['volume_ma{}'.format(window)] = (
            prep_data['volume'].rolling(window).mean())
    return prep_data


def build_training_data(prep_data):
    training_data = prep_data

    training_data['open_lastclose_ratio'] = np.zeros(len(training_data))
    training_data.loc[1:, 'open_lastclose_ratio'] = \
        (training_data['open'][1:].values - training_data['close'][:-1].values) / \
        training_data['close'][:-1].values
    training_data['high_close_ratio'] = \
        (training_data['high'].values - training_data['close'].values) / \
        training_data['close'].values
    training_data['low_close_ratio'] = \
        (training_data['low'].values - training_data['close'].values) / \
        training_data['close'].values
    training_data['close_lastclose_ratio'] = np.zeros(len(training_data))
    training_data.loc[1:, 'close_lastclose_ratio'] = \
        (training_data['close'][1:].values - training_data['close'][:-1].values) / \
        training_data['close'][:-1].values
    training_data['volume_lastvolume_ratio'] = np.zeros(len(training_data))
    training_data.loc[1:, 'volume_lastvolume_ratio'] = \
        (training_data['volume'][1:].values - training_data['volume'][:-1].values) / \
        training_data['volume'][:-1]\
            .replace(to_replace=0, method='ffill') \
            .replace(to_replace=0, method='bfill').values

    windows = [5, 10, 20, 60, 120]
    for window in windows:
        training_data['close_ma%d_ratio' % window] = \
            (training_data['close'] - training_data['close_ma%d' % window]) / \
            training_data['close_ma%d' % window]
        training_data['volume_ma%d_ratio' % window] = \
            (training_data['volume'] - training_data['volume_ma%d' % window]) / \
            training_data['volume_ma%d' % window]

    return training_data

# prepare data set
chart_data = data_manager.load_chart_data(
    os.path.join(settings.BASE_DIR,
                    'data/{}.csv'.format(stock_code)))
prep_data = data_manager.preprocess(chart_data)
training_data = data_manager.build_training_data(prep_data)

# chart data split
features_chart_data = ['date', 'open', 'high', 'low', 'close', 'volume']
chart_data = training_data[features_chart_data]

# training data set
features_training_data = [
    'open_lastclose_ratio', 'high_close_ratio', 'low_close_ratio',
    'close_lastclose_ratio', 'volume_lastvolume_ratio',
    'close_ma5_ratio', 'volume_ma5_ratio',
    'close_ma10_ratio', 'volume_ma10_ratio',
    'close_ma20_ratio', 'volume_ma20_ratio',
    'close_ma60_ratio', 'volume_ma60_ratio',
    'close_ma120_ratio', 'volume_ma120_ratio'
]
training_data = training_data[features_training_data]

# 강화학습 시작
policy_learner = PolicyLearner(
    stock_code=stock_code, chart_data=chart_data, training_data=training_data,
    min_trading_unit=1, max_trading_unit=2, delayed_reward_threshold=.2, lr=.001)
policy_learner.fit(balance=10000000, num_epoches=1000,
                    discount_factor=0, start_epsilon=.5)