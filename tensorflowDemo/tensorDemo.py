import tensorflow as tf
import numpy as np

# 解决tf版本问题，2.0无法兼容1.0，所以需要禁用2.0功能
tf.compat.v1.disable_eager_execution()
# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

Weights = tf.compat.v1.Variable(tf.compat.v1.random_uniform([1], -1.0, 1.0))
biases = tf.compat.v1.Variable(tf.compat.v1.zeros([1]))

y = Weights*x_data + biases
loss = tf.compat.v1.reduce_mean(tf.square(y-y_data))

optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.compat.v1.global_variables_initializer()  # 替换成这样就好

sess = tf.compat.v1.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

