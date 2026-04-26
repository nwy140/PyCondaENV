import torch
import sys

print('Python executable:', sys.executable)
print('Python version:', sys.version)

print('PyTorch version:', torch.__version__)

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', DEVICE)

if torch.cuda.is_available():
    try:
        print('CUDA version:', torch.version.cuda)
        print('GPU name:', torch.cuda.get_device_name(0))
    except Exception as e:
        print('Could not query GPU information:', e)

        
