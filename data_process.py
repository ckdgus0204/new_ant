import pandas as pd
import numpy as np
import sys, os

# file = "./005930.csv"

def load_chart_data(file):
   file = os.path.join('./data', file)
   chart_data = pd.read_csv(file, thousands=',', header=None)
   chart_data.columns = ['Data', 'open', 'high', 'low', 'close', 'adj_close', 'volume']
   chart_data = chart_data[1:]

   chart_data['open'] = chart_data['open'].astype(float)
   chart_data['high'] = chart_data['high'].astype(float)
   chart_data['close'] = chart_data['close'].astype(float)
   chart_data['volume'] = chart_data['volume'].astype(float)
   return chart_data

def preprocess(chart_data):
   prep_data = chart_data
   windows = [5, 10, 20, 60, 120]
   for window in windows:
      prep_data['close_ma%d' % window] = prep_data['close'].rolling(window).mean()
      prep_data['volume_ma%d' % window] = prep_data['volume'].rolling(window).mean()
   return prep_data

# after preprocess
def build_training_data(prep_data):
   training_data = prep_data

   training_data['open'] = training_data['open'].astype(float)
   training_data['high'] = training_data['high'].astype(float)
   training_data['low'] = training_data['low'].astype(float)
   training_data['volume'] = training_data['volume'].astype(float)

   training_data['open_lastclose_ratio'] = np.zeros(len(training_data))
   # training_data.loc[1:, 'open_lastclose_ratio'] = (training_data['open'][1:].values.astype(float) - training_data['close'][:-1].values.astype(float)) / training_data['close'][:-1].values.astype(float)
   training_data['open_lastclose_ratio'].iloc[1:] = (training_data['open'][1:] - training_data['close'][:-1]) / training_data['close'][:-1]
   training_data['high_close_ratio'] = (training_data['high'].values - training_data['close'].values) / training_data['close'].values
   training_data['low_close_ratio'] = (training_data['low'].values - training_data['close'].values) / training_data['close'].values

   training_data['close_lastclose_ratio'] = np.zeros(len(training_data))
   #  training_data.loc[1:, 'close_lastclose_ratio'] = (training_data['close'][1:].values - training_data['close'][:-1].values) / training_data['close'][:-1].values
   training_data['close_lastclose_ratio'].iloc[1:] =  (training_data['close'][1:].values - training_data['close'][:-1].values) / training_data['close'][:-1].values

   training_data['volume_lastvolume_ratio'] = np.zeros(len(training_data))
   training_data['volume_lastvolume_ratio'].iloc[1:] = (training_data['volume'][1:].values - training_data['volume'][:-1].values) / training_data['volume'][:-1].replace(to_replace=0, method='ffill').replace(to_replace=0, method='bfill').values
   #  training_data.loc[1:, 'volume_lastvolume_ratio'] = (training_data['volume'][1:].values - training_data['volume'][:-1].values) / training_data['volume'][:-1].replace(to_replace=0, method='ffill').replace(to_replace=0, method='bfill').values

   windows = [5, 10, 20, 60, 120]
   for window in windows:
      training_data['close_ma%d_ratio' % window] = (training_data['close'] - training_data['close_ma%d' % window]) / training_data['close_ma%d' % window]
      training_data['volume_ma%d_ratio' % window] = (training_data['volume'] - training_data['volume_ma%d' % window]) / training_data['volume_ma%d' % window]

   return training_data

file = '005930'
chart_data = load_chart_data(file+'.csv')
prep_data = preprocess(chart_data)

training_data = build_training_data(prep_data)

print(training_data)

training_data.to_csv('./'+file+'_training_data.csv', index=True, header=True)