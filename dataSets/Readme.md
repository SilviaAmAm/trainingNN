This directory contains datasets that have been generated from the electronic structure calculations.

### hackathonData.csv

This file contains a configuration of the system, the pbe energy and the b3lyp energy on each line. The configuration is expressed as C,x,y,z,H,x,y,z,H,x,y,z...
It only contains 7287 data points because it is the dataset that was used during the hackathon. The energies are in Ha 

### tot-pbe-b3lyp.csv

This file is the same as the hackathonData.csv, but it contains the additional data that was calculated after the hackathon. The energies are in Ha 

### pbe_b3lyp_partQ.csv

This file contain a configuration of the system, the partial charges calculated at pbe level, the pbe energy and the b3lyp energy on each line. The configuration of the system is expressed as Cx, Cy, Cz, Hx, Hy, Hz...
It contains all the b3lyp datapoints that were generated (17750 data points). The energies are in Ha 

### pbe_b3lyp_partQ_rel.csv

This file is the same as pbe_b3lyp_partQ.csv, but now the energies are relative rather than absolute. The energies are in Ha 

### data_coul.csv

This file contains on each line the randomly sorted coulomb matrix (4 repetitions) already scaled and the relative energy difference between PBE and B3LYP.The energies are in Ha 

### data_pccm.csv

This file contains on each line the partial charge coulomb matrix (4 repetitions) already scaled and the relative energy difference between PBE and B3LYP.The energies are in Ha 

### data_pccm24.csv

This file contains on each line the partial charge coulomb matrix (but where the diagonal elements are raised to the 2.4) already scaled and the relative energy difference between PBE and B3LYP.The energies are in Ha 

### pbe_b3lyp_Q_test_abs.csv

Since it was noticed that when training with the datased tot-pbe-b3lyp.csv, the neural network worked better than with pbe_b3lyp_partQ.csv, I looked into what were the differences between the two datasets. The only one that I could find was the ordering of the samples (which is strange, because it should not make a difference). But just to test, I made a new data set with the same structure as pbe_b3lyp_partQ.csv, but with the ordering of tot-pbe-b3lyp.csv to see if this makes a difference to the training. The energies are kept absolute.The energies are in Ha 

### pbe_b3lyp_Q_test_rel.csv

Exactly the same as the above dataset, but the energies are relative.The energies are in Ha 
