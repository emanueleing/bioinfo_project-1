import torch
from tensorboardX import SummaryWriter
from abc import abstractmethod


class BaseTrainer:
    """
    Base class for all trainers
    """

    def __init__(self,
                 model,
                 criterion,
                 metric_fnts,
                 optimizer,
                 config):
        self.config = config

        self.model = model
        self.criterion = criterion
        self.metric_fnts = metric_fnts
        self.optimizer = optimizer

        cfg_trainer = config['trainer']
        self.epochs = cfg_trainer['epochs']
        self.save_period = cfg_trainer['save_period']

        self.checkpoint_dir = config['save_dir']

        # TODO: Tensorboard writer
        # self.writer = Tens
        '''
        # TODO: Resume Network
        if config.resume is not None:
        '''

    @abstractmethod
    def _train_epoch(self, epoch):
        """
        Train logic for an epoch

        :param epoch: Current epoch number
        :return: None
        """
        raise NotImplemented