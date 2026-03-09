import pandas as pd
import lightgbm as lgb
from sklearn.preprocessing import LabelEncoder
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

# ---------------------------------------------------------
# 1. 사용자 행동 로그 데이터 (예시)
# ---------------------------------------------------------
user_logs = pd.DataFrame([
    {"user_id": 1, "place_id": 1001, "visit_count": 10, "like": 1, "category": "korean"},
    {"user_id": 1, "place_id": 1002, "visit_count": 5,  "like": 1, "category": "cafe"},
    {"user_id": 1, "place_id": 1003, "visit_count": 2,  "like": 0, "category": "japanese"},
    {"user_id": 2, "place_id": 1001, "visit_count": 1,  "like": 0, "category": "korean"},
    {"user_id": 2, "place_id": 1004, "visit_count": 8,  "like": 1, "category": "pizza"},
])

# ---------------------------------------------------------
# 2. Label Encoding (카테고리 → 숫자)
# ---------------------------------------------------------
encoder = LabelEncoder()
user_logs["category_encoded"] = encoder.fit_transform(user_logs["category"])

# ---------------------------------------------------------
# 3. Feature 구성 + Label 생성
# ---------------------------------------------------------
features = user_logs[["user_id", "place_id", "visit_count", "category_encoded"]]
labels = user_logs["like"]

# ---------------------------------------------------------
# 4. LightGBM 학습
# ---------------------------------------------------------
train_dataset = lgb.Dataset(features, label=labels)

params = {
    "objective": "binary",
    "metric": "binary_logloss",
    "verbosity": -1,
}

model = lgb.train(params, train_dataset, num_boost_round=50)


# ⭐ 핵심 API: 추천 결과 JSON으로 반환
@app.get("/recommend")
def recommend(user_id: int = 1):
    # ---------------------------------------------------------
    # 5. user_id에 대한 후보 장소 생성
    # ---------------------------------------------------------
    candidate_places = pd.DataFrame([
        {"user_id": user_id, "place_id": 2001, "visit_count": 0, "category": "cafe"},
        {"user_id": user_id, "place_id": 2002, "visit_count": 0, "category": "pizza"},
        {"user_id": user_id, "place_id": 2003, "visit_count": 0, "category": "korean"},
    ])

    # 카테고리 인코딩
    candidate_places["category_encoded"] = encoder.transform(candidate_places["category"])

    # ---------------------------------------------------------
    # 6. 예측
    # ---------------------------------------------------------
    candidate_features = candidate_places[["user_id", "place_id", "visit_count", "category_encoded"]]
    predictions = model.predict(candidate_features)

    candidate_places["score"] = predictions

    # ---------------------------------------------------------
    # 7. 정렬 후 JSON 반환
    # ---------------------------------------------------------
    recommended = candidate_places.sort_values("score", ascending=False)

    # FastAPI는 dict/list 자동으로 JSON 변환해줌
    return recommended[["place_id", "category", "score"]].to_dict(orient="records")
