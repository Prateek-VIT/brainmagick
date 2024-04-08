import torch
from torch import nn

class recurrence_plot(nn.Module):
  def __init__(self,
               in_channels: int,
               hidden_units: int,
               out_channels: int):
    super().__init__()
    self.conv1 = nn.Sequential(
      nn.Conv2d(in_channels=in_channels,
                out_channels=hidden_units,
                kernel_size=3, # how big is the square that's going over the image?
                stride=1, # default
                padding=1),# options = "valid" (no padding) or "same" (output has same shape as input) or int for specific number
      nn.ReLU(),
      nn.Conv2d(in_channels=hidden_units,
                out_channels=hidden_units,
                kernel_size=3,
                stride=1,
                padding=1),
      nn.ReLU(),
      nn.MaxPool2d(kernel_size=2)
    )
    self.conv2 = nn.Sequential(
        nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
    )
    self.feature_extractor = nn.Sequential(
        nn.Flatten(),
        nn.Linear(in_features=hidden_units*(in_channels**2)//4 ,
                      out_features=out_channels)
    )

  def forward(self,meg):
  # Fixed recurrence threshold in units of the time series' standard deviation
    EPS_std = 0.1
    # Default distance metric in phase space: "supremum"
    # Can also be set to "euclidean" or "manhattan".
    METRIC = "supremum"
    rp = torch.Tensor(RecurrencePlot(meg, metric=METRIC,
                        normalize=False, threshold_std=EPS_std))
    # convert the image into a tensor
    meg = rp.recurrence_matrix()

    meg = self.conv1(meg)
    meg = self.conv2(meg)
    meg = self.feature_extractor(meg)
    return meg