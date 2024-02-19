from ._explorers import ClipExplorer


# Decorator class defines what metrics to track and other metadata.
@ClipExplorer
def explorer(launcher):
	# Methods `slurm_` and `bind_` are in-place.
    #launcher.slurm_(gpus=4)  # All XPs scheduled with `launcher` will use 4 gpus.
    launcher.bind_({
        'norm.max_scale': 20, 
        'dset.n_recordings': 4,
        'model': 'clip_conv',
        'optim.batch_size' : 16,
        })  # set common params.

    more_subjects = {'dset.n_recordings': 8}
    selections = ['brennan2019']
    with launcher.job_array():
        for selection in selections:
            # The `bind()` method returns a sub-launcher with different params.
            # This won't affect the original launcher.
            sub = launcher.bind({'dset.selections': [selection]})
            # You schedule experiments by calling the (sub)-launcher.
            sub()
            sub({'optim.batch_size': 4})  #Experiment 1: does batch size influence CLIP ?
            # Following XP is just to get a noise level baseline
            sub({'optim.max_batches': 1, 'optim.epochs': 1, 'test.wer_random': True}) #
            # # Variations with different input speech-related representations.
            sub({'dset.features': ['MelSpectrum']}) #
            sub({'dset.features': ['MelSpectrum'], 'feature_model': 'deep_mel'})  # DeepMel
            # Then we train a regression model.
            ssub = sub.bind({'optim.loss': 'mse', 'dset.features': ['MelSpectrum']})
            ssub()
            sub(more_subjects) #what if we trained on some more subjects instead?