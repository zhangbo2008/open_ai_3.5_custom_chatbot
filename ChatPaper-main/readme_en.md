# ChatPaper

<div style="font-size: 1.5rem;">
  <a href="./README.md">中文</a> |
  <a href="./readme_en.md">English</a>
</div>
</br>

To keep up with the huge ArXiv papers and AI’s fast progress, we humans need to evolve. We download the latest papers on arxiv based on user keywords, and use ChatGPT3.5 API’s powerful summarization to condense them into a fixed format with minimal text and easy readability. 
We provide the most information for everyone to choose which papers to read deeply.

## TODO list:
1. Change all prompts to English.  --completed!
2. Use a more robust method to parse the Method section.
3. If there is a brother who wants to build a website, we can cooperate. --completed!
4. Implement a ChatReview version for everyone to refer to when reviewing (but there may be academic ethics issues?)
5. Output English mode! just set lauguage as "en"!

## Motivation

Facing the massive arXiv papers every day, and AI's rapid evolution, we humans must also evolve together in order not to be eliminated.

As a PhD student in Reinforcement Learning at USTC, I feel anxious. My brain holes can even not keep up with the speed of AI evolution now.

Therefore I developed this **ChatPaper**, trying to use magic to defeat magic.

**ChatPaper is a paper summary tool**: AI summarizes papers in one minute, and users read papers summarized by AI in one minute.

It can automatically download the latest papers from arXiv based on the keywords entered by the user, and then use ChatGPT3.5's powerful API interface summary ability to summarize the paper into a fixed format, with minimal text and lowest reading threshold to provide you with maximum information volume to decide which articles should be read carefully.

You can also provide local PDF document addresses for direct processing.

Generally speaking, you can quickly pass through a small field of latest articles in one night. I have tested it for two days myself.

I wish everyone can evolve with AI in this rapidly changing era!

Although this code is not much, it took me nearly a week to get through the whole process and share it with you today.

Your support is the motivation for my continuous update!

<div style="text-align: center;">
  <img src=https://user-images.githubusercontent.com/28528386/224465754-6f886e48-8626-419f-a154-e5d187fd22f9.jpg width="200" height="250"/>
</div>

<div style="text-align: center;">
  <img src=https://user-images.githubusercontent.com/28528386/224335122-1e87eb7b-a922-4c2f-b2aa-9612f62a6314.jpg width="200" height="250"/>
</div>


## How to use:
Windows, MAC and Ubuntu systems should be fine;

python version is best 3.9, other versions should not have any problems

1. Fill in your openai key in apikey.ini. Note that this code is a pure local project, your key is very safe!

2. The process must ensure global proxy! (Non-Chinese users may not have this problem)

3. Install dependencies:
``` bash
pip install -r requirements.txt
```
4. Run chat_paper.py, for example:

```python
python chat_paper.py --query "chatgpt robot" --filter_keys "chatgpt robot" --max_results 1 --language en
```

5. Parameter introduction:
```
[--pdf_path Whether to directly read local pdf documents? If not set, download directly from arxiv with query] 
[--query The keywords searched on the arxiv website, some abbreviations are demonstrated: all, ti(title), au(author), an example query: all: ChatGPT robot] 
[--key_word The keywords of your interested field, not very important] 
[--filter_keys The keywords you need to search in the abstract text, each word must appear to be your target paper] 
[--max_results The maximum number of articles searched each time, after the above filtering, it is your target number of papers, chat only summarizes filtered papers] 
[--sort arxiv sorting method, default is relevance, can also be time , arxiv.SortCriterion.LastUpdatedDate or arxiv.SortCriterion.Relevance , don't add quotation marks] 
[--save_image Whether to save pictures , if you haven't registered gitee's picture bed , default is false ] 
[--file_format File save format , default is markdown's md format , can also be txt ] 
```

## Tips for using the project:
Quickly brush papers with specific keywords, without illustrations, each article takes a minute, reading time is about a minute.

This project can be used to track the latest papers in a field, or pay attention to papers in other fields, can batch generate summaries, up to 1000 (if you can wait).
Although Chat may have some nonsense elements, but under my standardized questioning framework, its main information is valuable.

The digital parts need everyone to go back to check in the original text!

After finding a good article, you can read this article carefully.

Recommend two other AI-assisted websites for reading papers: https://typeset.io/ and chatpdf.
My tutorial: [Reinforcement Apprentice: Paper Reading Artifact SciSpace(Typeset.io) Evaluation-Evolve with AI](https://zhuanlan.zhihu.com/p/611874187)

The main advantage over these two tools is that ChatPaper can automatically summarize the latest papers in batches, which can greatly reduce the reading threshold, especially for us Chinese.
The disadvantage is also obvious. ChatPaper has no interactive function and cannot ask questions continuously. But I think this is not very important~


## Summary Demo:

![6O4E3VW~X (7I }`ZV`Z`J](https://user-images.githubusercontent.com/28528386/224890637-62be8d42-813c-40ff-8c69-90bb13080e21.png)
