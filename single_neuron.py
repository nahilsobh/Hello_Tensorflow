# ------------------------------------------------
# Original code appeard in Hello, Tensorflow! book
# ------------------------------------------------
import tensorflow as tf

x          = tf.constant(   1.0,    name='input'        )
w          = tf.Variable(   0.8,    name='weight'       )
y          = tf.multiply(     w, x, name='output'       )
y_         = tf.constant(   0.0,    name='correct_value')
loss       = tf.pow     (y - y_, 2, name='loss'         )
train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

# ----------------------------------------------------
# save the intermediate values of x w, y, y_, and loss
# ----------------------------------------------------
for value in [x, w, y, y_, loss]:
    tf.summary.scalar(value.op.name, value)

summaries = tf.summary.merge_all()

# -----------------------
# Start a compute session
# -----------------------
sess = tf.Session()

# --------------
# Save the graph 
# --------------
summary_writer = tf.summary.FileWriter('log_simple_stats', sess.graph)

# ----------------------------------------------
# run the optimizer and save intermediate values
# ----------------------------------------------
sess.run(tf.global_variables_initializer())
for i in range(100):
    summary_writer.add_summary(sess.run(summaries), i)
    sess.run(train_step)
