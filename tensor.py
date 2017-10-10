import tensorflow as tf



a= tf.add(3,5)
##to get the value of a we need to run the session

sess= tf.Session()
print(sess.run(a))
sess.close()