# Website Content — Ludovico Theo Giorgini

This file is the publication-ready source of truth for the website’s written content, link labels, and metadata.

## Site-wide metadata

- **Browser title:** Ludovico Theo Giorgini
- **Open Graph title:** Ludovico Theo Giorgini | Applied Mathematics and Scientific Machine Learning
- **Headshot alt text:** Portrait of Ludovico Theo Giorgini.

## Sidebar

### Identity

**Ludovico Theo Giorgini**

C.L.E. Moore Instructor of Mathematics

Massachusetts Institute of Technology

### Pages

- About me
- Research
- Publications
- Software
- Teaching
- Contact

### Links

- [CV](cv.pdf)
- [E-mail](mailto:ludogio@mit.edu)
- [MIT Profile](https://math.mit.edu/directory/profile.html?pid=2704)
- [Google Scholar](https://scholar.google.com/citations?user=DA5vUj0AAAAJ)
- [GitHub](https://github.com/ludogiorgi)
- [ORCID](https://orcid.org/0000-0003-1641-9087)

## About me

**Ludovico Theo Giorgini**

**C.L.E. Moore Instructor of Mathematics**  
**Massachusetts Institute of Technology**

I am an applied mathematician working at the intersection of applied probability, statistical physics, and scientific machine learning. I develop mathematical and computational methods for extracting effective low-dimensional descriptions from complex, high-dimensional systems. I am particularly interested in multiscale problems in fluid dynamics, geophysics, and nonequilibrium systems.

## Research

Scientific observations and high-fidelity simulations are generating unprecedented volumes of data across the physical sciences. I study how these data can be transformed into reduced models that retain the statistical and dynamical information needed for prediction and physical understanding. I combine stochastic analysis, linear response theory, and scientific machine learning to infer effective dynamics for the resolved variables in these models.

### Research Areas

#### Linear Response theory and statistical parameter calibration

My collaborators and I have developed a practical response-theoretic framework for predicting how nonlinear, high-dimensional systems respond to weak perturbations from observations of their unperturbed dynamics. The generalized fluctuation–dissipation theorem (GFDT) expresses this response through time-correlation functions, but its implementation requires the stationary score. Estimating the score accurately in high dimensions has been a principal computational obstacle to applying the GFDT beyond idealized settings. We have combined modern score-matching methods with the GFDT and validated the resulting response estimates on nonlinear stochastic PDEs. More recently, we extended this framework to statistical parameter calibration by interpreting infinitesimal changes in drift and diffusion parameters as dynamical perturbations. The resulting formulas express the sensitivities of stationary observables to all model parameters as time-correlation integrals evaluated along unperturbed trajectories; these sensitivities can then guide parameter updates that bring model statistics toward prescribed targets using only a few model integrations. For lower-dimensional systems, we also developed KGMM, a clustering-based method for accurate and computationally efficient score estimation. Building on these advances, we are using GFDT response sensitivities to identify low-dimensional, target-dependent parameter subspaces for calibrating high-dimensional models.

**Representative work:** [Giorgini et al. (2024)](https://doi.org/10.1103/PhysRevLett.133.267302), [Giorgini, Falasca, and Souza (2025)](https://doi.org/10.1073/pnas.2509578122), [Giorgini, Bischoff, and Souza (2025)](https://arxiv.org/abs/2509.19660), and [Giorgini, Bischoff, and Souza (2026)](https://doi.org/10.1016/j.physd.2026.135274).

#### Score-based stochastic closures

Many systems in the physical sciences and engineering couple nonlinear processes across widely separated spatial and temporal scales. The quantities of scientific interest, however, often depend only on a much smaller set of coarse observables and their statistics rather than on the complete high-dimensional state. The goal is therefore to use coarse data from observations, experiments, or high-fidelity simulations to construct efficient stochastic models that evolve only these resolved variables while reproducing the statistical and dynamical observables of interest. The difficulty is that the dynamics of the coarse variables are generally not closed: unresolved degrees of freedom influence their evolution through effective dissipation, fluctuations, feedback, and memory. I construct Markovian *a priori* closures directly from the statistical and finite-time dynamical observables they must reproduce. Instead of specifying a local evolution law and then testing its long-time behavior, the construction begins with these target observables and asks which stochastic models reproduce them by construction. The stationary score—the gradient of the logarithm of the steady-state probability density—characterizes a broad class of stochastic models that preserve the observed distribution by construction; combining it with linear response theory through the generalized fluctuation–dissipation theorem provides complementary dynamical constraints that restrict this class to models reproducing selected finite-time observables. The admissible family is therefore determined directly from observable constraints, without repeated simulations of candidate closures.

**Representative work:** [Giorgini (2026)](https://doi.org/10.1103/6qpv-lqmt), [Giorgini, Bischoff, and Souza (2025)](https://arxiv.org/abs/2508.19448), [Giorgini (2026)](https://arxiv.org/abs/2604.23952), and [Del Felice and Giorgini (2026)](https://doi.org/10.1063/5.0326565).

## Publications

### Preprints

1. **L. T. Giorgini**, “Conditional Score-Based Modeling of Effective Langevin Dynamics,” [arXiv:2604.23952 (2026)](https://arxiv.org/abs/2604.23952).
2. P. Patra, **L. T. Giorgini**, and J. S. Wettlaufer, “Stochastic Coupling of Climate Variables and Ice Volume over the Late Pleistocene Glacial Cycles,” [arXiv:2603.26937 (2026)](https://arxiv.org/abs/2603.26937).
3. **L. T. Giorgini**, T. Bischoff, and A. N. Souza, “Statistical Parameter Calibration via the Generalized Fluctuation–Dissipation Theorem and Generative Modeling,” [arXiv:2509.19660 (2025)](https://arxiv.org/abs/2509.19660).
4. **L. T. Giorgini**, T. Bischoff, and A. N. Souza, “Reduced-Order Modeling of Cyclo-Stationary Time Series Using Score-Based Generative Methods,” [arXiv:2508.19448 (2025)](https://arxiv.org/abs/2508.19448).

### Peer-Reviewed Journal Articles

1. **L. T. Giorgini**, “Score-Based Modeling of Effective Langevin Dynamics,” [*Physical Review E* **114**, L012102 (2026)](https://doi.org/10.1103/6qpv-lqmt).
2. **L. T. Giorgini**, T. Bischoff, and A. N. Souza, “KGMM: A K-means Clustering Approach to Gaussian Mixture Modeling for Score Function Estimation,” [*Physica D: Nonlinear Phenomena* **495**, 135274 (2026)](https://doi.org/10.1016/j.physd.2026.135274).
3. G. Del Felice and **L. T. Giorgini**, “Integrating Score-Based Generative Modeling and Neural ODEs for Accurate Representation of Multiscale Chaotic Dynamics,” [*Chaos* **36**, 063143 (2026)](https://doi.org/10.1063/5.0326565).
4. **L. T. Giorgini**, F. Falasca, and A. N. Souza, “Predicting Forced Responses of Probability Distributions via the Fluctuation–Dissipation Theorem and Generative Modeling,” [*Proceedings of the National Academy of Sciences* **122**, e2509578122 (2025)](https://doi.org/10.1073/pnas.2509578122).
5. **L. T. Giorgini**, A. N. Souza, D. Lippolis, P. Cvitanović, and P. J. Schmid, “Learning Dissipation and Instability Fields from Chaotic Dynamics,” [*Physica D: Nonlinear Phenomena* **481**, 134865 (2025)](https://doi.org/10.1016/j.physd.2025.134865).
6. **L. T. Giorgini**, K. Deck, T. Bischoff, and A. N. Souza, “Response Theory via Generative Score Modeling,” [*Physical Review Letters* **133**, 267302 (2024)](https://doi.org/10.1103/PhysRevLett.133.267302).
7. **L. T. Giorgini**, A. N. Souza, and P. J. Schmid, “Reduced Markovian Models of Dynamical Systems,” [*Physica D: Nonlinear Phenomena* **470**, 134393 (2024)](https://doi.org/10.1016/j.physd.2024.134393).
8. **L. T. Giorgini**, W. Moon, and J. S. Wettlaufer, “Analytical Survival Analysis of the Non-autonomous Ornstein–Uhlenbeck Process,” [*Journal of Statistical Physics* **191**, 138 (2024)](https://doi.org/10.1007/s10955-024-03355-z).
9. U. D. Jentschura and **L. T. Giorgini**, “Enhanced and Generalized One-Step Neville Algorithm: Fractional Powers and Access to the Convergence Rate,” [*Computer Physics Communications* **303**, 109280 (2024)](https://doi.org/10.1016/j.cpc.2024.109280).
10. **L. T. Giorgini**, U. D. Jentschura, E. M. Malatesta, T. Rizzo, and J. Zinn-Justin, “Instantons in φ⁴ Theories: Transseries, Virial Theorems, and Numerical Aspects,” [*Physical Review D* **110**, 036003 (2024)](https://doi.org/10.1103/PhysRevD.110.036003). Editors’ Suggestion.
11. N. D. B. Keyes, **L. T. Giorgini**, and J. S. Wettlaufer, “Stochastic Paleoclimatology: Modeling the EPICA Ice Core Climate Records,” [*Chaos* **33**, 093132 (2023)](https://doi.org/10.1063/5.0128814).
12. **L. T. Giorgini**, R. Eichhorn, M. Das, W. Moon, and J. S. Wettlaufer, “Thermodynamic Cost of Erasing Information in Finite Time,” [*Physical Review Research* **5**, 023084 (2023)](https://doi.org/10.1103/PhysRevResearch.5.023084).
13. **L. T. Giorgini**, W. Moon, N. Chen, and J. S. Wettlaufer, “Non-Gaussian Stochastic Dynamical Model for the El Niño Southern Oscillation,” [*Physical Review Research* **4**, L022065 (2022)](https://doi.org/10.1103/PhysRevResearch.4.L022065).
14. **L. T. Giorgini**, U. D. Jentschura, E. M. Malatesta, G. Parisi, T. Rizzo, and J. Zinn-Justin, “Correlation Functions of the Anharmonic Oscillator: Numerical Verification of Two-Loop Corrections to the Large-Order Behavior,” [*Physical Review D* **105**, 105012 (2022)](https://doi.org/10.1103/PhysRevD.105.105012).
15. W. Moon, **L. T. Giorgini**, and J. S. Wettlaufer, “Analytical Solution of Stochastic Resonance in the Nonadiabatic Regime,” [*Physical Review E* **104**, 044130 (2021)](https://doi.org/10.1103/PhysRevE.104.044130).
16. S. H. Lim, **L. T. Giorgini**, W. Moon, and J. S. Wettlaufer, “Predicting Critical Transitions in Multiscale Dynamical Systems Using Reservoir Computing,” [*Chaos* **30**, 123126 (2020)](https://doi.org/10.1063/5.0023764).
17. **L. T. Giorgini**, W. Moon, and J. S. Wettlaufer, “Analytical Survival Analysis of the Ornstein–Uhlenbeck Process,” [*Journal of Statistical Physics* **181**, 2404–2414 (2020)](https://doi.org/10.1007/s10955-020-02669-y).
18. **L. T. Giorgini**, U. D. Jentschura, E. M. Malatesta, G. Parisi, T. Rizzo, and J. Zinn-Justin, “Two-Loop Corrections to the Large-Order Behavior of Correlation Functions in the One-Dimensional N-Vector Model,” [*Physical Review D* **101**, 125001 (2020)](https://doi.org/10.1103/PhysRevD.101.125001).
19. **L. T. Giorgini**, S. H. Lim, W. Moon, and J. S. Wettlaufer, “Precursors to Rare Events in Stochastic Resonance,” [*EPL* **129**, 40003 (2020)](https://doi.org/10.1209/0295-5075/129/40003). Editor’s Choice.

### Conference and Workshop Publications

1. **L. T. Giorgini**, S. H. Lim, W. Moon, N. Chen, and J. S. Wettlaufer, “Modeling the El Niño Southern Oscillation with Neural Differential Equations,” [Time Series Workshop at ICML 2021 (2021)](https://roseyu.com/time-series-workshop/submissions/2021/TSW-ICML2021_paper_19.pdf).

## Open-source scientific software

- **[DiscreteTransformers.jl](https://github.com/ludogiorgi/DiscreteTransformers.jl):** Transformer-based ensemble forecasting and scenario generation for discretized time series. [Code](https://github.com/ludogiorgi/DiscreteTransformers.jl)
- **[ContinuousTransformers.jl](https://github.com/ludogiorgi/ContinuousTransformers.jl):** Continuous-state, delay-embedded transformer models for probabilistic forecasting. [Code](https://github.com/ludogiorgi/ContinuousTransformers.jl)
- **[FastSDE.jl](https://github.com/ludogiorgi/FastSDE):** High-performance Julia simulation of deterministic and stochastic dynamical systems. [Code](https://github.com/ludogiorgi/FastSDE)
- **[ScoreEstimation.jl](https://github.com/ludogiorgi/ScoreEstimation.jl):** KGMM-based score estimation using clustered Gaussian mixtures and neural interpolation. [Code](https://github.com/ludogiorgi/ScoreEstimation.jl) [Paper](https://doi.org/10.1016/j.physd.2026.135274)
- **[ParameterCalibration.jl](https://github.com/ludogiorgi/ParameterCalibration.jl):** GFDT-based sensitivity estimation and statistical parameter calibration from a single baseline simulation. [Code](https://github.com/ludogiorgi/ParameterCalibration.jl) [Paper](https://arxiv.org/abs/2509.19660)
- **[ScoreUNet1D.jl](https://github.com/ludogiorgi/ScoreUNet1D.jl):** Denoising-score-matching U-Net models and Langevin validation for one-dimensional fields. [Code](https://github.com/ludogiorgi/ScoreUNet1D.jl) [Paper](https://doi.org/10.1103/6qpv-lqmt)
- **[StateDependentMobility.jl](https://github.com/ludogiorgi/StateDependentMobility.jl):** Learning and validation of state-dependent mobility tensors from finite-lag trajectories and conditional scores. [Code](https://github.com/ludogiorgi/StateDependentMobility.jl) [Paper](https://arxiv.org/abs/2604.23952)

## Teaching

### MIT 18.305: Advanced Analytic Methods in Science and Engineering

**Instructor · Fall 2026**

18.305 is a graduate course covering asymptotic, multiscale, and singular-perturbation methods for extracting the dominant behavior of mathematical models across separated scales. I am the primary lecturer for the Fall 2026 offering.

### MIT 18.354J: Nonlinear Dynamics II — Continuum Systems

**Instructor · Spring 2026**

18.354J is a graduate course covering dimensional analysis, variational methods, stability, singular perturbations, waves, and pattern formation. I was the primary lecturer for the Spring 2026 offering.

## Contact

- **Email:** [ludogio@mit.edu](mailto:ludogio@mit.edu)
- **Office:** Room 2-157
- **Address:** [Department of Mathematics, MIT, 77 Massachusetts Avenue, Cambridge, MA 02139](https://maps.google.com/?q=MIT+Mathematics+Department,+77+Massachusetts+Avenue,+Cambridge,+MA+02139)

## Footer

© 2026 Ludovico Theo Giorgini
