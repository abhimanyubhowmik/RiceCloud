import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import Logging

log = Logging.app_logging()


class vgg16:

    def __init__(self, dataset):
        self.dataset = dataset
        self.vgg16 = torch.load('Model/cnn_model.pth',map_location=torch.device('cpu'))
        self.device = torch.device("cpu")

    
    def test_data(self):
        try:
            criterion = nn.CrossEntropyLoss()
            optimizer = optim.RMSprop(vgg16.parameters(),lr=1e-4)
            vgg16 = vgg16.to(self.device)

            X_test = []
            with torch.no_grad():
                for data in self.dataset.x:
                    data = data.to(self.device)
                    data = data.unsqueeze(0)
                    outputs = vgg16(data)
                    X_test.append(outputs)
                
            X_test_np = np.zeros([1, 4096])
            for i in range(len(X_test)):
                if torch.cuda.is_available():
                    arr = X_test[i].cpu().numpy()
                    X_test_np = np.concatenate((X_test_np, arr), axis=0)
                else:
                    arr = X_test[i].numpy()
                    X_test_np = np.concatenate((X_test_np, arr), axis=0)
            X_test = X_test_np[1:,:]
            log.info('Feture Selection Completed')
            return X_test

        except Exception as e:
            log.error(e)






    





    


