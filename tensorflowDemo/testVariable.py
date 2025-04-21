import tensorflow as tf

# 解决tf版本问题，2.0无法兼容1.0，所以需要禁用2.0功能
tf.compat.v1.disable_eager_execution()

state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.compat.v1.assign(state, new_value)

init = tf.compat.v1.global_variables_initializer()  # 替换成这样就好

# 使用 Session
with tf.compat.v1.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))


