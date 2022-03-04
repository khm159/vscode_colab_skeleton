
from models import model_builder
from opts import opt 

def main_worker(opt):
    """
    main worker for CNN training
    """
    model = model_builder(opt)
    print(model)
    dummy = torch.zeros([32, 3, 224, 224]).cuda()
    output = model(dummy)
    print("output : ", output.shape)

if __name__ == "__main__":
    main_worker(opt)