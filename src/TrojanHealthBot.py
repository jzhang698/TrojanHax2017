# TrojanHealthBot

import numpy as np
import tensorflow as tf

outfile = open('out.txt', 'w')
accuracy_arr = []

# repeat run the model
for repeat in range(0, 5):
	config = open('../config.txt')
	input_features = int(config.readline().strip())
	trn_x = '../' + config.readline().strip()
	trn_y = '../' + config.readline().strip()
	tst_x = '../' + config.readline().strip()
	tst_y = '../' + config.readline().strip()


	X      = np.genfromtxt(trn_x, delimiter=',', dtype=int)
	X_test = np.genfromtxt(tst_x, delimiter=',', dtype=int)
	Y      = np.genfromtxt(trn_y, delimiter=',', dtype=int)
	Y = np.array([Y, -(Y-1)]).T
	Y_test = np.genfromtxt(tst_y, delimiter=',', dtype=int)
	Y_test = np.array([Y_test, -(Y_test-1)]).T

	#  optional remove some data for testing
	# index = np.random.uniform(0, 105, size=34)
	# X = np.delete(X, index, axis=0)
	# Y = np.delete(Y, index, axis=0)
	# print(len(X), len(Y))

	# print(len(X))
	# print(X)
	# print('-----------------------------')
	# print(len(X_test))
	# print(X_test)
	# print('-----------------------------')
	# print(len(Y))
	# print(Y)
	# print('-----------------------------')
	# print(len(Y_test))
	# print(Y_test)
	# print('-----------------------------')

	layer_1_features = 10
	layer_2_features = 10

	# define weight/bias
	weight = [
		tf.Variable(tf.random_normal([layer_2_features, 2])), # out
		tf.Variable(tf.random_normal([input_features, layer_1_features])),
		tf.Variable(tf.random_normal([layer_1_features, layer_2_features]))
	]
	bias = [
		tf.Variable(tf.random_normal([2])), # out
		tf.Variable(tf.random_normal([layer_1_features])),
		tf.Variable(tf.random_normal([layer_2_features]))
	]

	# setup tensorflow vars
	x = tf.placeholder("float", [None, input_features])
	y = tf.placeholder("float", [None, 2])
	layer_1 = tf.add(tf.matmul(x, weight[1]), bias[1])
	layer_1 = tf.nn.relu(layer_1)
	layer_2 = tf.add(tf.matmul(layer_1, weight[2]), bias[2])
	layer_2 = tf.nn.relu(layer_2)
	pred = tf.matmul(layer_2, weight[0]) + bias[0]
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
	optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
	init = tf.global_variables_initializer()

	with tf.Session() as sess:
		sess.run(init)
		# run for 200 epochs
		for epoch in range(200):
			avg_cost = 0.
			# split into batches of size 4
			total_batch = int(len(X)/4)
			X_batches = np.array_split(X, total_batch)
			Y_batches = np.array_split(Y, total_batch)
			for i in range(total_batch):
				batch_x, batch_y = X_batches[i], Y_batches[i]
				_, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})
				avg_cost = avg_cost + c / total_batch
		# Finish up / show accuracy
		correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
		accuracy_arr.append(accuracy.eval({x: X_test, y: Y_test}))

outfile.write(str(accuracy_arr))
outfile.write('\n')
outfile.write(str(sum(accuracy_arr) / float(len(accuracy_arr))))
outfile.close()