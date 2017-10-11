import sys
sys.path.append('/mnt/storage/home/sa16246/repositories/Aglaia')
import tensorflow as tf
import Neural_net as nn
import pickle

estimator = nn.MLPRegFlow(max_iter=1000, hidden_layer_sizes=(80,), batch_size=20)
pickle.dump(estimator, open('/mnt/storage/home/sa16246/repositories/trainingNN/training_Aglaia/first_test/model.pickl','wb'))
