# CitcomS

This folder contains the scripts used to process, edit, and prepare tectonic plate velocity fields for use as boundary conditions in CitcomS models. The original data consists of velocity vectors (x and y components) provided at multiple geographic coordinates and for time steps ranging from 65 Ma to the present, with 1 Ma intervals.

The scripts perform the following tasks:

  Reading and organizing plate velocity data.

  Targeted modification of velocities in specific regions to introduce or remove features such as back-arc basins and mid-ocean ridges.

  Spatial interpolation to increase resolution and adapt the data to new simulation grids.

  Replacement of velocity values in selected areas to test or refine tectonic scenarios.

  Preparation of final input files formatted for CitcomS.

The overall goal of these scripts is to tailor tectonic velocity data to specific geodynamic scenarios, enabling numerical experimentation with custom configurations.
