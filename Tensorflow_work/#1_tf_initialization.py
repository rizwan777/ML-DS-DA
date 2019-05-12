import tensorflow as tf

# first we start with the initializing the values for computation
# 1 . giving constant values
# 2. Adding Value at runtime
#------------------ 1. store constant value into node of tensorflow--------------------------------------#
node1 = tf.constant(3)
node2 = tf.constant(34)

# node2 = tf.constant(34,dtype=tf.float64)
# if you very sure about your operation with nodes then
# you may assign the datatype specificly using {dtype} perameter for memory optimization.

node3 = tf.multiply(node1,node2)  # here we use default tensorflow methods ..!!
print("Initialization =>",node1, node2, node3)
# op ==> Tensor("Const:0", shape=(), dtype=int32)  <== node1 info.
#        Tensor("Const_1:0", shape=(), dtype=int32)   <== node2 info.
#        Tensor("Mul:0", shape=(), dtype=int32)     <== node3 info.

#  session : a tf.Session encapsulates the control and state of the TensorFlow runtime.
sess = tf.Session()    # Session is Started  and assign with the session variable

#if you want to see your work flow by graphically you should type this
FileWriter = tf.summary.FileWriter(".\\graph\\",sess.graph)
# then after go to command prompt of current dir and type {{ tensorboard --logdir="graph" }}

print("Constant Vaules =>",sess.run([node1, node2,node3]))  # Session is running with run() method
# op => [3, 34, 102]
#        ^   ^    ^
#        |   |    |
#     node1 node2 node3=function{multiply}


# note:{{
#           whenever your session operation was finish then you must close the session using "sess.Close()"
#           here {sess} is initialized check line no 20.
# }}

# ------------- 2.below code for Providing  Values at Runtime using tf method {placeholder}  -------------#
nodeX = tf.placeholder(tf.int64)
nodeY = tf.placeholder(tf.int64)
# in above we use placeholder for adding value later but we need to provide its data type

nodeSum = tf.add(nodeX,nodeY)
# in above we used tensorflow add method
print("Runtime Binding =>",sess.run(nodeSum,{nodeX:[1,2,3,4],nodeY:[5,4,3,2]}))
# 1. adding session to run the tensor
# 2. above we assign our reference variable of adding method {nodeSum}
# 3. providing runtime values to the nodes {nodeX =>{1,2,3,4}, while nodeY =>{5,4,3,2}} are assign
# op => [6 6 6 6]  adding both nodes value with each other.

sess.close()  # Session is close with close() method
