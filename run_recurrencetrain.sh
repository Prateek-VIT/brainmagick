dora run dset.selections=[gwilliams2022] download_only=true
dora grid RecurrenceTrain --dry_run --init
dora run -f cee1ce25 
dora run -f a95edc12 
dora run -f c139b441 
dora run -f 03713fbc 
dora run -f ff1fc34d 
dora run -f 0c6082d9 
dora run -f daaeadad 
dora run -f d8eaa124 
dora run -f f86c83f5 
dora run -f 62434dc2 
dora grid RecurrenceTrain
dora grid RecurrenceTrain --dry_run
python -m scripts.run_eval_probs grid_name="RecurrenceTrain"