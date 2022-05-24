# DeepGeophysicalInversion
Deep Learning framework to learn Geophysical Inverse problems.

Expected Progression.

1 - Learn simple workflow for 2D Gravity problem with fixed geometry and regualaization parameters.

2 - Try and learn parameterized inverse method for same problem.

3 - Generalize general PDE models and time dependent methods.

4 - Generalize to joint inversion.


1 - Data -> NN -> Model -> Forward operator -> Loss + Regularization.

2 - Data + Paramter -> Model -> Forward operator -> Loss + ???

3 - Same as above.

4 -> Physics embeddings 1..n -> transformer -> Model.

Deepmind uses Graph NNs for their flud simulators.  We can try this too.
