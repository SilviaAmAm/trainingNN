import extract
import Neural_net_2 as nn
import numpy as np

estimator = nn.MLPRegFlow(max_iter=1200, learning_rate_init=0.001, hidden_layer_sizes=(80,), batch_size=20, alpha_reg=0)
coord_xyz = np.random.rand(20, 126)
ene = np.random.rand(20,127)
estimator.fit(coord_xyz, ene)
estimator.predict(coord_xyz)
score = estimator.score(coord_xyz[:10,:], ene[:10])
print(score)
print("Test succeeded!! :D") 
