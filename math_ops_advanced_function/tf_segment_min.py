import tensorflow as tf

"""tf.segment_min(data, segment_ids, name=None)
功能：tensor进行拆分后求最小值。
输入：segment_ids:必须是整型，1维向量，向量数目与data第一维的数量一致。
                必须从0开始，且以1进行递增。 """
a = tf.constant([[1,2,3],[4,5,6],[7,8,9]])
z=tf.segment_min(a,[0,0,1])

sess = tf.Session()
print(sess.run(z))
sess.close()

# z==>[[1 2 3]
#      [7 8 9]]
