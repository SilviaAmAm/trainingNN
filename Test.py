import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# train_X = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
# train_Y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])

# data
x = np.arange(-4.0,4.0,0.01)
train_X = np.reshape(x, (len(x),1))
train_Y = np.power(train_X,2) + np.reshape(np.random.normal(0,1,800), (len(x),1))

# num samples/features
n_samples = len(x)
n_features = 1

# parameters
n_hidden = 20
batch_size = 50

# Building the model
X = tf.placeholder("float", [None, n_features])
y = tf.placeholder("float", [None, 1])

# weights
eps = 0.01
weights1 = tf.Variable(tf.random_normal([n_hidden, n_features]) * 2 * eps - eps)
bias1 = tf.Variable(tf.zeros([n_hidden]))
weights2 = tf.Variable(tf.random_normal([1, n_hidden]) * 2 * eps - eps)
bias2 = tf.Variable(tf.zeros([1]))

# model
a1 = tf.add(tf.matmul(X, tf.transpose(weights1)),bias1)  # output of layer1, size = n_sample x n_hidden_layer
a1 = tf.nn.sigmoid(a1)
model = tf.add(tf.matmul(a1, tf.transpose(weights2)), bias2)  # output of last layer, size = n_samples x 1
cost = tf.nn.l2_loss(t=(model - y))  # using the quadratic cost function
train_cost = []

# optimiser
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(cost)

# Initialisation of the model
init = tf.global_variables_initializer()

# Running the graph
with tf.Session() as sess:
    sess.run(init)

    for iter in range(4000):
        # This is the total number of batches in which the training set is divided
        n_batches = int(n_samples / batch_size)
        # This will be used to calculate the average cost per iteration
        avg_cost = 0
        # Learning over the batches of data
        for i in range(n_batches):
            batch_x = train_X[i * batch_size:(i + 1) * batch_size, :]
            batch_y = train_Y[i * batch_size:(i + 1) * batch_size, :]
            opt, c = sess.run([optimizer, cost], feed_dict={X: batch_x, y: batch_y})
            avg_cost += c / n_batches
        train_cost.append(avg_cost)
        if iter % 500 == 0:
            print "Completed " + str(iter) + " iterations. \n"

    y_pred = sess.run(model,feed_dict={X: train_X})

# Plotting predictions
fig3, ax3 = plt.subplots(figsize=(6,6))
ax3.scatter(train_X, y_pred, color="r", label="NN")
ax3.scatter(train_X, train_Y, color="b", label="original")
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.legend()
plt.show()

# Plotting cost
fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.plot(train_cost)
ax2.set_xlabel('Number of iterations')
ax2.set_ylabel('Cost Value in train set')
ax2.legend()
plt.show()
