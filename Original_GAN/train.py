import torch
import torch.nn as nn
import torch.cuda as cuda
import torch.optim as optim
import torchvision.transforms as transforms
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=200)
parser.add_argument('--batch_size', type=int, default=128)
parser.add_argument('--lr', type=float, default=0.001)
parser.add_argument('--latent_dim', type=int, default=288)
parser.add_argument('--img_width', type=int) # default ?
parser.add_argument('--img_height', type=int)
parser.add_argument('--channels', type=int, default=3)
parser.add_argument('--sample_interval', type=int, default=400)
