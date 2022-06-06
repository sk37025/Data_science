import pandas as pd 

def train_test_reader():
    train = pd.read_csv("./data/raw/train.csv")
    test = pd.read_csv("./data/raw/test.csv")
    print(f'train data set은 {train.shape[1]} 개의 feature를 가진 {train.shape[0]} 개의 데이터 샘플로 이루어져 있습니다.')
    print(f'test data set은 {test.shape[1]} 개의 feature를 가진 {test.shape[0]} 개의 데이터 샘플로 이루어져 있습니다.')
    return train, test 

def check_missing_col(df):
    missing_col = []
    for col in df.columns: 
        missing_values = sum(df[col].isna())
        is_missing = True if missing_values > 0 else False
        if is_missing : 
            print("결측치가 있는 컬럼은 : {} 입니다.".format(col))
            print("해당 컬럼에 총 {} 개의 결측치가 존재합니다.".format(missing_values))
            missing_col.append([col,df[col].dtype])
    if missing_col == []:
        print("결측치가 존재하지 않습니다.")
    return missing_col

def make_label_map(dataframe):
    '''라벨 인코딩을 하기 위한 dictionary map 생성 함수'''
    label_maps = {}
    for col in dataframe.columns:
        if dataframe[col].dtype=='object':
            label_map = {'unknown':0}
            for i, key in enumerate(dataframe[col].unique()):
                label_map[key] = i+1  #새로 등장하는 유니크 값들에 대해 1부터 1씩 증가시켜 키값을 부여해줍니다.
            label_maps[col] = label_map
    print(label_maps)
    return label_maps

def label_encoder(df, label_map):
    for col in df.columns: 
        if df[col].dtype == "object":
            df[col] = df[col].map(label_map[col])
            df[col] = df[col].fillna(label_map[col]['unknown'])
    return df 


