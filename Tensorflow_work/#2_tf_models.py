import tensorflow as tf

# in this files we work for {{ Construction of model & loss function and also trying to reduce to loss function }}
# steps to perform to obtain optimal results
# 1. Declare or obtain Variables
# 2. Initialization of Variables
# 3. Create Model
# 4. create loss function
# 5. apply vector
# 6. optimize loss we are using GradientDescentOptimizer
# 7. Graphical visualization (Optional)
# 8. Apply the loss function with Optimizers and GDO method
# 9. Close the Session
# -------------------------- 1. Declare or obtain Variables-------------------------
w = tf.Variable([.1], dtype=tf.float64)
b = tf.Variable([-.1], dtype=tf.float64)
x = tf.placeholder(dtype=tf.float64)

mul = tf.multiply(w,b) # this is only for test purpose
# --------------------------3. Create  liner model--------------------------------
liner_model = w * x + b

# --------------------5. apply vector {y} node to I/O data obtained in the experiment-------------

y = tf.placeholder(dtype=tf.float64)
# ------------------------------# 4. create loss function------------------------------
loss = tf.reduce_sum(tf.square(liner_model - y))
sess = tf.Session()

# ------------------------------- 2. Initialization of Variable -----------------------------
init = tf.global_variables_initializer()
print("this is also initialization =>",sess.run(init))
print("multiplication function =>",sess.run([mul,w,b]))
print("this call linear model =>",sess.run(liner_model,{x:[1,2,3,4]}))
print("this call linear model with loss function =>",sess.run(loss,{x:[1,2,3,4,5],y:[4.8, 8.5, 10.4, 21.0, 25.3]}))

# -------------------------- 6. optimize loss we are using GradientDescentOptimizer---------------
optimizer = tf.train.GradientDescentOptimizer(0.0001)
Train = optimizer.minimize(loss)

# save the training data with two arrays
x_train = [1,2,4,5,8]
y_train = [4.8,8.5,10.2,14.5,21.3]

# lest train 10000 times
for i in range(10000):
    sess.run(Train, {x:x_train,y:y_train})

# -------------------------- # 7. Graphical visualization ------------------------------
# if you want to see your work flow by graphically you should type this
FileWriter = tf.summary.FileWriter(".\\graph\\",sess.graph)
# then after go to command prompt of current dir and type {{ tensorboard --logdir="graph" }}

# ----------------------  # 8. Apply the loss function with Optimzers and GDO method -----------------

print("Training o/p =>{0},{1},{2}".format(sess.run(w),sess.run(b),sess.run(loss,{x:x_train,y:y_train})))

# ------------------------- 9. close the Session ----------------
sess.close()