# Hello, Tensorflow!

This a corrected, beautified, and commented code in [Hello, Tensorflow!](https://www.oreilly.com/learning/hello-tensorflow) book.

| Before                                                                 | After                                                                  |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
|import tensorflow as tf                                                 |import tensorflow as tf                                                 |
|                                                                        |                                                                        |
|x = tf.constant(1.0, name='input')                                      |x = tf.constant(1.0, name='input')                                      |
|w = tf.Variable(0.8, name='weight')                                     |w = tf.Variable(0.8, name='weight')                                     |
|y = tf.mul(w, x, name='output')                                         |y = tf.mul(w, x, name='output')                                         |
|y_ = tf.constant(0.0, name='correct_value')                             |y_ = tf.constant(0.0, name='correct_value')                             |
|loss = tf.pow(y - y_, 2, name='loss')                                   |loss = tf.pow(y - y_, 2, name='loss')                                   |
|train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)    |train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)    |
|                                                                        |                                                                        |
|for value in [x, w, y, y_, loss]:                                       |for value in [x, w, y, y_, loss]:                                       |
|    tf.scalar_summary(value.op.name, value)                             |   *tf.summary.scalar(value.op.name, value)*                            |
|                                                                        |                                                                        |
|summaries = tf.merge_all_summaries()                                    |*summaries = tf.summary.merge_all()*                                    |
|                                                                        |                                                                        |
|sess = tf.Session()                                                     |sess = tf.Session()                                                     |
|summary_writer = tf.train.SummaryWriter('log_simple_stats', sess.graph) |*summary_writer = tf.summary.FileWriter('log_simple_stats', sess.graph)*|
|                                                                        |                                                                        |
|sess.run(tf.initialize_all_variables())                                 |*sess.run(tf.global_variables_initializer())*                           |
|for i in range(100):                                                    |for i in range(100):                                                    |
|    summary_writer.add_summary(sess.run(summaries), i)                  |    summary_writer.add_summary(sess.run(summaries), i)                  |
|    sess.run(train_step)                                                |    sess.run(train_step)                                                |

