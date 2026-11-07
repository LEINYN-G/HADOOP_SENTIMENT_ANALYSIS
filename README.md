# End-to-End Scalable Sentiment Analysis Pipeline on Social Media Data

## 📋 Project Overview
This project implements a complete, hybrid sentiment analysis pipeline capable of processing large-scale social media data (Twitter & Reddit datasets from Kaggle consisting of over 1.6 million records). The architecture combines the high-throughput batch-processing capability of **Apache Hadoop MapReduce (HDFS)** via WSL/Ubuntu for data aggregation, with interactive **Machine Learning modeling (TF-IDF, Naive Bayes, Logistic Regression)**, NLP validations (**VADER, TextBlob**), and performance visualizations in **Jupyter Notebook**.

---

## 🛠️ Step-by-Step Task Execution & Architecture

### Task 1: Social Media Data Acquisition
*   **Implementation Location:** `~/sentiment_project/data_acquisition.py`
*   **Execution Framework:** Python / PRAW (Reddit API Simulation Matrix)
*   **Details:** Designed an authenticated live ingestion script outlining token streaming structures from platforms like Reddit. The script explicitly incorporates an automated exponential backoff retry strategy (`time.sleep`) to handle API rate-limit exceptions gracefully, ensuring pipeline stability during continuous collection.

### Task 2: Text Preprocessing and NLP Preparation
*   **Implementation Location:** `~/sentiment_project/mapper.py` & Jupyter Notebook Cell 2
*   **Execution Framework:** Python Regular Expressions (`re`) & NLTK
*   **Details:** Developed distributed text cleaning matrices to filter out structural social media noise at scale. The preprocessing pipeline applies:
    *   Uniform string normalization (lowercase transformation)
    *   Algorithmic removal of hyper-links and Web URLs (`https?://\S+|www\.\S+`)
    *   Stripping of personal user identity anchors (`@mentions`)
    *   Punctuation stripping and NLTK linguistic stopword filtering to isolate core text tokens.

### Task 3: Sentiment Analysis Modeling & Evaluation
*   **Implementation Location:** Jupyter Notebook (Pipeline Comparison Grid)
*   **Execution Framework:** Scikit-Learn Engine
*   **Details:** Evaluated multiple preprocessing variations across distinct classification models to isolate optimal performance. 
*   **Performance Benchmarks:**
    *   *Model Version A (Multinomial Naive Bayes + Basic Preprocessing):* **70.33% Accuracy** | Macro F1-Score: **0.6565**
    *   *Model Version B (Logistic Regression + Advanced Stopword Removal):* **85.82% Accuracy** | Macro F1-Score: **0.8435**
    *   *Insight:* Wiping out high-frequency semantic noise allowed the Logistic Regression classifier to evaluate TF-IDF feature weights with significantly higher precision.

### Task 4: Scalability and Distributed Processing
*   **Implementation Location:** WSL Linux / Ubuntu environment (`/home/nisha/cse/hadoop`)
*   **Execution Framework:** Apache Hadoop 3.3.6 Single-Node Cluster [pseudo Master-Node] (HDFS & MapReduce Streaming)
*   **Details:** Processed millions of lines of unstructured data within HDFS. Resolved system-level WSL port conflicts by remapping conflicting network bindings (`dfs.datanode.address` moved to `9876` and Secondary NameNode UI moved to `9869`). Executed the MapReduce engine natively using the Hadoop Streaming JAR utility to generate global word aggregation counts:
    *   **Negative Records:** 34,645
    *   **Neutral Records:** 53,514
    *   **Positive Records:** 70,440

### Task 5: Insights, Interpretation, and Visualizations
*   **Implementation Location:** Jupyter Notebook (Visual Plots) & hdfs as well (~/sentiment_project/visuals.py)
*   **Execution Framework:** Matplotlib, Seaborn, and WordCloud
*   **Details:** Rendered deep analytical representations including a categorical sentiment bar chart distribution, high-frequency word clouds for positive vs. negative classes, and a performance confusion matrix heatmap.

---

## 📊 Final Sentiment Distribution Matrix
The complete text allocation computed by the distributed engine across the analytics lifecycle settled as follows:

| Sentiment Category | Aggregate Record Volume | Percentage Share |
| :--- | :--- | :--- |
| 🔴 **Negative** | 34,645 | 21.84% |
| 🟡 **Neutral** | 53,514 | 33.74% |
| 🟢 **Positive** | 70,440 | 44.42% |
| 🌎 **Total Processed** | **158,599** | **100.00%** |

---

## ⚖️ Ethical Considerations

*   **Privacy Preservation & Strict Anonymity:** To guard individual user privacy, the mapping runtime aggressively strips out personal metadata tracks and account markers (`@mentions`). This ensures public opinions can be tracked globally without risking the exposure or re-identification of personal user profiles.
*   **Structural Bias Awareness:** Social media datasets inherently suffer from geographic and platform sampling bias (skewing towards younger, highly digital populations). Automated models can struggle with regional idioms, sarcasm, or distinct demographic dialects. Future iterations must cross-validate lexicons across independent control systems to avoid misrepresenting minority linguistic patterns.

---

## Target Learning Outcomes
Upon successful completion of this comprehensive big data pipeline project, a student is expected to have mastered the following capabilities:

1. **Big Data Infrastructure Management:** Ability to set up, configure, and troubleshoot an active Apache Hadoop multi-daemon cluster system inside a Linux/WSL environment (handling DataNode socket crashes, HDFS formatting, and cluster ID conflicts).
2. **Distributed Architecture Programming:** Competence in utilizing Hadoop Streaming utilities to write decoupled, stream-based **Mapper** and **Reducer** logic in Python, handling mass data pipelines without overloading host RAM limits.
3. **Advanced Natural Language Preprocessing:** Deep operational understanding of text token filtering matrices using regular expressions (handling URLs, hashtags, mentions, and language stopwords).
4. **Machine Learning Model Evaluation:** Capacity to design comparative data experiments, cross-evaluating multiple algorithms (Naive Bayes vs. Logistic Regression) and mathematically validating them using exact **Accuracy, Precision, Recall, and F1-Score** parameters.
5. **Data-Driven Visual Storytelling:** Mastery in transforming large numerical tables into accessible graphical insights (Word Clouds, Heatmaps, and Distribution Bar Charts).
6. **Ethical System Design:** Developed awareness of data citizenship responsibilities, including data sanitization for user anonymity and handling algorithmic demographic bias.
