
"""
Trainer is an orchastrator for the training loop.  Using interfaces for each step in the pipeline.
ModelGenerator - Generates a a random model.
ForwardOperator - Generates the field data for a given model.
Noise Generator - Adds noise to a given dataset.
Inverse Operator - Runs the inverse function apporximator to build a model.
"""

class Trainer:

    def __init__(self, model_generator, forward_operator, noise_generator,
        inverse_operator, objective_function) -> None:
        self._forward_operator = forward_operator
        self._model_generator = model_generator
        self._noise_generator = noise_generator
        self._inverse_operator = inverse_operator
        self._objective_function = objective_function
    
    def train(self, num_iters, inversion_parameters):
        
        for _ in range(num_iters):
            self._training_step(inversion_parameters)


    def _training_step(self, inversion_parameters):
        # Generate model.
        model = self._model_generator.generate_model()

        # Generate field data.
        field_data = self._forward_operator.forward(model)

        # Add noise.
        field_data_noise = self._noise_generator.add_noise(field_data)

        # Invert the model: use the noisey dataset.
        for inversion_parameter in inversion_parameters:
            inverted_model = self._inverse_operator.invert(field_data_noise, inversion_parameter)

            # Build objective function.
            # Use clean data to help model ignore noise.
            objective_fn = self._objective_function.calculate(inverted_model, field_data, inversion_parameter)

            # Minimuze objective function.
            objective_fn.optimize()

