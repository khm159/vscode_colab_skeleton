import torchvision.models as models 

def model_builder(opt):
    """
    simple model builder using torchvision 

    Args:
        opt : argument parser, 실험 세팅 존재 

    Raises:
        NotImplementedError : 미구현 모델 입력시 
        TODO: 다른 모델 추가하기 

    Returns:
        model : pytorch pretrained CNN model 
                if selected pretrained options 
                else default initialized model  
    """
    if opt.arch == 'resnet18':
        if opt.num_classes == 1000:
            return models.resnet18(opt.pretrained).cuda()
        else:
            model = models.resnet18(opt.pretrained)
            model.fc = nn.Linear(
                models.resnet.Bottleneck.expansion*512,
                opt.num_classes
                )
            return model.cuda()
    else:
        NotImplementedError
