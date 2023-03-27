import pandas as pd
import openai


### 1、data preparation and save the dataset as a jsonl file

#openai tools fine_tunes.prepare_data -f /Users/gaomingqing/dev/ai/openai/demo/cede_finetuned/code.csv

### 3、suggest a few improvements
### cli 执行 openai tools fine_tunes.prepare_data -f code_prepared.jsonl -q
### 会输出模型训练的总结，包括建议及运行命令等

### 4、train
# openai api fine_tunes.create -t "sport2_prepared_train.jsonl" -v "sport2_prepared_valid.jsonl" --compute_classification_metrics --classification_positive_class " baseball" -m ada
#训练完成后， 生成模型，模型名称：ada:ft-personal-2023-03-02-08-21-32


#### 5、训练完毕后，查看模型指标，导出模型结果数据
#openai api fine_tunes.results -i file-4AUqwm25bqJOaOewkm1fmkn7> result.csv

#### 6、using the model
openai.api_key = "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"


ft_model = "text-davinci-003"
res = openai.Completion.create(model=ft_model, prompt="根据我历史的输入vodnode_tar，给出未来电视央视频表快速点击表的建表" + '\n\n###\n\n', max_tokens=200, temperature=0)

print(res['choices'][0]['text'])



