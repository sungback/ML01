# train_model.py
# 역할: titanic.csv를 읽고, 전처리 + 머신러닝 모델을 학습한 뒤 joblib 파일로 저장

from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

pd.set_option("display.max_columns", None) # 모든 컬럼 보기

# ============================================================
# 1. 기준 경로 설정
# ============================================================
# app.py, train_model.py, titanic.csv가 같은 폴더에 있다고 가정
BASE_DIR = Path(__file__).parent

DATA_PATH = BASE_DIR / "titanic.csv"
MODEL_PATH = BASE_DIR / "titanic_pipeline.joblib"


# ============================================================
# 2. 데이터 불러오기
# ============================================================
df = pd.read_csv(DATA_PATH)

print("데이터 크기:", df.shape)
print("컬럼 목록:")
print(df.columns.tolist())
print()

print("데이터 미리보기:")
print(df.head())
print()


# ============================================================
# 3. 사용할 컬럼 선택
# ============================================================
# survived: 정답 컬럼
# boat, body: 사고 이후에 알 수 있는 정보이므로 데이터 누수 위험 → 제외
# name, ticket, cabin, home.dest: 수업용 간단 배포 앱에서는 제외
features = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]

target = "survived"

X = df[features]
y = df[target]


# ============================================================
# 4. 숫자형 / 범주형 컬럼 구분
# ============================================================
numeric_features = [
    "age",
    "sibsp",
    "parch",
    "fare",
]

categorical_features = [
    "pclass",
    "sex",
    "embarked",
]


# ============================================================
# 5. 전처리 파이프라인 만들기
# ============================================================
# 숫자형 데이터:
# - 결측치를 중앙값으로 채움
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
    ]
)

# 범주형 데이터:
# - 결측치를 최빈값으로 채움
# - OneHotEncoder로 숫자 변환
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

# 숫자형 처리와 범주형 처리를 하나로 결합
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)


# ============================================================
# 6. 전처리 + 모델을 하나의 Pipeline으로 구성
# ============================================================
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", DecisionTreeClassifier(max_depth=6, random_state=7)),
    ]
)


# ============================================================
# 7. 학습 데이터 / 테스트 데이터 분리
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=7,
    stratify=y,
)


# ============================================================
# 8. 모델 학습
# ============================================================
pipeline.fit(X_train, y_train)


# ============================================================
# 9. 모델 평가
# ============================================================
train_score = pipeline.score(X_train, y_train)
test_score = pipeline.score(X_test, y_test)

y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("훈련 점수:", round(train_score, 4))
print("테스트 점수:", round(test_score, 4))
print("정확도:", round(accuracy, 4))
print()

print("혼동 행렬:")
print(confusion_matrix(y_test, y_pred))
print()

print("분류 리포트:")
print(classification_report(y_test, y_pred))


# ============================================================
# 10. 모델 저장
# ============================================================
# model만 저장하지 않고,
# 전처리 + 모델이 포함된 pipeline 전체를 저장해야 함
joblib.dump(pipeline, MODEL_PATH)

print()
print("모델 저장 완료:", MODEL_PATH)
