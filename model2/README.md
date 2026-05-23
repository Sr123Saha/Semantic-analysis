---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:37800
- loss:CrossEntropyLoss
base_model: cross-encoder/ms-marco-MiniLM-L6-v2
pipeline_tag: text-classification
library_name: sentence-transformers
---

# CrossEncoder based on cross-encoder/ms-marco-MiniLM-L6-v2

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [cross-encoder/ms-marco-MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text pair classification.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [cross-encoder/ms-marco-MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2) <!-- at revision c5ee24cb16019beea0893ab7796b1df96625c6b8 -->
- **Maximum Sequence Length:** 128 tokens
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
    ['Профессия: специалист поддержки компания: ооо интегра софт город: новосибирск зарплата: 79585 руб. о компании: ооо интегра софт занимается заказной разработкой и поддержкой корпоративных систем. команда расширяется из-за роста проекта. требования: • опыт работы от 6 месяцев • знание тикеты • знание коммуникация обязанности: • обработка обращений пользователей • решение типовых проблем • эскалация сложных инцидентов будет плюсом: понимание agile‑процессов. Уровень: junior. Требуемые навыки: тикеты, коммуникация. Описание: ООО Интегра Софт занимается заказной разработкой и поддержкой корпоративных систем. Команда расширяется из-за роста проекта.', 'Профессия: менеджер по продажам. Уровень: middle. Навыки: холодные звонки, b2c продажи, воронка продаж, договоры, повторные продажи, презентации, спокойная коммуникация. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: За последние годы собрал крепкую практику в роли «Менеджер по продажам». Сильнее всего там, где нужно разговаривать с клиентом по делу и не сливать лид после первого возражения. Обычно комфортно работаю в темпе, когда многое меняется по ходу дела. Си'],
    ['Профессия: специалист поддержки компания: ооо бизнес партнер город: новосибирск зарплата: 158655 руб. о компании: ооо бизнес партнер автоматизирует процессы для корпоративных клиентов. проект развивается уже несколько лет, поэтому часть задач связана не только с новой разработкой, но и с поддержкой текущих решений. ищем человека, которому будет комфортно работать в команде, где многие процессы уже выстроены, но при этом регулярно появляются новые задачи и доработки. требования: • знание crm • знание тикеты • знание коммуникация обязанности: • ведение внутренней документации • решение типовых проблем • обработка обращений пользователей. Уровень: senior. Требуемые навыки: crm, тикеты, коммуникация. Описание: ООО Бизнес Партнер автоматизирует процессы для корпоративных клиентов. Проект развивается уже несколько лет, поэтому часть задач связана не только с новой разработкой, но и с поддержкой текущих решений. Ищем человека, которому будет комфортно работат', 'Профессия: специалист поддержки. Уровень: senior. Навыки: crm, обработка обращений, чат-поддержка, email support, sla, база знаний, системность, спокойная коммуникация. Общие навыки: crm. Совпадение навыков: 1. Покрытие требований: 0.33. Опыт: В роли «Специалист поддержки» сильнее всего там, где нужно выстроить подход, снять хаос и подтянуть планку качества. Сильнее всего в ситуациях, где надо и услышать клиента, и не потерять техническую суть вопроса. Обычно быстро собираю контекст и не л'],
    ['Профессия: frontend developer компания: ооо точка роста город: екатеринбург зарплата: 205394 руб. о компании: ооо точка роста работает над веб‑платформами для малого бизнеса. у нас нет жесткого разделения задач, поэтому иногда потребуется взаимодействовать со смежными специалистами и участвовать в обсуждении технических решений. важна адекватная коммуникация, спокойное отношение к правкам и готовность постепенно погружаться в проект. требования: • опыт работы от 4 лет • знание redux • знание rest api • знание react • внимательность к задачам обязанности: • исправление багов • работа с api • разработка пользовательских интерфейсов будет плюсом: опыт поддержки legacy‑проектов. Уровень: senior. Требуемые навыки: redux, rest api, react, внимательность к задачам. Описание: ООО Точка Роста работает над веб‑платформами для малого бизнеса. У нас нет жесткого разделения задач, поэтому иногда потребуется взаимодействовать со смежными специалистами и участвовать в обсуждении технических решений. Важна адекватная коммуникация', 'Профессия: тестировщик по. Уровень: middle. Навыки: jira, testrail, rest api, chrome devtools, регрессионное тестирование, баг-репорты, дотошность. Общие навыки: rest api. Совпадение навыков: 1. Покрытие требований: 0.25. Опыт: За последние годы собрал крепкую практику в роли «Тестировщик ПО». Комфортно работаю на стыке логики, внимательности и спокойной коммуникации с разработкой и аналитиками. Обычно не жду, пока кто-то разложит работу по полочкам, а сам привожу ее к рабо'],
    ['Профессия: инженер пто. Уровень: junior. Требуемые навыки: исполнительная документация, сметы, проектирование, чтение чертежей, autocad. Описание: Компания: ООО Городской Сервис\r\nГород: Екатеринбург\r\nЗарплата: 245805 руб.\r\nО компании: ООО Городской Сервис занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направ', 'Профессия: специалист по логистике. Уровень: senior. Навыки: маршрутизация, перевозчики, транспортные документы, excel, 1с, статусы поставок, ответственность, умение держать сроки. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: Если коротко, по направлению «Специалист по логистике» привык работать на уровне, где важны не только задачи, но и качество процесса вокруг них. Комфортно работаю с большим количеством статусов, документов и согласований, если есть понятный поток. Пл'],
    ['Профессия: бухгалтер. Уровень: junior. Требуемые навыки: бухгалтерия, первичная документация, excel, 1с, налоговая отчетность. Описание: Компания: АО ФинТех Решения\r\nГород: Новосибирск\r\nЗарплата: 75518 руб.\r\nО компании: АО ФинТех Решения занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.\r\n', 'Профессия: специалист поддержки. Уровень: junior. Навыки: crm, обработка обращений, чат-поддержка, email support, sla, база знаний, внимание к деталям, работа в команде. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: Есть опыт самостоятельной работы в роли «Специалист поддержки», без постоянного ручного контроля. Спокойно объясняю сложное простым языком и не раздражаюсь, когда человек нервничает сильнее, чем проблема того заслуживает. Не люблю обещать лишнее, но '],
]
scores = model.predict(pairs)
print(scores)
# [[ 1.7295e+00 -1.2334e+00 -6.7383e-01]
#  [-1.4834e+00 -1.4834e+00  2.9004e+00]
#  [-2.1270e+00 -9.2773e-01  3.2051e+00]
#  [-1.2285e+00  1.6797e+00 -1.0281e-03]
#  [ 3.8110e-01  2.3066e+00 -2.2422e+00]]
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
  | details  | <ul><li>min: 128 tokens</li><li>mean: 128.0 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 128 tokens</li><li>mean: 128.0 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>0: ~28.85%</li><li>1: ~37.50%</li><li>2: ~33.65%</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | label          |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
  | <code>Профессия: специалист поддержки компания: ооо интегра софт город: новосибирск зарплата: 79585 руб. о компании: ооо интегра софт занимается заказной разработкой и поддержкой корпоративных систем. команда расширяется из-за роста проекта. требования: • опыт работы от 6 месяцев • знание тикеты • знание коммуникация обязанности: • обработка обращений пользователей • решение типовых проблем • эскалация сложных инцидентов будет плюсом: понимание agile‑процессов. Уровень: junior. Требуемые навыки: тикеты, коммуникация. Описание: ООО Интегра Софт занимается заказной разработкой и поддержкой корпоративных систем. Команда расширяется из-за роста проекта.</code>                                                                                                                                                                                                                                                                                                                                                                 | <code>Профессия: менеджер по продажам. Уровень: middle. Навыки: холодные звонки, b2c продажи, воронка продаж, договоры, повторные продажи, презентации, спокойная коммуникация. Общие навыки: . Совпадение навыков: 0. Покрытие требований: 0.00. Опыт: За последние годы собрал крепкую практику в роли «Менеджер по продажам». Сильнее всего там, где нужно разговаривать с клиентом по делу и не сливать лид после первого возражения. Обычно комфортно работаю в темпе, когда многое меняется по ходу дела. Си</code>   | <code>1</code> |
  | <code>Профессия: специалист поддержки компания: ооо бизнес партнер город: новосибирск зарплата: 158655 руб. о компании: ооо бизнес партнер автоматизирует процессы для корпоративных клиентов. проект развивается уже несколько лет, поэтому часть задач связана не только с новой разработкой, но и с поддержкой текущих решений. ищем человека, которому будет комфортно работать в команде, где многие процессы уже выстроены, но при этом регулярно появляются новые задачи и доработки. требования: • знание crm • знание тикеты • знание коммуникация обязанности: • ведение внутренней документации • решение типовых проблем • обработка обращений пользователей. Уровень: senior. Требуемые навыки: crm, тикеты, коммуникация. Описание: ООО Бизнес Партнер автоматизирует процессы для корпоративных клиентов. Проект развивается уже несколько лет, поэтому часть задач связана не только с новой разработкой, но и с поддержкой текущих решений. Ищем человека, которому будет комфортно работат</code>                                      | <code>Профессия: специалист поддержки. Уровень: senior. Навыки: crm, обработка обращений, чат-поддержка, email support, sla, база знаний, системность, спокойная коммуникация. Общие навыки: crm. Совпадение навыков: 1. Покрытие требований: 0.33. Опыт: В роли «Специалист поддержки» сильнее всего там, где нужно выстроить подход, снять хаос и подтянуть планку качества. Сильнее всего в ситуациях, где надо и услышать клиента, и не потерять техническую суть вопроса. Обычно быстро собираю контекст и не л</code> | <code>2</code> |
  | <code>Профессия: frontend developer компания: ооо точка роста город: екатеринбург зарплата: 205394 руб. о компании: ооо точка роста работает над веб‑платформами для малого бизнеса. у нас нет жесткого разделения задач, поэтому иногда потребуется взаимодействовать со смежными специалистами и участвовать в обсуждении технических решений. важна адекватная коммуникация, спокойное отношение к правкам и готовность постепенно погружаться в проект. требования: • опыт работы от 4 лет • знание redux • знание rest api • знание react • внимательность к задачам обязанности: • исправление багов • работа с api • разработка пользовательских интерфейсов будет плюсом: опыт поддержки legacy‑проектов. Уровень: senior. Требуемые навыки: redux, rest api, react, внимательность к задачам. Описание: ООО Точка Роста работает над веб‑платформами для малого бизнеса. У нас нет жесткого разделения задач, поэтому иногда потребуется взаимодействовать со смежными специалистами и участвовать в обсуждении технических решений. ...</code> | <code>Профессия: тестировщик по. Уровень: middle. Навыки: jira, testrail, rest api, chrome devtools, регрессионное тестирование, баг-репорты, дотошность. Общие навыки: rest api. Совпадение навыков: 1. Покрытие требований: 0.25. Опыт: За последние годы собрал крепкую практику в роли «Тестировщик ПО». Комфортно работаю на стыке логики, внимательности и спокойной коммуникации с разработкой и аналитиками. Обычно не жду, пока кто-то разложит работу по полочкам, а сам привожу ее к рабо</code>                 | <code>2</code> |
* Loss: [<code>CrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#crossentropyloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 4
- `fp16`: True
- `disable_tqdm`: False
- `per_device_eval_batch_size`: 4

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 4
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
- `per_device_eval_batch_size`: 4
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
| 0.0529 | 500   | 1.0953        |
| 0.1058 | 1000  | 1.0178        |
| 0.1587 | 1500  | 0.9189        |
| 0.2116 | 2000  | 0.8693        |
| 0.2646 | 2500  | 0.8360        |
| 0.3175 | 3000  | 0.8119        |
| 0.3704 | 3500  | 0.7814        |
| 0.4233 | 4000  | 0.7242        |
| 0.4762 | 4500  | 0.7459        |
| 0.5291 | 5000  | 0.7267        |
| 0.5820 | 5500  | 0.7333        |
| 0.6349 | 6000  | 0.7235        |
| 0.6878 | 6500  | 0.6934        |
| 0.7407 | 7000  | 0.6844        |
| 0.7937 | 7500  | 0.6488        |
| 0.8466 | 8000  | 0.6779        |
| 0.8995 | 8500  | 0.6712        |
| 0.9524 | 9000  | 0.6444        |
| 1.0053 | 9500  | 0.6552        |
| 1.0582 | 10000 | 0.6462        |
| 1.1111 | 10500 | 0.6867        |
| 1.1640 | 11000 | 0.6701        |
| 1.2169 | 11500 | 0.6515        |
| 1.2698 | 12000 | 0.6520        |
| 1.3228 | 12500 | 0.6265        |
| 1.3757 | 13000 | 0.6408        |
| 1.4286 | 13500 | 0.6495        |
| 1.4815 | 14000 | 0.6205        |
| 1.5344 | 14500 | 0.6247        |
| 1.5873 | 15000 | 0.6167        |
| 1.6402 | 15500 | 0.6192        |
| 1.6931 | 16000 | 0.6184        |
| 1.7460 | 16500 | 0.6187        |
| 1.7989 | 17000 | 0.6172        |
| 1.8519 | 17500 | 0.5724        |
| 1.9048 | 18000 | 0.6102        |
| 1.9577 | 18500 | 0.6208        |
| 2.0106 | 19000 | 0.6216        |
| 2.0635 | 19500 | 0.5979        |
| 2.1164 | 20000 | 0.5874        |
| 2.1693 | 20500 | 0.6330        |
| 2.2222 | 21000 | 0.5734        |
| 2.2751 | 21500 | 0.5985        |
| 2.3280 | 22000 | 0.6108        |
| 2.3810 | 22500 | 0.5928        |
| 2.4339 | 23000 | 0.5392        |
| 2.4868 | 23500 | 0.6155        |
| 2.5397 | 24000 | 0.5911        |
| 2.5926 | 24500 | 0.5738        |
| 2.6455 | 25000 | 0.5731        |
| 2.6984 | 25500 | 0.5840        |
| 2.7513 | 26000 | 0.5969        |
| 2.8042 | 26500 | 0.5420        |
| 2.8571 | 27000 | 0.5517        |
| 2.9101 | 27500 | 0.6118        |
| 2.9630 | 28000 | 0.6391        |


### Training Time
- **Training**: 23.2 minutes

### Framework Versions
- Python: 3.11.9
- Sentence Transformers: 5.5.1
- Transformers: 5.9.0
- PyTorch: 2.5.1+cu121
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