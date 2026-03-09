import tensorflow as tf
import numpy as np

model = tf.saved_model.load("deepfm_tfmodel")
infer = model.infer

out = infer(
    tf.constant([1], dtype=tf.int32),
    tf.constant([2], dtype=tf.int32)
)

print("추천 스코어:", out["score"])
