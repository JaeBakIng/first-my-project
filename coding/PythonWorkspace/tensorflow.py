import tensorflow as tf # tensorflow 를 tf로 쓸거다

# X and Y data
x_train = [1, 2, 3] # <-- list
y_train = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight') # tf. ??? 는 tf안에 있는 함수를 불러오는것 .점 이 불러오도록하는 코드
b = tf.Variable(tf.random_normal([1]), name='bias')

# Our hypothesis XW+b
hypothesis = x_train * W + b # = H(x) = wx + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train)) # 코드 거진 외우자!

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) #GDA cost를 minimize할수있는 값을 찾아줌 tf모듈 안에 train 모듈 안에 GDA가 있음
train = optimizer.minimize(cost)

# Launch the graph in a session.
sess = tf.Session()
# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(2001):
   sess.run(train)
   if step % 20 == 0:
       print(step, sess.run(cost), sess.run(W), sess.run(b))