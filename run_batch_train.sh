dora grid batch_train --dry_run --init
dora run -f fc009d54
dora run -f df3c2e06
dora run -f 5cdb73bb
dora run -f 059c9d21
dora run -f f6b3c37e
dora run -f 6697239b
dora run -f c3fc5567
dora run -f c9b2148b
dora run -f ee6796ec
dora run -f e252892d
dora run -f 6d4ede81
dora run -f aeb53f3f
dora run -f 75b7cb9c
dora run -f c48e4c2c
dora run -f b45e85a1
dora grid batch_train
dora grid batch_train --dry_run
python -m scripts.run_eval_probs grid_name="batch_train.py"