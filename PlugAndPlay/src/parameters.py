import os
import torch
import torchvision


class Images:

    PATH_TRAINING = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'data', 'training', '*.png')

    PATH_TEST = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'data', 'test', '*.png')

    # when None it will train on the original resolution, ow pass in tuple (,) for desired resolution
    RESOLUTION = (256,256)

    CHANNELS = 1

    TRANSFORM = torchvision.transforms.Compose([
        # torchvision.transforms.RandomResizedCrop(64), # still not clear # i think it could be a disadvantage as much as an advantage especially for classification - obviously depending on the image
        torchvision.transforms.RandomHorizontalFlip(),
        torchvision.transforms.RandomVerticalFlip(),
        torchvision.transforms.ToTensor() # maps a PIL grayscale image to [0,1]
    ])   # what does the normalisation do
    # torchvision.transforms.FiveCrop(size) # Crop the given PIL Image into four corners and the central crop


def getNetParameters(net = None):

    from DNN import Net

    M = 12

    if net == None:

        net=Net()

    KERNELS_SIMO = list(net.parameters())[0:M//2]  

    KERNELS_MISO = list(net.parameters())[-M//2:]

    ACTIVATIONS = list(net.parameters())[M//2:-M//2]

    return KERNELS_SIMO, KERNELS_MISO, ACTIVATIONS


class Minimiser:

    BATCH_SIZE = 9

    NUMB_FEAT_MAPS = 32

    NUMB_LAYERS = 10

    # Noise level
    SIGMA = [0.1]

    # number of dataset iterations
    EPOCHS = 20

    # training setup
    CRITERION = torch.nn.MSELoss()


class Models:


    DCNN_256_005 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_005noise.pth')

    DCNN_256_01 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_01noise.pth')
    DCNN_256_01_noproj = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_01noproj.pth')


    DCNN_256_001 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_001noise.pth')
    
    DCNN_256_015 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_015noise.pth')

    DCNN_256_02 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_02noise.pth')

    DCNN_256_00500801015 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_varnoise.pth')

    DCNN_256_008 = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'models', 'dncnn_256resolution_008noise.pth')

class TRAINING_MODEL:

    model = Models.DCNN_256_01_noproj

class Data:

    DENOISER_MSE = os.path.join(os.path.sep, os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'data', 'stats', 'mse.csv')


if __name__ == "__main__":

    print(getNetParameters()[0][0].size())
