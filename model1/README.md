---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:40910
- loss:BinaryCrossEntropyLoss
base_model: DiTy/cross-encoder-russian-msmarco
pipeline_tag: text-ranking
library_name: sentence-transformers
metrics:
- pearson
- spearman
model-index:
- name: CrossEncoder based on DiTy/cross-encoder-russian-msmarco
  results:
  - task:
      type: cross-encoder-correlation
      name: Cross Encoder Correlation
    dataset:
      name: validation
      type: validation
    metrics:
    - type: pearson
      value: 0.739165862296372
      name: Pearson
    - type: spearman
      value: 0.730104725656858
      name: Spearman
---

# CrossEncoder based on DiTy/cross-encoder-russian-msmarco

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [DiTy/cross-encoder-russian-msmarco](https://huggingface.co/DiTy/cross-encoder-russian-msmarco) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [DiTy/cross-encoder-russian-msmarco](https://huggingface.co/DiTy/cross-encoder-russian-msmarco) <!-- at revision 9029bab08103ad171724b510d312befa5b476293 -->
- **Maximum Sequence Length:** 512 tokens
- **Number of Output Labels:** 1 label
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
    ['Компания: ООО ТехноСофт  Город: Новосибирск  Зарплата: 159735 руб.  О компании: ООО ТехноСофт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 2 лет  • знание React  • знание JavaScript  • знание REST API  • знание TypeScript    Обязанности:  • взаимодействие со смежными отделами  • участие в командной разработке  • поддержка существующих решений  ', 'В направлении «Контент-менеджер» уже работаю достаточно уверенно и без долгого разгона. Комфортно работать с большим количеством материалов, если у них есть понятная система и редакционный ритм. Обычно спокойно отношусь к рутине, если задача и критерии результата понятны. Комфортно беру задачи целиком, если понятен результат и есть нормальная коммуникация со смежниками. 2024 - 2026 | ООО Медиа Групп | Контент-менеджер  Поддерживал редакционный календарь, правил страницы и адаптировал материалы под разные площадки и форматы.  Брал на себя заметный кусок процесса и не прятался за формулировками. Редко требовал ручного напоминания, когда сроки и критерии уже были согласованы.'],
    ['Компания: АО Медиа Платформа  Город: Москва  Зарплата: 148235 руб.  О компании: АО Медиа Платформа занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 2 лет  • знание Чтение чертежей  • знание Проектирование  • знание AutoCAD  • знание Сметы    Обязанности:  • взаимодействие со смежными отделами  • оптимизация процессов  • ведение документации  ', 'Если коротко, как сильный специалист по направлению «Инженер ПТО» полезен там, где задач много, а понятности мало. Сильнее всего там, где нужно быстро навести порядок в документации и не упустить важные детали по объекту. Плюс люблю, когда из хаоса получается понятный процесс. Нравятся роли, где можно влиять на качество решений, стандарты и темп команды, а не только закрывать тикеты. 2024 - 2026 | ООО Городской Сервис | Инженер ПТО (ведущий)  Готовил исполнительную документацию, сверял объемы по объекту и держал в порядке комплект документов для сдачи.  Брал ответственность за результат шире своей зоны. Команда за счет этого работала ровнее и меньше зависела от ручного контроля.  2022 - 2024 | ООО Северный Вектор | Инженер ПТО (senior)  Готовил исполнительную документацию, сверял объемы по объекту и держал в порядке комплект документов для сдачи.  Поддерживал процесс в собранном виде даже на длинной и сложной дистанции. Вокруг работы появлялись понятные правила, а не только героическое'],
    ['Компания: ООО Бизнес Партнер  Город: Казань  Зарплата: 52978 руб.  О компании: ООО Бизнес Партнер занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 6 месяцев  • знание Коммуникация  • знание Тикеты  • знание Helpdesk  • знание CRM  • знание Linux    Обязанности:  • оптимизация процессов  • поддержка существующих решений  • участие в командной разработке  ', 'Если коротко, рассматриваю стажерскую или стартовую позицию в «Администратор». Сильнее всего там, где нужно держать контакт с людьми, не терять детали и не создавать суету вокруг простых вопросов. Плюс предпочитаю понятные договоренности и рабочую коммуникацию без лишнего шума. Сейчас важнее всего набрать крепкую базу и научиться работать в команде без лишней суеты. 2025 - 2026 | ООО Городской Сервис | Администратор (стажер)  Встречал посетителей, вел запись, работал со звонками и держал фронт процесса в аккуратном состоянии.  Держал темп даже там, где часть вещей приходилось осваивать на месте. при этом не откладывал мелкие правки до бесконечности.'],
    ['Компания: ООО Интегра Софт  Город: Пермь  Зарплата: 130256 руб.  О компании: ООО Интегра Софт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 2 лет  • знание Контент  • знание CMS  • знание Photoshop  • знание SEO  • знание Копирайтинг    Обязанности:  • ведение документации  • оптимизация процессов  • участие в командной разработке  ', 'Опыт в направлении «Офис-менеджер» позволяет брать неоднозначные задачи и быстро приводить их к рабочему виду. Нравится наводить порядок в операционке и делать так, чтобы команде было проще работать. Обычно стараюсь оставлять после себя порядок в файлах, задачах и договоренностях. Полезен там, где нужен самостоятельный человек с хорошим чувством приоритетов и качества. 2025 - 2026 | ООО Точка Роста | Офис-менеджер (senior)  Вел документооборот, координировал встречи и следил, чтобы бытовые и административные вопросы не тормозили команду.  Помогал выравнивать качество работы по команде. В итоге сложные задачи переставали висеть между людьми и реально двигались вперед.  2023 - 2025 | ООО Точка Роста | Офис-менеджер (middle)  Поддерживал офисную рутину: закупки, календарь руководителя, командировки и взаимодействие с подрядчиками.  Подхватывал сложные участки, где не хватало структуры. Это заметно снимало лишние круги согласований и экономило время на релизах.'],
    ['ООО Точка Роста работает над веб‑платформами для малого бизнеса. Нужен человек для поддержки текущих задач.', 'За последние годы собрал крепкую практику в роли «Администратор». Хочу быстрее набрать реальную практику. 2023 - 2026 | ООО Северный Вектор | Администратор (middle)  Координировал расписание, обрабатывал сообщения и не давал бытовым сбоям разъезжаться по всей смене.  Собирал рабочий контекст сам, без ожидания, что его кто-то полностью разложит. Редко требовал ручного напоминания, когда сроки и критерии уже были согласованы.  2022 - 2023 | ООО Проф Маркет | Администратор (junior)  Координировал расписание, обрабатывал сообщения и не давал бытовым сбоям разъезжаться по всей смене.  Спокойно вел задачи от уточнения деталей до понятной сдачи результата. Держал сроки без привычки спасать все только последним вечером.'],
]
scores = model.predict(pairs)
print(scores)
# [0.5984 0.9376 0.0017 0.6079 0.6861]

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    'Компания: ООО ТехноСофт  Город: Новосибирск  Зарплата: 159735 руб.  О компании: ООО ТехноСофт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 2 лет  • знание React  • знание JavaScript  • знание REST API  • знание TypeScript    Обязанности:  • взаимодействие со смежными отделами  • участие в командной разработке  • поддержка существующих решений  ',
    [
        'В направлении «Контент-менеджер» уже работаю достаточно уверенно и без долгого разгона. Комфортно работать с большим количеством материалов, если у них есть понятная система и редакционный ритм. Обычно спокойно отношусь к рутине, если задача и критерии результата понятны. Комфортно беру задачи целиком, если понятен результат и есть нормальная коммуникация со смежниками. 2024 - 2026 | ООО Медиа Групп | Контент-менеджер  Поддерживал редакционный календарь, правил страницы и адаптировал материалы под разные площадки и форматы.  Брал на себя заметный кусок процесса и не прятался за формулировками. Редко требовал ручного напоминания, когда сроки и критерии уже были согласованы.',
        'Если коротко, как сильный специалист по направлению «Инженер ПТО» полезен там, где задач много, а понятности мало. Сильнее всего там, где нужно быстро навести порядок в документации и не упустить важные детали по объекту. Плюс люблю, когда из хаоса получается понятный процесс. Нравятся роли, где можно влиять на качество решений, стандарты и темп команды, а не только закрывать тикеты. 2024 - 2026 | ООО Городской Сервис | Инженер ПТО (ведущий)  Готовил исполнительную документацию, сверял объемы по объекту и держал в порядке комплект документов для сдачи.  Брал ответственность за результат шире своей зоны. Команда за счет этого работала ровнее и меньше зависела от ручного контроля.  2022 - 2024 | ООО Северный Вектор | Инженер ПТО (senior)  Готовил исполнительную документацию, сверял объемы по объекту и держал в порядке комплект документов для сдачи.  Поддерживал процесс в собранном виде даже на длинной и сложной дистанции. Вокруг работы появлялись понятные правила, а не только героическое',
        'Если коротко, рассматриваю стажерскую или стартовую позицию в «Администратор». Сильнее всего там, где нужно держать контакт с людьми, не терять детали и не создавать суету вокруг простых вопросов. Плюс предпочитаю понятные договоренности и рабочую коммуникацию без лишнего шума. Сейчас важнее всего набрать крепкую базу и научиться работать в команде без лишней суеты. 2025 - 2026 | ООО Городской Сервис | Администратор (стажер)  Встречал посетителей, вел запись, работал со звонками и держал фронт процесса в аккуратном состоянии.  Держал темп даже там, где часть вещей приходилось осваивать на месте. при этом не откладывал мелкие правки до бесконечности.',
        'Опыт в направлении «Офис-менеджер» позволяет брать неоднозначные задачи и быстро приводить их к рабочему виду. Нравится наводить порядок в операционке и делать так, чтобы команде было проще работать. Обычно стараюсь оставлять после себя порядок в файлах, задачах и договоренностях. Полезен там, где нужен самостоятельный человек с хорошим чувством приоритетов и качества. 2025 - 2026 | ООО Точка Роста | Офис-менеджер (senior)  Вел документооборот, координировал встречи и следил, чтобы бытовые и административные вопросы не тормозили команду.  Помогал выравнивать качество работы по команде. В итоге сложные задачи переставали висеть между людьми и реально двигались вперед.  2023 - 2025 | ООО Точка Роста | Офис-менеджер (middle)  Поддерживал офисную рутину: закупки, календарь руководителя, командировки и взаимодействие с подрядчиками.  Подхватывал сложные участки, где не хватало структуры. Это заметно снимало лишние круги согласований и экономило время на релизах.',
        'За последние годы собрал крепкую практику в роли «Администратор». Хочу быстрее набрать реальную практику. 2023 - 2026 | ООО Северный Вектор | Администратор (middle)  Координировал расписание, обрабатывал сообщения и не давал бытовым сбоям разъезжаться по всей смене.  Собирал рабочий контекст сам, без ожидания, что его кто-то полностью разложит. Редко требовал ручного напоминания, когда сроки и критерии уже были согласованы.  2022 - 2023 | ООО Проф Маркет | Администратор (junior)  Координировал расписание, обрабатывал сообщения и не давал бытовым сбоям разъезжаться по всей смене.  Спокойно вел задачи от уточнения деталей до понятной сдачи результата. Держал сроки без привычки спасать все только последним вечером.',
    ]
)
# [{'corpus_id': ..., 'score': ...}, {'corpus_id': ..., 'score': ...}, ...]
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

## Evaluation

### Metrics

#### Cross Encoder Correlation

* Dataset: `validation`
* Evaluated with [<code>CECorrelationEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CECorrelationEvaluator)

| Metric       | Value      |
|:-------------|:-----------|
| pearson      | 0.7392     |
| **spearman** | **0.7301** |

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

* Size: 40,910 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                        | sentence_1                                                                           | label                                                          |
  |:---------|:----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type     | string                                                                            | string                                                                               | float                                                          |
  | modality | text                                                                              | text                                                                                 |                                                                |
  | details  | <ul><li>min: 19 tokens</li><li>mean: 62.6 tokens</li><li>max: 96 tokens</li></ul> | <ul><li>min: 73 tokens</li><li>mean: 168.27 tokens</li><li>max: 228 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.51</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | label                           |
  |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
  | <code>Компания: ООО ТехноСофт  Город: Новосибирск  Зарплата: 159735 руб.  О компании: ООО ТехноСофт занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 2 лет  • знание React  • знание JavaScript  • знание REST API  • знание TypeScript    Обязанности:  • взаимодействие со смежными отделами  • участие в командной разработке  • поддержка существующих решений  </code>       | <code>В направлении «Контент-менеджер» уже работаю достаточно уверенно и без долгого разгона. Комфортно работать с большим количеством материалов, если у них есть понятная система и редакционный ритм. Обычно спокойно отношусь к рутине, если задача и критерии результата понятны. Комфортно беру задачи целиком, если понятен результат и есть нормальная коммуникация со смежниками. 2024 - 2026 \| ООО Медиа Групп \| Контент-менеджер  Поддерживал редакционный календарь, правил страницы и адаптировал материалы под разные площадки и форматы.  Брал на себя заметный кусок процесса и не прятался за формулировками. Редко требовал ручного напоминания, когда сроки и критерии уже были согласованы.</code>                                                                                                                                                                                                                                                                                                                                  | <code>0.6666666666666666</code> |
  | <code>Компания: АО Медиа Платформа  Город: Москва  Зарплата: 148235 руб.  О компании: АО Медиа Платформа занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 2 лет  • знание Чтение чертежей  • знание Проектирование  • знание AutoCAD  • знание Сметы    Обязанности:  • взаимодействие со смежными отделами  • оптимизация процессов  • ведение документации  </code>             | <code>Если коротко, как сильный специалист по направлению «Инженер ПТО» полезен там, где задач много, а понятности мало. Сильнее всего там, где нужно быстро навести порядок в документации и не упустить важные детали по объекту. Плюс люблю, когда из хаоса получается понятный процесс. Нравятся роли, где можно влиять на качество решений, стандарты и темп команды, а не только закрывать тикеты. 2024 - 2026 \| ООО Городской Сервис \| Инженер ПТО (ведущий)  Готовил исполнительную документацию, сверял объемы по объекту и держал в порядке комплект документов для сдачи.  Брал ответственность за результат шире своей зоны. Команда за счет этого работала ровнее и меньше зависела от ручного контроля.  2022 - 2024 \| ООО Северный Вектор \| Инженер ПТО (senior)  Готовил исполнительную документацию, сверял объемы по объекту и держал в порядке комплект документов для сдачи.  Поддерживал процесс в собранном виде даже на длинной и сложной дистанции. Вокруг работы появлялись понятные правила, а не только героическое</code> | <code>1.0</code>                |
  | <code>Компания: ООО Бизнес Партнер  Город: Казань  Зарплата: 52978 руб.  О компании: ООО Бизнес Партнер занимается развитием внутренних сервисов и поддержкой корпоративных проектов. Команда расширяется из-за роста количества задач и новых направлений.    Требования:  • опыт работы от 6 месяцев  • знание Коммуникация  • знание Тикеты  • знание Helpdesk  • знание CRM  • знание Linux    Обязанности:  • оптимизация процессов  • поддержка существующих решений  • участие в командной разработке  </code> | <code>Если коротко, рассматриваю стажерскую или стартовую позицию в «Администратор». Сильнее всего там, где нужно держать контакт с людьми, не терять детали и не создавать суету вокруг простых вопросов. Плюс предпочитаю понятные договоренности и рабочую коммуникацию без лишнего шума. Сейчас важнее всего набрать крепкую базу и научиться работать в команде без лишней суеты. 2025 - 2026 \| ООО Городской Сервис \| Администратор (стажер)  Встречал посетителей, вел запись, работал со звонками и держал фронт процесса в аккуратном состоянии.  Держал темп даже там, где часть вещей приходилось осваивать на месте. при этом не откладывал мелкие правки до бесконечности.</code>                                                                                                                                                                                                                                                                                                                                                          | <code>0.0</code>                |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": null
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `fp16`: True
- `per_device_eval_batch_size`: 32

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 32
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
- `per_device_eval_batch_size`: 32
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
| Epoch  | Step | Training Loss | validation_spearman |
|:------:|:----:|:-------------:|:-------------------:|
| 0.3909 | 500  | 0.6696        | 0.5458              |
| 0.7819 | 1000 | 0.5904        | 0.6186              |
| 1.0    | 1279 | -             | 0.6382              |
| 1.1728 | 1500 | 0.5665        | 0.6514              |
| 1.5637 | 2000 | 0.5500        | 0.6801              |
| 1.9547 | 2500 | 0.5404        | 0.6955              |
| 2.0    | 2558 | -             | 0.6976              |
| 2.3456 | 3000 | 0.5177        | 0.7104              |
| 2.7365 | 3500 | 0.5191        | 0.7225              |
| 3.0    | 3837 | -             | 0.7301              |


### Training Time
- **Training**: 18.7 minutes

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