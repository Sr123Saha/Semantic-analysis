---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:37800
- loss:CrossEntropyLoss
base_model: DeepPavlov/rubert-base-cased
pipeline_tag: text-classification
library_name: sentence-transformers
---

# CrossEncoder based on DeepPavlov/rubert-base-cased

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [DeepPavlov/rubert-base-cased](https://huggingface.co/DeepPavlov/rubert-base-cased) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text pair classification.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [DeepPavlov/rubert-base-cased](https://huggingface.co/DeepPavlov/rubert-base-cased) <!-- at revision 4036cab694767a299f2b9e6492909664d9414229 -->
- **Maximum Sequence Length:** 256 tokens
- **Number of Output Labels:** 3 labels
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

### Full Model Architecture

```
CrossEncoder(
  (0): Transformer({'transformer_task': 'sequence-classification', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'logits'}}, 'module_output_name': 'scores', 'architecture': 'BertForSequenceClassification'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import CrossEncoder

# Download from the 🤗 Hub
model = CrossEncoder("cross_encoder_model_id")
# Get scores for pairs of inputs
pairs = [
    ['Профессия: юрист. Уровень: junior. Требуемые навыки: судебная практика, договоры, консультирование, документооборот, гражданское право. Описание: Компания: ООО ТехноСофт\r\nГород: Пермь\r\nЗарплата: 218622 руб.\r\nО компании: ООО ТехноСофт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.\r\n\r\nТребования:\r\n• опыт работы от 4 лет\r\n• знание Судебная практика\r\n• знание Договоры\r\n• знание Консультирование\r\n• знание Документооборот\r\n• знание Гражданское пра', 'Профессия: юрист. Уровень: senior. Навыки: договорная работа, правовой анализ, претензионная работа, гк рф, согласование документов, консультирование, самостоятельность, внимательность. Общие навыки: консультирование. Совпадение навыков: 1. Покрытие требований: 0.20. Опыт: Если коротко, по направлению «Юрист» привык работать на уровне, где важны не только задачи, но и качество процесса вокруг них. Сильнее всего в задачах, где правовой риск надо не просто увидеть, а еще и понятно объяснить бизнесу, что с ним делать. Плюс комфортно работаю в темпе, когда многое меняется по ходу дела. Сильная сторона — не терять картину целиком, даже когда параллельно едет несколько на'],
    ['Профессия: менеджер по продажам. Уровень: junior. Требуемые навыки: b2b, холодные продажи, коммуникация, crm. Описание: Компания: ООО Интегра Софт\r\nГород: Казань\r\nЗарплата: 132703 руб.\r\nО компании: ООО Интегра Софт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.\r\n\r\nТребования:\r\n• опыт работы от 2 лет\r\n• знание B2B\r\n• знание Холодные продажи\r\n• знание Коммуникация\r\n• знание CRM\r\n\r\nОбязанности:\r\n• поддержка существующи', 'Профессия: frontend-разработчик. Уровень: junior. Навыки: react, next.js, typescript, rtk query, scss. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: Если коротко, вхожу в профессию по направлению «Frontend-разработчик» через стажировки, учебные кейсы и короткие практические задачи. Сильнее всего там, где нужно разложить большой экран на понятные компоненты и не утонуть в состоянии. Плюс быстро собираю контекст и не люблю оставлять хвосты. Нормально отношусь к простым задачам на входе, если они ведут к реальной практике. 2025 - 2026 | ООО Интег'],
    ['Профессия: системный администратор компания: ооо дата лайн город: санкт-петербург зарплата: 203914 руб. о компании: ооо дата лайн работает с аналитикой и обработкой данных. ищем специалиста в небольшую команду. требования: • опыт работы от 4 лет • знание vpn • знание zabbix • знание linux • знание bash • умение работать в команде обязанности: • решение технических проблем • настройка рабочих мест • поддержка серверов будет плюсом: понимание agile‑процессов. Уровень: senior. Требуемые навыки: vpn, zabbix, linux, bash, умение работать в команде. Описание: ООО Дата Лайн работает с аналитикой и обработкой данных. Ищем специалиста в небольшую команду.', 'Профессия: маркетолог. Уровень: senior. Навыки: smm, контент-план, b-тесты, креативы, email-маркетинг, сквозная аналитика, внимательность, самостоятельность. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: По направлению «Маркетолог» привык работать на уровне, где важны не только задачи, но и качество процесса вокруг них. Сильнее всего там, где нужно быстро проверить гипотезу, понять результат и не влюбляться в идею только потому, что она красивая. Обычно люблю, когда из хаоса получается понятный процесс. Умею не только закрывать свои задачи, но и подхватывать спорные места в процессе до того, как о'],
    ['Профессия: frontend developer компания: ооо точка роста город: москва зарплата: 117037 руб. о компании: ооо точка роста работает над веб‑платформами для малого бизнеса. команда расширяется из-за роста проекта. требования: • опыт работы от 2 лет • знание git • знание typescript • знание react • умение работать в команде обязанности: • работа с api • поддержка существующего frontend • исправление багов. Уровень: middle. Требуемые навыки: git, typescript, react, умение работать в команде. Описание: ООО Точка Роста работает над веб‑платформами для малого бизнеса. Команда расширяется из-за роста проекта.', 'Профессия: frontend-разработчик. Уровень: middle. Навыки: react, next.js, typescript, rtk query, scss, vite, внимательность. Общие навыки: react, typescript. Совпадение навыков: 2. Покрытие требований: 0.50. Опыт: Если коротко, за последние годы собрал крепкую практику в роли «Frontend-разработчик». Нравится переводить макеты и требования в интерфейсы, которыми реально удобно пользоваться каждый день. Плюс быстро собираю контекст и не люблю оставлять хвосты. Сильнее всего в командах, где ценят не шум, а стабильный результат и взрослую ответственность. 2025 - 2026 | ООО Интегра Софт | Frontend-разработчик\r\nС'],
    ['Профессия: frontend-разработчик. Уровень: junior. Требуемые навыки: redux, javascript, react, typescript. Описание: Компания: ООО Интегра Софт\r\nГород: Казань\r\nЗарплата: 156929 руб.\r\nО компании: ООО Интегра Софт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.\r\n\r\nТребования:\r\n• опыт работы от 2 лет\r\n• знание Redux\r\n• знание JavaScript\r\n• знание React\r\n• знание TypeScript\r\n\r\nОбязанности:\r\n• ведение документации\r\n• р', 'Профессия: графический дизайнер. Уровень: senior. Навыки: illustrator, полиграфия, бренд-гайды, презентации, digital-материалы, адаптация макетов, самостоятельность, инициативность, ответственность. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: В роли «Графический дизайнер» сильнее всего там, где нужно выстроить подход, снять хаос и подтянуть планку качества. Сильнее всего там, где нужно быстро собрать понятный визуал без лишнего шума и стилистических скачков. Лучше всего проявляюсь там, где нужно совместить hands-on работу, наставничество и здравый приоритет задач. 2022 - 2026 | ООО Проф Маркет | Графический дизайнер (ведущий)\r\nДелал ба'],
]
scores = model.predict(pairs)
print(scores)
# [[-2.8145 -1.5918  4.8125]
#  [ 5.5625 -2.3418 -3.5645]
#  [ 5.6758 -3.0391 -3.0723]
#  [-2.8359 -1.3936  4.6719]
#  [ 1.125   1.6006 -3.4531]]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 37,800 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                           | sentence_1                                                                           | label                                                              |
  |:---------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
  | type     | string                                                                               | string                                                                               | int                                                                |
  | modality | text                                                                                 | text                                                                                 |                                                                    |
  | details  | <ul><li>min: 99 tokens</li><li>mean: 142.22 tokens</li><li>max: 237 tokens</li></ul> | <ul><li>min: 98 tokens</li><li>mean: 148.12 tokens</li><li>max: 175 tokens</li></ul> | <ul><li>0: ~30.77%</li><li>1: ~31.73%</li><li>2: ~37.50%</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | label          |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
  | <code>Профессия: юрист. Уровень: junior. Требуемые навыки: судебная практика, договоры, консультирование, документооборот, гражданское право. Описание: Компания: ООО ТехноСофт  <br>Город: Пермь  <br>Зарплата: 218622 руб.  <br>О компании: ООО ТехноСофт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.  <br>  <br>Требования:  <br>• опыт работы от 4 лет  <br>• знание Судебная практика  <br>• знание Договоры  <br>• знание Консультирование  <br>• знание Документооборот  <br>• знание Гражданское пра</code>                                                                            | <code>Профессия: юрист. Уровень: senior. Навыки: договорная работа, правовой анализ, претензионная работа, гк рф, согласование документов, консультирование, самостоятельность, внимательность. Общие навыки: консультирование. Совпадение навыков: 1. Покрытие требований: 0.20. Опыт: Если коротко, по направлению «Юрист» привык работать на уровне, где важны не только задачи, но и качество процесса вокруг них. Сильнее всего в задачах, где правовой риск надо не просто увидеть, а еще и понятно объяснить бизнесу, что с ним делать. Плюс комфортно работаю в темпе, когда многое меняется по ходу дела. Сильная сторона — не терять картину целиком, даже когда параллельно едет несколько на</code> | <code>2</code> |
  | <code>Профессия: менеджер по продажам. Уровень: junior. Требуемые навыки: b2b, холодные продажи, коммуникация, crm. Описание: Компания: ООО Интегра Софт  <br>Город: Казань  <br>Зарплата: 132703 руб.  <br>О компании: ООО Интегра Софт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.  <br>  <br>Требования:  <br>• опыт работы от 2 лет  <br>• знание B2B  <br>• знание Холодные продажи  <br>• знание Коммуникация  <br>• знание CRM  <br>  <br>Обязанности:  <br>• поддержка существующи</code>                                                                                                | <code>Профессия: frontend-разработчик. Уровень: junior. Навыки: react, next.js, typescript, rtk query, scss. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: Если коротко, вхожу в профессию по направлению «Frontend-разработчик» через стажировки, учебные кейсы и короткие практические задачи. Сильнее всего там, где нужно разложить большой экран на понятные компоненты и не утонуть в состоянии. Плюс быстро собираю контекст и не люблю оставлять хвосты. Нормально отношусь к простым задачам на входе, если они ведут к реальной практике. 2025 - 2026 \| ООО Интег</code>                                                                                                   | <code>0</code> |
  | <code>Профессия: системный администратор компания: ооо дата лайн город: санкт-петербург зарплата: 203914 руб. о компании: ооо дата лайн работает с аналитикой и обработкой данных. ищем специалиста в небольшую команду. требования: • опыт работы от 4 лет • знание vpn • знание zabbix • знание linux • знание bash • умение работать в команде обязанности: • решение технических проблем • настройка рабочих мест • поддержка серверов будет плюсом: понимание agile‑процессов. Уровень: senior. Требуемые навыки: vpn, zabbix, linux, bash, умение работать в команде. Описание: ООО Дата Лайн работает с аналитикой и обработкой данных. Ищем специалиста в небольшую команду.</code> | <code>Профессия: маркетолог. Уровень: senior. Навыки: smm, контент-план, b-тесты, креативы, email-маркетинг, сквозная аналитика, внимательность, самостоятельность. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: По направлению «Маркетолог» привык работать на уровне, где важны не только задачи, но и качество процесса вокруг них. Сильнее всего там, где нужно быстро проверить гипотезу, понять результат и не влюбляться в идею только потому, что она красивая. Обычно люблю, когда из хаоса получается понятный процесс. Умею не только закрывать свои задачи, но и подхватывать спорные места в процессе до того, как о</code>                                             | <code>0</code> |
* Loss: [<code>CrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#crossentropyloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `fp16`: True
- `disable_tqdm`: False

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 8
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 8
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step  | Training Loss |
|:------:|:-----:|:-------------:|
| 0.1058 | 500   | 0.8838        |
| 0.2116 | 1000  | 0.6552        |
| 0.3175 | 1500  | 0.6184        |
| 0.4233 | 2000  | 0.5570        |
| 0.5291 | 2500  | 0.5265        |
| 0.6349 | 3000  | 0.5020        |
| 0.7407 | 3500  | 0.5133        |
| 0.8466 | 4000  | 0.4903        |
| 0.9524 | 4500  | 0.4687        |
| 1.0582 | 5000  | 0.4625        |
| 1.1640 | 5500  | 0.4501        |
| 1.2698 | 6000  | 0.4344        |
| 1.3757 | 6500  | 0.4241        |
| 1.4815 | 7000  | 0.3978        |
| 1.5873 | 7500  | 0.3813        |
| 1.6931 | 8000  | 0.3845        |
| 1.7989 | 8500  | 0.3961        |
| 1.9048 | 9000  | 0.3615        |
| 2.0106 | 9500  | 0.3555        |
| 2.1164 | 10000 | 0.3462        |
| 2.2222 | 10500 | 0.3247        |
| 2.3280 | 11000 | 0.3055        |
| 2.4339 | 11500 | 0.3331        |
| 2.5397 | 12000 | 0.2948        |
| 2.6455 | 12500 | 0.2929        |
| 2.7513 | 13000 | 0.3015        |
| 2.8571 | 13500 | 0.3004        |
| 2.9630 | 14000 | 0.3000        |


### Training Time
- **Training**: 29.2 minutes

### Framework Versions
- Python: 3.11.9
- Sentence Transformers: 5.5.1
- Transformers: 5.9.0
- PyTorch: 2.6.0+cu124
- Accelerate: 1.13.0
- Datasets: 4.8.5
- Tokenizers: 0.22.2

## Additional Resources

- [Training and Finetuning Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-reranker): the end-to-end guide for training or finetuning Cross Encoder (reranker) models.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video reranker models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal Cross Encoders.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->