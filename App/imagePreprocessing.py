from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms
import Logging

log = Logging.app_logging()


class LeafDataset(Dataset):
    
    def __init__(self,images):
        
        self.x = []
        #self.y = []
        self.transform = transforms.Compose([transforms.ToTensor(),
                                             transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                                                  std=[0.229, 0.224, 0.225])
                                            ])
        
        try:
            for image in images:
                img = Image.open(image).resize((224,224))
                self.x.append(self.transform(img))
            log.info('Image preprossing completed')
        except Exception as e:
            log.error(e)


        
    
    def __len__(self):
        return len(self.x)