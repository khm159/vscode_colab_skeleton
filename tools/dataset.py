def get_dataset_info(opt):
    """
    Set dataset information from dataset name 

    Args:
        opt : argument parser, 실험 세팅 

    Raises:
        NotImplementedError : 미구현 데이터셋일 시 

    Returns: None 
    """
    if opt.dataset == 'MNIST':
        opt.num_classes = 10
    elif opt.dataset == 'ImageNet':
        opt.num_classes = 1000
    else:
        NotImplementedError