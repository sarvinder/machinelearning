import tensorflow as tf


#a=tf.add(3,5)
##to get the value of a we need to run the session

#sess= tf.Session()
#print(sess.run(a))
#sess.close()
#to get the random number matrix or vector
#tf.truncated_normal()

#This is used to visualize the data example
def visualize():
    a=tf.constant(2)
    b=tf.constant(3)
    x=tf.add(a,b)

    with tf.Session() as sess:
        writer=tf.summary.FileWriter('./graphs',sess.graph)
        print(sess.run(x))
    writer.close()
    sess.close()