# Aggregate-Modeling-of-Pseudomonas
Repository containing code for an aggregate simulation of pseudomonas that captures both aggregate and cell-level behavior.  My contributions are combined with contributions of Michael J Sweeney and Sarah Sundius.

This project is a simulation written in Julia that models aggregate behavior of P. aeruginosa. Its purpose is to provide data to study aggregate behavior and investigate the relationship between growth rate and aggregate size. It is an IBM that captures cell-level behavior such as cell replication and cell death, as well as aggregate-level behavior such as diffusive aggreagation. It is meant to fill the hole in aggregate modeling left by simulations that only focus on biofilms or planktonic cells, and do not capture multiple levels of behavior.

There are 2 primary files in this project: 2D_AGGREGATES.ipynb contains the main Julia simulation. CONCENTRATION_GRADIENT.py contains Julia functions used for simulating a chemical/environmental "layer" in the main simulation. It can exist standalone as a diffusion simulation as well.

NOTE: All key and propietary sections of the main simulation code have been redacted since a publication is currently pending. Please reach out to me at kkrishnan38@gatech.edu if you would like to learn more about the sim or the code! Thank you. 

Below are images of the simulation collated from my undergraduate thesis at Georgia Tech circa 2024.

## Diffusion
The forward time-centered space solution of the diffusion equation (solved in diffusion.jl) is a high-error method to solving partial differential equations. However, as far as numerical methods go, it is efficient and easy to implement. 

![diffusion](https://github.com/karthik-krishnan-28/Aggregate-Modeling-of-Pseudomonas/blob/main/thesis/diffusion.png)

## Aggregate Dynamics
The simulation was built to observe aggregate growth dynamics at low densities with the intention of investigating a hypothesis regarding faster growing cells being present in larger aggregates and the underlying reasons for this emergent behavior. The figures below show how the simulation can be used to visualize aggregate behavior for different growth scenarios. As can be seen in 2D_AGGREGATES.ipynb, users can fix parameters like growth rates, diffusive aggregation rates, aggregate erosion rates, etc. and then visualize behaviors over time and over many random tests and initial conditions. 

First, a case where aggregates erosion rates are higher than cellular growth rates:

![low-separation](https://github.com/karthik-krishnan-28/Aggregate-Modeling-of-Pseudomonas/blob/main/thesis/low_sep.png)

Second, a case where aggregates erosion rates are lower than cellular growth rates:

![low-separation](https://github.com/karthik-krishnan-28/Aggregate-Modeling-of-Pseudomonas/blob/main/thesis/high_sep.png)

Lastly, a case where aggregates erosion rates are lower than cellular growth rates and diffusive aggregation is turned on:

![low-separation](https://github.com/karthik-krishnan-28/Aggregate-Modeling-of-Pseudomonas/blob/main/thesis/high_sep_collisions.png)


A final note: quantitative data can also be collected and analyzed regarding aggregate size and growth distributions as well as cell positions and solute densities/flow.
