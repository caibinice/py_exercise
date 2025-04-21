import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_curve, auc
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold

# 忽略部分版本警告
warnings.filterwarnings('ignore')
# 设置sns样式
sns.set(style='white', context='notebook', palette='muted')
# 导入数据
train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')
# full = train.append(test, ignore_index=True)
full = pd.concat([train, test], ignore_index=True)

# 对Cabin缺失值进行处理，利用U（Unknown）填充缺失值
full['Cabin'] = full['Cabin'].fillna('U')
# print(full['Cabin'].head())

# print(full[full['Embarked'].isnull()])
# full['Embarked'].hist(bins=5)  # bins参数表示直方图的柱子数
# print(full['Embarked'].value_counts())
full['Embarked'] = full['Embarked'].fillna('S')
print(full['Embarked'].value_counts())

# 利用3等舱，登船港口为英国，舱位未知旅客的平均票价来填充缺失值。
full['Fare'] = full['Fare'].fillna(
    full[(full['Pclass'] == 3) & (full['Embarked'] == 'S') & (full['Cabin'] == 'U')]['Fare'].mean())

#构造新特征Title
full['Title']=full['Name'].map(lambda x:x.split(',')[1].split('.')[0].strip())
#查看title数据分布
# print(full['Title'].value_counts())

# 将相近的特征整合在一起
TitleDict = {}
TitleDict['Mr'] = 'Mr'
TitleDict['Mlle'] = 'Miss'
TitleDict['Miss'] = 'Miss'
TitleDict['Master'] = 'Master'
TitleDict['Jonkheer'] = 'Master'
TitleDict['Mme'] = 'Mrs'
TitleDict['Ms'] = 'Mrs'
TitleDict['Mrs'] = 'Mrs'
TitleDict['Don'] = 'Royalty'
TitleDict['Sir'] = 'Royalty'
TitleDict['the Countess'] = 'Royalty'
TitleDict['Dona'] = 'Royalty'
TitleDict['Lady'] = 'Royalty'
TitleDict['Capt'] = 'Officer'
TitleDict['Col'] = 'Officer'
TitleDict['Major'] = 'Officer'
TitleDict['Dr'] = 'Officer'
TitleDict['Rev'] = 'Officer'

full['Title'] = full['Title'].map(TitleDict)
print(full['Title'].value_counts())

full['familyNum']=full['Parch']+full['SibSp']+1
# 查看familyNum与Survived
# sns.barplot(data=full,x='familyNum',y='Survived')


# 按照家庭成员人数多少，将家庭规模分为“小、中、大”三类：
def familysize(familyNum):
    if familyNum == 1:
        return 0
    elif (familyNum >= 2) & (familyNum <= 4):
        return 1
    else:
        return 2


full['familySize'] = full['familyNum'].map(familysize)
full['familySize'].value_counts()
# 查看familySize与Survived
sns.barplot(data=full, x='familySize', y='Survived')
# 当家庭规模适中时，乘客的生存率更高。
plt.show()
