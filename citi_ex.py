import dask
from flask import Flask, request
DF = dask.datasets.timeseries(start='2020-01-01', end='2020-01-02').compute().head(100)

def get_means(df):
    mean_by_name = df.groupby('name').mean()['x']
    dict_means = mean_by_name.to_dict()
    return dict_means

def apply_means(dict_means, df):
    for index, row in df.iterrows():
        df.loc[index, 'x_mean'] = dict_means[row['name']]
    return df

def get_by_name(name, dataframe):
    df = dataframe[dataframe['name'] == name].sort_values(by=['x'])
    df = df.iloc[:10]
    json = df.to_json(orient='split')
    return json

# Preprocess part

dict_means = get_means(DF)
last_df = apply_means(dict_means, DF)


# Api Part

app = Flask(__name__)


@app.route('/top10', methods=['GET'])
def get_top10():
    name = request.args.get('name')
    json_string = get_by_name(name, last_df)
    return json_string
