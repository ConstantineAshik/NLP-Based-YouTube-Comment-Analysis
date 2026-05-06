# Project Report

## **Quantifying the Noise: Sentiment, Topic, and Clustering Analysis of YouTube Comments**

---

## 1. Abstract

YouTube comment sections contain large amounts of user-generated text, including opinions, questions, appreciation, criticism, humor, spam, and topic-related discussions. Because of the large volume and unstructured nature of these comments, manually understanding audience reactions is difficult. This project, titled **“Quantifying the Noise”**, applies Natural Language Processing techniques to analyze YouTube comments from five different videos.

The project collects YouTube comments using the YouTube Data API, cleans and preprocesses the text, extracts important keywords and bigrams, visualizes word patterns, analyzes sentiment, and groups similar comments using clustering algorithms. The main objective is to convert noisy, informal YouTube comments into meaningful insights about audience interest, discussion topics, and emotional responses.

The project uses Python libraries such as Pandas, NLTK, Scikit-learn, TextBlob, VADER, WordCloud, NetworkX, and Transformers. The analysis shows that each video has distinct dominant topics, such as black holes, CRISPR, climate change, space exploration, and decision-making. The project successfully demonstrates how NLP and machine learning can be used to summarize and interpret large-scale online audience reactions.

---

## 2. Introduction

Social media platforms have become one of the largest sources of public opinion. Among these platforms, YouTube is especially important because it combines video content with active audience discussion through comments. Every popular YouTube video may contain thousands of comments, making it difficult for creators, researchers, or analysts to manually understand what the audience is saying.

YouTube comments are often noisy. They may contain informal language, spelling mistakes, emojis, repeated words, jokes, irrelevant comments, and emotional expressions. However, inside this noisy text, there are useful patterns. Viewers often mention what they liked, what confused them, what topic they focused on, and how they emotionally reacted to the video.

This project focuses on extracting meaningful information from such noisy comment data. The title **“Quantifying the Noise”** reflects the main purpose of the project: turning unstructured, noisy YouTube comments into measurable insights using NLP.

The project analyzes five YouTube videos from different topics. The comments are cleaned and processed, then analyzed using keyword extraction, bigram analysis, sentiment analysis, co-occurrence networks, word clouds, and clustering methods.

---

## 3. Objectives of the Project

The main objectives of this project are:

1. To collect YouTube comments from multiple videos using the YouTube Data API.
2. To clean and preprocess raw comment text for NLP analysis.
3. To identify the most frequent and important words from each video’s comments.
4. To extract important two-word phrases using bigram analysis.
5. To visualize audience discussion patterns using word clouds and co-occurrence networks.
6. To analyze the sentiment of comments using TextBlob and VADER.
7. To group similar comments using clustering techniques such as KMeans, DBSCAN, and BERT-based clustering.
8. To compare audience reactions across different video topics.
9. To convert large-scale comment data into interpretable insights.

---

## 4. Dataset Description

The dataset consists of YouTube comments collected from five different videos. Each video was represented by a unique YouTube video ID. The notebook collected comments using the YouTube Data API and saved them as CSV files.

### Raw Comment Collection

| Video ID      | Number of Raw Comments |
| ------------- | ---------------------: |
| `MnYppmstxIs` |                  1,326 |
| `8GQZuzIdeQQ` |                    921 |
| `gypAjPp6eps` |                  6,865 |
| `pEt6-jA2UE4` |                  2,189 |
| `pGsbEd6w7PI` |                  3,191 |

After preprocessing and removing empty cleaned comments, the usable dataset became:

| Video ID / File | Number of Cleaned Comments |
| --------------- | -------------------------: |
| `pGsbEd6w7PI`   |                      2,999 |
| `MnYppmstxIs`   |                      1,268 |
| `8GQZuzIdeQQ`   |                        899 |
| `gypAjPp6eps`   |                      6,786 |
| `pEt6-jA2UE4`   |                      2,136 |

The final dataset contains comments from educational, scientific, and discussion-based videos. The topics include black holes, CRISPR, climate change, space-related theories, and decision-making.

---

## 5. Tools and Technologies Used

The project was implemented using Python in a Jupyter Notebook environment.

### Main Libraries Used

| Library        | Purpose                                             |
| -------------- | --------------------------------------------------- |
| `pandas`       | Loading, storing, and manipulating comment datasets |
| `numpy`        | Numerical operations                                |
| `nltk`         | Stopword removal, tokenization, and lemmatization   |
| `re`           | Regular expression-based text cleaning              |
| `scikit-learn` | TF-IDF, CountVectorizer, KMeans, DBSCAN             |
| `TextBlob`     | Sentiment polarity analysis                         |
| `VADER`        | Rule-based sentiment analysis                       |
| `WordCloud`    | Word cloud visualization                            |
| `NetworkX`     | Word co-occurrence network visualization            |
| `matplotlib`   | Plotting charts and graphs                          |
| `Transformers` | BERT-based embedding and sentiment pipeline         |
| `torch`        | Running transformer models                          |
| `pickle`       | Saving processed data and analysis results          |

---

## 6. Methodology

The project follows a complete NLP pipeline. The main steps are:

1. Data collection
2. Text preprocessing
3. Keyword extraction
4. Bigram extraction
5. Visualization
6. Sentiment analysis
7. Clustering
8. Result interpretation

---

## 7. Data Collection

The first stage of the project was collecting comments from YouTube. The notebook uses the YouTube Data API to fetch comments from selected video IDs. Each video’s comments were saved into separate CSV files.

The comments were stored with the original raw text. This raw text included uppercase and lowercase letters, punctuation, numbers, links, emojis, and informal expressions. Since raw comments are not suitable for direct NLP analysis, preprocessing was required.

One important issue in the notebook is that the YouTube API key was written directly inside the code. This is not safe because API keys should not be exposed in project files. A better practice is to store the API key in an environment variable.

Example safer approach:

```python
import os

api_key = os.getenv("YOUTUBE_API_KEY")
```

---

## 8. Text Preprocessing

Text preprocessing was one of the most important parts of the project. YouTube comments are usually noisy, so the text needed to be cleaned before analysis.

The preprocessing steps included:

### 8.1 Lowercasing

All text was converted into lowercase so that words such as “Climate”, “climate”, and “CLIMATE” would be treated as the same word.

Example:

```text
Climate Change is Real
```

becomes:

```text
climate change is real
```

### 8.2 Removing URLs

Links were removed because URLs do not usually help with topic or sentiment analysis.

### 8.3 Removing Punctuation and Numbers

Punctuation marks and numbers were removed to simplify the text.

Example:

```text
This video is amazing!!!
```

becomes:

```text
this video is amazing
```

### 8.4 Stopword Removal

Common English words such as “the”, “is”, “and”, “to”, and “of” were removed because they appear frequently but usually do not carry strong topic meaning.

### 8.5 Lemmatization

Words were reduced to their base form using lemmatization.

Example:

```text
running, runs, ran
```

can be reduced toward:

```text
run
```

This helps group related word forms together.

---

## 9. Keyword Extraction

Keyword extraction was used to identify the most important words in the comment sections of each video. The project used both frequency-based analysis and TF-IDF-based analysis.

### 9.1 Frequency-Based Keyword Analysis

The notebook used `CountVectorizer` to count the most common unigrams and bigrams.

A unigram is a single word, such as:

```text
climate
```

A bigram is a two-word phrase, such as:

```text
climate change
```

### 9.2 TF-IDF Keyword Analysis

TF-IDF stands for **Term Frequency-Inverse Document Frequency**. It gives higher importance to words that are frequent in one document but not too common across all documents.

This helps identify topic-specific words. For example, the word “video” may appear in many comments, but words like “crispr”, “black hole”, or “climate change” are more topic-specific.

---

## 10. Results: Top Keywords

### 10.1 Video: `8GQZuzIdeQQ`

This video appears to be related to **choices, decisions, life, and TED-style discussion**.

Top TF-IDF keywords:

| Keyword  | TF-IDF Score |
| -------- | -----------: |
| choice   |       44.780 |
| thank    |       31.347 |
| hard     |       29.579 |
| make     |       28.454 |
| talk     |       25.736 |
| video    |       19.383 |
| decision |       18.839 |
| life     |       16.168 |
| good     |       14.600 |
| great    |       13.773 |

The dominant audience discussion focuses on **hard choices**, **decision-making**, and appreciation for the talk.

---

### 10.2 Video: `pGsbEd6w7PI`

This video appears to be related to **black holes, Brian Cox, space, time, and the universe**.

Top TF-IDF keywords:

| Keyword  | TF-IDF Score |
| -------- | -----------: |
| hole     |      143.750 |
| black    |      139.033 |
| brian    |       77.529 |
| cox      |       75.066 |
| time     |       73.680 |
| universe |       66.739 |
| space    |       48.640 |
| matter   |       33.578 |

The comments strongly focus on **black holes**, **space-time**, **matter**, and **Brian Cox**.

---

### 10.3 Video: `pEt6-jA2UE4`

This video appears to be related to **climate change and global warming**.

Top TF-IDF keywords:

| Keyword | TF-IDF Score |
| ------- | -----------: |
| climate |       76.442 |
| change  |       69.164 |
| global  |       40.502 |
| people  |       39.085 |
| earth   |       37.370 |
| warming |       37.197 |
| year    |       36.289 |
| stop    |       30.043 |
| world   |       30.038 |
| human   |       29.992 |

The discussion mainly focuses on **climate change**, **global warming**, **human responsibility**, and the future of the planet.

---

### 10.4 Video: `MnYppmstxIs`

This video appears to be related to **CRISPR, DNA, and educational explanation**.

Top TF-IDF keywords:

| Keyword     | TF-IDF Score |
| ----------- | -----------: |
| thank       |       96.733 |
| video       |       68.673 |
| helpful     |       66.600 |
| thanks      |       52.183 |
| great       |       44.994 |
| explanation |       38.885 |
| crispr      |       32.096 |
| dna         |       22.578 |
| understand  |       21.034 |
| explained   |       17.817 |

The audience reaction is strongly positive. Many comments express gratitude and mention that the video was helpful and easy to understand.

---

### 10.5 Video: `gypAjPp6eps`

This video appears to be related to **stars, planets, aliens, space, and Dyson sphere discussions**.

Top TF-IDF keywords:

| Keyword   | TF-IDF Score |
| --------- | -----------: |
| star      |      270.207 |
| planet    |      195.593 |
| alien     |      194.070 |
| light     |      113.640 |
| earth     |       97.840 |
| data      |       75.786 |
| space     |       75.065 |
| universe  |       71.711 |
| scientist |       67.375 |
| sphere    |       67.191 |

The comments are mainly centered around **stars**, **aliens**, **planets**, and possible space-related explanations.

---

## 11. Results: Top Bigrams

Bigram analysis gives more meaningful phrases than single-word analysis because it captures word combinations.

### 11.1 `8GQZuzIdeQQ`

Top bigrams:

| Bigram      | TF-IDF Score |
| ----------- | -----------: |
| hard choice |       19.399 |
| ted talk    |        8.204 |
| make hard   |        7.708 |
| make choice |        5.773 |
| ruth chang  |        4.424 |

This confirms that the video discussion is strongly related to **hard choices** and decision-making.

---

### 11.2 `pGsbEd6w7PI`

Top bigrams:

| Bigram            | TF-IDF Score |
| ----------------- | -----------: |
| black hole        |      104.612 |
| brian cox         |       45.525 |
| big bang          |       21.137 |
| space time        |       15.192 |
| hawking radiation |       11.177 |
| event horizon     |       10.767 |
| speed light       |        8.030 |

These phrases clearly show that the video is about black holes and physics.

---

### 11.3 `pEt6-jA2UE4`

Top bigrams:

| Bigram         | TF-IDF Score |
| -------------- | -----------: |
| climate change |       47.205 |
| global warming |       25.906 |
| ice age        |       10.317 |
| fossil fuel    |        7.149 |
| climate crisis |        3.891 |
| greenhouse gas |        3.758 |

The comments strongly focus on environmental issues and climate science.

---

### 11.4 `MnYppmstxIs`

Top bigrams:

| Bigram            | TF-IDF Score |
| ----------------- | -----------: |
| helpful thank     |       21.786 |
| great video       |       18.297 |
| great explanation |        8.683 |
| really helpful    |        7.962 |
| best explanation  |        7.285 |

This video has a highly positive and appreciation-focused comment section.

---

### 11.5 `gypAjPp6eps`

Top bigrams:

| Bigram          | TF-IDF Score |
| --------------- | -----------: |
| black hole      |       49.440 |
| dyson sphere    |       47.601 |
| mysterious star |       23.953 |
| death star      |       21.042 |
| orbiting star   |       17.712 |
| light year      |       17.279 |

This confirms the topic is related to space, stars, and theoretical astronomical explanations.

---

## 12. Word Cloud Visualization

Word clouds were generated for each video. A word cloud visually represents the most frequent words in the comments. Larger words appear more frequently.

The word clouds helped identify the dominant discussion themes quickly. For example:

* The black hole video showed large words such as **black**, **hole**, **universe**, **time**, and **space**.
* The CRISPR video showed words such as **thank**, **helpful**, **video**, **crispr**, and **dna**.
* The climate change video showed words such as **climate**, **change**, **global**, **warming**, **earth**, and **human**.
* The space video showed words such as **star**, **planet**, **alien**, and **sphere**.
* The choice-related video showed words such as **choice**, **hard**, **decision**, and **life**.

Word clouds are useful for presentation because they give a quick visual summary of audience discussions.

---

## 13. Word Co-occurrence Network

The project also created word co-occurrence networks using NetworkX. In this method, words are represented as nodes, and connections are drawn between words that appear together in the same comments.

This helps identify relationships between words. For example:

* In the black hole video, words such as **black**, **hole**, **space**, **time**, and **universe** are likely connected.
* In the climate video, words such as **climate**, **change**, **global**, **warming**, and **human** are connected.
* In the CRISPR video, words such as **crispr**, **dna**, **explanation**, and **helpful** are connected.

This method gives a deeper view of how viewers combine ideas in their comments.

---

## 14. Sentiment Analysis

Sentiment analysis was performed to understand the emotional tone of the comments. The project used two sentiment analysis methods:

1. **TextBlob**
2. **VADER**

### 14.1 TextBlob

TextBlob calculates polarity scores. The polarity score usually ranges from -1 to +1.

* Positive score means positive sentiment.
* Negative score means negative sentiment.
* Around zero means neutral sentiment.

### 14.2 VADER

VADER is especially useful for social media text because it handles informal language, capitalization, and intensity expressions better than many simple sentiment tools.

VADER gives a compound score:

* Positive compound score means positive sentiment.
* Negative compound score means negative sentiment.
* Around zero means neutral sentiment.

### 14.3 Sentiment Observation

Based on the keywords and bigrams, the CRISPR video seems to have highly positive comments because many users used words such as:

* thank
* helpful
* great
* amazing
* best
* understand

The climate change video may contain more debate or concern because the keywords include:

* climate
* change
* global
* warming
* stop
* human
* planet

The black hole and space-related videos appear to contain curiosity-based discussion, with users focusing on scientific ideas, theories, and questions.

---

## 15. Clustering Analysis

Clustering was used to group similar comments together. The project used three clustering approaches:

1. KMeans clustering with TF-IDF vectors
2. DBSCAN clustering with cosine distance
3. KMeans clustering with BERT embeddings

---

## 16. KMeans Clustering with TF-IDF

KMeans clustering divides comments into a fixed number of clusters. In the notebook, 3 clusters were used for each video.

### TF-IDF KMeans Cluster Distribution

| Video ID      | Cluster 0 | Cluster 1 | Cluster 2 |
| ------------- | --------: | --------: | --------: |
| `8GQZuzIdeQQ` |       668 |        67 |       164 |
| `pGsbEd6w7PI` |     1,999 |       751 |       249 |
| `pEt6-jA2UE4` |       156 |       386 |     1,594 |
| `MnYppmstxIs` |       945 |       113 |       210 |
| `gypAjPp6eps` |     1,575 |     4,547 |       664 |

The cluster distributions show that some videos have one large dominant cluster. This means many comments may be similar or general in nature. Smaller clusters may represent more specific discussion themes.

For example:

* In the CRISPR video, one cluster may contain appreciation comments.
* In the climate change video, one cluster may contain comments about climate science, while others may contain opinions or debate.
* In the black hole video, clusters may separate general praise, physics discussion, and specific questions.

---

## 17. BERT-Based Clustering

The project also used BERT embeddings. Unlike TF-IDF, which mainly focuses on word frequency, BERT embeddings capture deeper semantic meaning.

The notebook used `bert-base-uncased` to convert comments into numerical embeddings using mean pooling. Then KMeans was applied to the embeddings.

### BERT KMeans Cluster Distribution

| Video ID      | Cluster 0 | Cluster 1 | Cluster 2 |
| ------------- | --------: | --------: | --------: |
| `8GQZuzIdeQQ` |       350 |       370 |       179 |
| `pGsbEd6w7PI` |     1,402 |       389 |     1,189 |
| `pEt6-jA2UE4` |       339 |       689 |     1,109 |
| `MnYppmstxIs` |       309 |       414 |       545 |
| `gypAjPp6eps` |     3,387 |     1,799 |     1,600 |

The BERT-based clustering appears more balanced than the TF-IDF-based clustering. This suggests that semantic embeddings may better capture the meaning of comments rather than only word frequency.

---

## 18. DBSCAN Clustering

DBSCAN was also applied using cosine distance. However, the parameters used in the notebook were not ideal:

```python
DBSCAN(eps=0.5, min_samples=1, metric='cosine')
```

The problem is that `min_samples=1` allows almost every point to become its own cluster. As a result, DBSCAN produced too many small clusters, making the result difficult to interpret.

A better approach would be:

```python
DBSCAN(eps=0.7, min_samples=5, metric='cosine')
```

However, the value of `eps` should be tuned experimentally.

---

## 19. Interpretation of Results

The results show that the project successfully extracted meaningful patterns from noisy YouTube comments.

### 19.1 Topic Separation

Each video had clearly different keywords and bigrams. This means the NLP pipeline successfully captured the main topic of each video.

Examples:

| Video Topic     | Strong Keywords / Bigrams                        |
| --------------- | ------------------------------------------------ |
| Black holes     | black hole, brian cox, space time, event horizon |
| CRISPR          | crispr, dna, helpful, great explanation          |
| Climate change  | climate change, global warming, fossil fuel      |
| Space mystery   | dyson sphere, mysterious star, alien, planet     |
| Decision-making | hard choice, ted talk, decision, life            |

### 19.2 Audience Reaction

The CRISPR video appears to have the most clearly positive audience reaction. Many comments expressed appreciation and learning.

The climate change video likely contains more serious and concerned discussion because of terms related to global warming, humans, and the planet.

The space-related videos contain curiosity-driven discussion, speculation, and scientific terms.

### 19.3 Usefulness of NLP

The project demonstrates that NLP can help summarize thousands of comments quickly. Instead of reading every comment manually, keyword extraction, sentiment analysis, and clustering can reveal major discussion themes automatically.

---

## 20. Strengths of the Project

This project has several strong points:

1. **Real-world data**
   The project uses actual YouTube comments instead of a small manually created dataset.

2. **Multiple NLP techniques**
   It includes preprocessing, keyword extraction, bigram analysis, sentiment analysis, clustering, word clouds, and networks.

3. **Multiple videos analyzed**
   Since five videos were analyzed, the project can compare audience reactions across different topics.

4. **Visual analysis included**
   Word clouds, sentiment plots, bar charts, and co-occurrence networks make the results easier to understand.

5. **Machine learning and deep learning included**
   The project uses both traditional ML methods like TF-IDF and KMeans, and transformer-based embeddings using BERT.

6. **Good project scope**
   The project is suitable for an academic NLP/data science course because it covers data collection, preprocessing, analysis, visualization, and interpretation.

---

## 21. Limitations of the Project

Although the project is strong, there are some limitations.

### 21.1 Exposed API Key

The notebook contains a visible YouTube API key. This is a security issue. The key should be removed and replaced with an environment variable.

### 21.2 Inconsistent File Paths

Some files were saved inside a folder, but later the notebook attempted to load them from the root directory. This can cause file-not-found errors.

Example issue:

```python
pd.read_csv("pGsbEd6w7PI_comments_cleaned.csv")
```

Better:

```python
pd.read_csv("youtube_comments_cleaned/pGsbEd6w7PI_comments_cleaned.csv")
```

### 21.3 Repeated Preprocessing Functions

The notebook has more than one preprocessing function. This may create inconsistency. A single preprocessing function should be used throughout the project.

### 21.4 BERT Sentiment Model Issue

The notebook attempts to use:

```python
pipeline("sentiment-analysis", model="bert-base-uncased")
```

This is not ideal because `bert-base-uncased` is not fine-tuned for sentiment classification.

A better model would be:

```python
distilbert-base-uncased-finetuned-sst-2-english
```

### 21.5 Clustering Needs Evaluation

The number of clusters was selected manually. The notebook uses 3 clusters, but it does not justify why 3 is the best choice.

Better evaluation methods:

* Elbow Method
* Silhouette Score
* Davies-Bouldin Score

### 21.6 DBSCAN Parameter Problem

DBSCAN used `min_samples=1`, which caused too many small clusters. This reduced the usefulness of the DBSCAN output.

---

## 22. Recommendations for Improvement

To improve the project, the following changes are recommended:

1. Remove the API key from the notebook.
2. Use environment variables for API credentials.
3. Organize the notebook into clear sections with markdown explanations.
4. Use one consistent preprocessing function.
5. Fix all file path inconsistencies.
6. Add sentiment summary tables showing positive, negative, and neutral percentages.
7. Use a proper transformer sentiment model.
8. Tune clustering parameters.
9. Add cluster interpretation by showing top words per cluster.
10. Add evaluation metrics such as Silhouette Score.
11. Compare TextBlob and VADER results in a table.
12. Add a final dashboard-style summary for each video.

---

## 23. Suggested Improved Workflow

A cleaner final workflow for the project would be:

1. Import libraries
2. Set API key securely
3. Collect YouTube comments
4. Save raw comments
5. Clean and preprocess comments
6. Save cleaned comments
7. Perform unigram and bigram analysis
8. Perform TF-IDF keyword extraction
9. Generate word clouds
10. Generate co-occurrence networks
11. Perform sentiment analysis
12. Summarize sentiment percentages
13. Perform clustering
14. Evaluate clustering quality
15. Interpret results
16. Save final outputs

---

## 24. Ethical and Security Considerations

Since this project uses public YouTube comments, there are some ethical points to consider.

First, user privacy should be respected. The project should avoid publishing usernames or personally identifiable information. The analysis should focus on aggregated patterns, not individual users.

Second, API keys should be protected. Exposing API keys can cause unauthorized use, quota abuse, and security problems.

Third, sentiment analysis should not be treated as perfectly accurate. Online comments often include sarcasm, humor, slang, and mixed emotions, which can be difficult for automated models to understand.

---

## 25. Conclusion

The project **“Quantifying the Noise: Sentiment, Topic, and Clustering Analysis of YouTube Comments”** successfully demonstrates how Natural Language Processing can be used to analyze large volumes of YouTube comments. The project collected comments from five videos, cleaned the text, extracted important keywords and bigrams, visualized word patterns, analyzed sentiment, and grouped similar comments using clustering algorithms.

The results show that each video has a clear discussion theme. The black hole video produced keywords related to physics and the universe. The CRISPR video received many positive and appreciative comments. The climate change video focused on global warming, humans, and environmental concerns. The space mystery video generated discussion about stars, aliens, and Dyson spheres. The decision-making video focused on choices, life, and TED-style discussion.

Overall, the project turns noisy online comments into structured insights. It is a strong NLP project with real-world data and multiple analysis techniques. With some improvements in notebook organization, security, clustering evaluation, and sentiment modeling, it can become a polished and high-quality academic project.

---

## 26. Short Final Summary

This project analyzes YouTube comments using NLP to identify major topics, audience sentiment, and comment clusters. It uses real YouTube data, cleans the comments, extracts keywords and bigrams, visualizes word patterns, performs sentiment analysis, and applies clustering using TF-IDF and BERT embeddings. The project shows how noisy social media comments can be transformed into meaningful audience insights.
