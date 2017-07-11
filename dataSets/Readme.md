This directory contains datasets that have been generated from the electronic structure calculations. It is divided in directories depending on the level of theory at which the data has been calculated.

## XYQ

### X_pbe.csv, Y_pbe.csv, Q_pbe.csv
The configurations, the energies (in Ha) and the partial charges calculated at the unrestricted PBE level with basis set STO-3G.


### X_b3lyp.csv, Y_b3lyp.csv, Q_b3lyp.csv
The configurations, the energies (in Ha) and the partial charges calculated at the unrestricted B3LYP level with basis set avtz.


### X_cc.csv, Y_cc.csv, Q_cc.csv
The configurations, the energies (in Ha) and the partial charges calculated at the unrestricted CCSD(T) level with basis set avtz/mp2fit.



## PBE_B3LYP


### pbe_b3lyp_partQ_rel.csv

This file is the same as pbe_b3lyp_partQ.csv, but now the energies are relative rather than absolute. The energies are in Ha 


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

### data_rscm_b3lypcc.csv

This file contains on each line the trimmed randomly sorted coulomb matrix (5 repetitions) already scaled and the relative energy difference between B3LYP and CC. The energies are in Ha.

### data_pccm_b3lypcc.csv

This file contains on each line the trimmed partial charge coulomb matrix (5 repetitions) already scaled and the relative energy difference between B3LYP and CC. The energies are in Ha.

### data_pccm24_b3lypcc.csv

This file contains on each line the trimmed partial charge coulomb matrix (5 repetitions) already scaled and the relative energy difference between B3LYP and CC. The energies are in Ha.

### data_dpccm_b3lypcc.csv

This file contains on each line the diagonal elements of the partial charge coulomb matrix (q_i^2). The X values are already scaled and the relative energy difference between B3LYP and CC. The energies are in Ha.

