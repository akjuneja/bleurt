#!/bin/bash
# Fine-tune BLEURT script

python -m bleurt.finetune_md_bleurt \
  --init_bleurt_checkpoint "bleurt-base-512" \
  --train_set "data/complete_paraphrase/train_mixed_mulithead.jsonl" \
  --dev_set "data/complete_paraphrase/val_mixed_mulithead.jsonl" \
  --use_triplet_loss=False \
  --model_dir "./finetuned_models/multihead_mixed_complete_paraphrase_vector_score/" \
  --num_train_steps=500