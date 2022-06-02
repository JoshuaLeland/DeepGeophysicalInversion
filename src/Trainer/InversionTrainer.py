from ..InverseModels.IInverseModels import IInverseModel
from ..ForwardModels.IForwardModel import IFowardModel
from ..ModelGenerator.IModelGenerator import IModelGenerator
from ..ModelGenerator.IParameterGenerator import IParameterGenerator
from  ..Losses.IDataLoss import IDataLoss
from  ..Losses.IRegLoss import IRegLoss

class InversionTrainer:

    def __init__(self, inverse_model :IInverseModel, forward_model: IFowardModel, model_generator: IModelGenerator,
    data_loss: IDataLoss, reg_loss: IRegLoss, parameter_generator: IParameterGenerator, optimizer):
        self.inverse_model = inverse_model
        self.forward_model = forward_model
        self.model_generator = model_generator
        self.parameter_generator = parameter_generator
        self.data_loss = data_loss
        self.reg_loss = reg_loss
        self.optimizer = optimizer


    def train(self, num_iters, print_iters=10, print=False):
        for iter in range(num_iters):
            self.optimizer.zero_grad()
            loss = self._iter_()

            if print and (num_iters % print_iters == print_iters - 1):
                print("iter: %d".format(iter), "loss: {:.5f}".format(loss))

            loss.backward()
            self.optimizer.step()

    def _iter_(self):

        # Generate a random model.
        model = self.model_generator.build()
        parameters = self.parameter_generator.generate()

        # Simulate field data.
        field_data = self.forward_model.forward(model)

        # 'invert' field data.
        recovered_model = self.inverse_model.invert(field_data, parameters)

        # run the forward model.
        predicted_data = self.forward_model.forward(recovered_model)

        # calculate loss.
        return self.data_loss(field_data, predicted_data) + self.reg_loss(model, parameters)






