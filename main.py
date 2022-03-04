
from models import model_builder
from opts import parser
from tools.dataset import get_dataset_info
import torch 

def main_worker(opt):
    """
    main worker for CNN training
    """
    get_dataset_info(opt)
    model = model_builder(opt)
    print(model)
    dummy = torch.zeros([32, 3, 224, 224]).cuda()
    output = model(dummy)
    print("output : ", output.shape)

if __name__ == "__main__":
    opt = parser.parse_args()
    main_worker(opt)