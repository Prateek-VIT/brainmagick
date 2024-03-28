# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""Ablation grid."""
from itertools import product  # noqa
from ._explorers import ClipExplorer
from ..train import main  # noqa

@ClipExplorer
def explorer(launcher):
    # launcher.slurm_(
    #     gpus=2, mem_per_gpu=200,
    #     partition="learnlab",
    # )
    # See conf/model/clip_conv.yaml for the configuration used.
    launcher.bind_({'model': 'clip_conv', 'optim.batch_size': 16,'override_n_subjects_model':3})
    total_recordings=196
    batch_size = 20
    seeds = [2036, 2037, 2038]
    audio_sets = ['gwilliams2022']
    with launcher.job_array():
        exps_var = product(seeds, audio_sets)
        initseed,initdset = next(exps_var)
        sub = [launcher.bind({'dset.selections': [initdset], 'override_n_subjects_model':3}, seed=initseed)]
        for seed, dset in exps_var:
            #the starting model
            sub[0]({"dset.n_recordings": batch_size})
            prevxp = main.get_xp(sub[0]._argv)
            for batch in range(batch_size,total_recordings,batch_size):
                #the continuing model
                sub.append(launcher.bind({"dset.selections":[initdset],"dset.n_recordings":batch_size,"dset.skip_recordings":batch},continue_sig=prevxp.sig,continue_best=True,seed=initseed))
                sub[batch//20]()
                prevxp = main.get_xp(sub[batch//20]._argv)
            
