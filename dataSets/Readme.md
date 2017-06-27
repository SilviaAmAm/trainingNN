This directory contains datasets that have been generated from the electronic structure calculations. It is divided in directories depending on the level of theory at which the data has been calculated.

## XYQ

### X_pbe.csv, Y_pbe.csv, Q_pbe.csv
The configurations, the energies (in Ha) and the partial charges calculated at the unrestricted PBE level with basis set STO-3G.


### X_b3lyp.csv, Y_b3lyp.csv, Q_b3lyp.csv
The configurations, the energies (in Ha) and the partial charges calculated at the unrestricted B3LYP level with basis set avtz.


### X_cc.csv, Y_cc.csv, Q_cc.csv
The configurations, the energies (in Ha) and the partial charges calculated at the unrestricted CCSD(T) level with basis set avtz/mp2fit.



## PBE_B3LYP

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

This file contains on each line the full randomly sorted coulomb matrix (4 repetitions) already scaled and the relative energy difference between PBE and B3LYP. The energies are in Ha.

### data_pccm.csv

This file contains on each line the full partial charge coulomb matrix (4 repetitions) already scaled and the relative energy difference between PBE and B3LYP.The energies are in Ha

### data_pccm24.csv

This file contains on each line the full partial charge coulomb matrix (but where the diagonal elements are raised to the 2.4) already scaled and the relative energy difference between PBE and B3LYP.The energies are in Ha


### trim_data_coul.csv

This file contains on each line the trimmed randomly sorted coulomb matrix (5 repetitions) already scaled and the relative energy difference between PBE and B3LYP. The energies are in Ha.

### trim_data_pccm.csv

This file contains on each line the trimmed partial charge coulomb matrix (5 repetitions) already scaled and the relative energy difference between PBE and B3LYP. The energies are in Ha.

### trim_data_pccm24.csv

This file contains on each line the trimmed partial charge coulomb matrix (5 repetitions) already scaled and the relative energy difference between PBE and B3LYP. The energies are in Ha.

### data_dpccm.csv

This file contains on each line the diagonal elements of the partial charge coulomb matrix (q_i^2). The X values are already scaled and the relative energy difference between PBE and B3LYP. The energies are in Ha.

### pbe_b3lyp_Q_test_abs.csv

Since it was noticed that when training with the datased tot-pbe-b3lyp.csv, the neural network worked better than with pbe_b3lyp_partQ.csv, I looked into what were the differences between the two datasets. The only one that I could find was the ordering of the samples (which is strange, because it should not make a difference). But just to test, I made a new data set with the same structure as pbe_b3lyp_partQ.csv, but with the ordering of tot-pbe-b3lyp.csv to see if this makes a difference to the training. The energies are kept absolute.The energies are in Ha

### pbe_b3lyp_Q_test_rel.csv

Exactly the same as the above dataset, but the energies are relative. The energies are in Ha.


## PBE_CC

### pbe_cc_Q_abs.csv

This contains the absolute energies (in Hartree) at the CCSD(T) level (avtz basis set) and the PBE energies (STO-3G basis set). The partial charges are calculated at the PBE basis set.

### pbe_cc_Q_rel.csv

Exactly the same as pbe_cc_Q_abs.csv except that the energies are relative instead of absolute.

### data_coul_pbecc.csv

This file contains on each line the trimmed randomly sorted coulomb matrix (5 repetitions) already scaled and the relative energy difference between PBE and CC. The energies are in Ha.

### data_pccm_pbecc.csv

This file contains on each line the trimmed partial charge coulomb matrix (5 repetitions) already scaled and the relative energy difference between PBE and CC. The energies are in Ha.

### data_pccm24_pbecc.csv

This file contains on each line the trimmed partial charge coulomb matrix (5 repetitions) already scaled and the relative energy difference between PBE and CC. The energies are in Ha.

### data_dpccm_pbecc.csv

This file contains on each line the diagonal elements of the partial charge coulomb matrix (q_i^2). The X values are already scaled and the relative energy difference between PBE and CC. The energies are in Ha.


## B3LYP_CC

### b3lyp_cc_Q_abs.csv

This contains the absolute energies (in Hartree) at the CCSD(T) level (avtz basis set) and the b3lyp energies (avtz basis set). The partial charges are calculated at the b3lyp basis set.

### b3lyp_cc_Q_rel.csv

Exactly the same as b3lyp_cc_Q_abs.csv except that the energies are relative instead of absolute.


