# Hello, Tensorflow!

This a corrected, beautified, and commented code in [Hello, Tensorflow!](https://www.oreilly.com/learning/hello-tensorflow) book.

| Before                                                                 | After                                                                  |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
|tf.scalar_summary(value.op.name, value)                                 |   tf.**summary.scalar**(value.op.name, value)                          |
|summaries = tf.merge_all_summaries()                                    |summaries = tf.**summary.merge_all**()                                  |
|summary_writer = tf.train.SummaryWriter('log_simple_stats', sess.graph) |summary_writer = tf.**summary.FileWriter**('log_simple_stats', sess.graph)|
|sess.run(tf.initialize_all_variables())                                 |sess.run(**tf.global_variables_initializer()**)                         |

