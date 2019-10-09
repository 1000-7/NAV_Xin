# NAV_Xin



python train.py -mode validate -bert_data_path /home/ljw/wangxin/bert_file/bert_data/ss -model_path ../models/bert_transformer  -visible_gpus 0  -gpu_ranks 0 -batch_size 30000  -log_file ../logs/validate.log  -result_path ../results/cnndm -test_all -block_trigram true

python train.py -mode test -bert_data_path /home/ljw/wangxin/bert_file/bert_data/ss -model_path ../models/bert_transformer  -visible_gpus 0  -gpu_ranks 0 -batch_size 30000  -log_file ../logs/test.log  -result_path ../results/test -test_from ../models/bert_transformer/model_step_50000.pt -test_all -block_trigram true