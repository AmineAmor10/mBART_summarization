python -m torch.distributed.launch \
--nproc_per_node=8  transformers/examples/seq2seq/custom_run_summarization_mbart50_tokenizer.py \
--model_name_or_path saved_4beams/checkpoint-8000 \
--do_eval \
--do_predict \
--validation_file long_wiki_fr/valid.json \
--test_file long_wiki_fr/test.json \
--text_column text \
--summary_column summary \
--num_beams 4 \
--val_max_target_length 1024 \
--output_dir eval_results_4beams \
--per_device_eval_batch_size 1 \
--overwrite_output_dir \
--predict_with_generate \
--fp16

