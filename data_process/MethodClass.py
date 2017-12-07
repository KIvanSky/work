import pandas as pd
import numpy as np

class file:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.new_name = self.name[0:-4]
    def openfile(self):
        print(self.name)
        df = pd.read_table(self.path + self.name, header=2)
        print(self.name)
        return df
    def reline(self):    # txt替换
        rf = self.openfile()
        df = pd.DataFrame(rf.values,
                          columns=['time', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                   22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])

        return df
    def joint(self,df):     # 三列替换

        list_drop = []

        for i in df.index:

            start = df.iat[i, 37]
            end = df.iat[i, 38]
            print(i)
            if start > end:
                print(i)
                df.iat[i, 29] = df.iat[i, 32]
                df.iat[i, 30] = df.iat[i, 33]
                df.iat[i, 31] = df.iat[i, 34]
            else:
                if start < end:
                    continue

                else:
                    list_drop.append(i)

        df.drop(list_drop, inplace=True)
        print(df)
        rf2 = df.drop([32, 33, 34, 37, 38, 41], axis=1)
        rf2.to_csv("/Users/BuleSky/Desktop/work/" + self.new_name + '.csv', index=False)
        return rf2

    def computeliquid(self, df):   # 计算液位差公式

        mat = 160 * (np.array(df.iloc[:, 24]) - np.array(df.iloc[:, 25])) / 10000
        print(df.iloc[:, 25])
        return mat
    def liquid(self,df):      # 计算液位差


        df["液位波动"] = self.computeliquid(df)

        df.to_csv('/Users/BuleSky/Desktop/liquid/' + self.name, index=False, encoding='gb2312')
        print('liquidEND')
        return df

    def temperature(self, df_tem):    #添加温度


        df_tem.index = range(0, len(df_tem))

        df_tem["float_time"] = df_tem.time.apply(lambda t: float(t[6:10] + t[3:5] + t[:2] + t[11:13] + t[14:16] + t[17:19]))
        print(df_tem)
        result = pd.read_excel('/Users/BuleSky/Desktop/match/presult1019.xlsx').fillna(0)[:]


        for i in result.index:

            start = result.iloc[i].picturename
            end = start + 1




            df_tem.loc[df_tem.index[(df_tem.float_time >= start) & (df_tem.float_time <= end)], '41'] = result.iloc[i].right
            df_tem.loc[df_tem.index[(df_tem.float_time >= start) & (df_tem.float_time <= end)], '42'] = result.iloc[i].left
        print(df_tem)
        data = df_tem.loc[list(df_tem.loc[:, ['41', '42']].dropna(axis=0).index), :]

        data = data.drop(['float_time'], axis=1)
        data.to_csv('/Users/BuleSky/Desktop/temperature/' + self.name + '.csv', index=False,encoding='gb2312')
        print('temperatureEND')
        print(data)
        return data
    def addresult(self,df_result):         # 添加结果


        df_result.index = range(0, len(df_result))
        df_result["float_time"] = df_result.time.apply(lambda t: float(t[6:10] + t[3:5] + t[:2] + t[11:13] + t[14:16] + t[17:19]))
        result = pd.read_csv('/Users/BuleSky/Desktop/match/time1115.csv').fillna(0)[:]

        count = 0
        time_count = 0
        for i in result.index:
            print(i)
            start = result.iloc[i].start
            end = result.iloc[i].end
            print('*******************')
            if result.iloc[i].cause == 0:
                print("*******************************************************")
                if len(df_result.index[(df_result.float_time >= start) & (df_result.float_time <= end)]) > 0:
                    time_count = 0
                else:
                    time_count += 1
                count += len(df_result.index[(df_result.float_time >= start) & (df_result.float_time <= end)])
                df_result.loc[df_result.index[(df_result.float_time >= start) & (df_result.float_time <= end)], '43'] = 1
            else:
                print("*******************************************************")
                if len(df_result.index[(df_result.float_time >= start) & (df_result.float_time <= end)]) > 0:
                    time_count = 0
                else:
                    time_count += 1
                count += len(df_result.index[(df_result.float_time >= start) & (df_result.float_time <= end)])
                df_result.loc[df_result.index[(df_result.float_time >= start) & (df_result.float_time <= end)], '43'] = 0

        data = df_result.loc[list(df_result.loc[:, ['43']].dropna(axis=0).index), :]

        data = data.drop(['float_time'], axis=1)
        data.to_excel('/Users/BuleSky/Desktop/addresult/' + self.new_name + '.xlsx', index=False,encoding='gb2312')
        print('addresultEND')
