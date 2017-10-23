import extract
import Neural_net as nn
estimator = nn.MLPRegFlow()
estimator = nn.MLPRegFlow(max_iter=1200, learning_rate_init=0.001, hidden_layer_sizes=(80,), batch_size=20, alpha_reg=0)
import numpy as np
coord_xyz = np.random.rand(20, 126)
ene = np.random.rand(20,)
estimator.fit(coord_xyz, ene)
estimator.predict(coord_xyz)
score = estimator.score(coord_xyz[:10,:], ene[:10])
print(score)
print("Test succeeded!! :D") 
