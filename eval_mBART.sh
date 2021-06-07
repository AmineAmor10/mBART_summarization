python -m torch.distributed.launch \
--nproc_per_node=8  transformers/examples/seq2seq/final_run_summarization_mbart.py \
--model_name_or_path saved/checkpoint-8000 \
--do_eval \
--do_predict \
--validation_file long_wiki_fr/valid.json \
--test_file long_wiki_fr/test.json \
--text_column text \
--summary_column summary \
--num_beams 8 \
--val_max_target_length 1024 \
--output_dir eval_results \
--per_device_eval_batch_size 1 \
--overwrite_output_dir \
--predict_with_generate \
--fp16

