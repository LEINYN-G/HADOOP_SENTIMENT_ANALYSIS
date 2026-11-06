## Evaluation & Distribution Metrics
The dataset was aggregated via a distributed Hadoop execution pipeline. Below is the final distribution of text profiles discovered:

| Sentiment Category | Record Volume | Percentage Share |
| ------------------ | ------------- | ---------------- |
| **Negative**       | 34,645        | 21.84%           |
| **Neutral**        | 53,514        | 33.74%           |
| **Positive**       | 70,440        | 44.42%           |
| **Total Processed**| **158,599**   | **100.00%**      |

---

## ⚖️ Insights, Interpretation, and Ethical Considerations

### 1. Architectural Insights & Topic Trends
The data reflects a distinct positive skewness within the active user community framework, with positive sentiments accounting for 44.42% of total processed communications. Through distributed parsing matrices, regular expressions managed structural noise (such as handling platform-specific mentions, hyper-links, and slang tokens), transforming loose social text fragments into clean data without running out of standard RAM limits.

### 2. Ethical Reflections: Privacy, Anonymity, and Bias Mitigation
Processing large-scale social media text signatures presents real privacy and demographic fairness risks. To address user privacy and preserve strict anonymity, this pipeline aggressively stripped out personal profile markers (such as user handles via `@mentions`) during the data mapping runtime phase to ensure individuals cannot be reverse-tracked or targeted based on their public sentiments. 

Furthermore, social datasets contain implicit sampling bias, as platform demographics lean heavily toward specific geographic regions and age brackets. Automated algorithms often struggle with localized slang, context shifts, or cultural idioms, which can lead to misclassification. To maintain fairness and reduce systemic algorithm bias, future iterations should cross-validate lexicon mappings across broader multi-platform control datasets to prevent misrepresenting minority linguistic patterns.

### Project Report : HADOOP_SENTIMENT_ANALYSIS
DataSet Name: Twitter Reddit social media dataset (kaggle)
DataSet Size: 1.6 Millions (roughly 200-300 MB)
[ Two ways to perform this Analysis: 
1) Jupyter Notebook  (faster and easier)
2) Hadoop MapReduce(Java/Python) via HDFS is fully supported on Linux Ubuntu
Which Method I followed?
	2)
#### What System I used? (Requirements)
	My Laptop (Ram: 16 GB, 64 bit OS)
	WSL Linux/Ubuntu 20.x.x setup
Pre_set-up: [ ** note: SKIP IF ALREADY DONE **]
Pre-requesites for Hadoop:
	Install Networking Tools  ( $ sudo apt install net-tools )
	Install Gedit ( $ sudo apt gedit )
	Install Open SSH ( $sudo apt-get install openssh-server && openssh-client )
	Install JAVA ($ sudo apt install openjdk-8-jdk -y )
	Install MySQL ( $ sudo apt install mysql-server -y )
	Disable IPV6
	Hadoop version – 3.3.6 (Download the tar file and untar it in a dedicated user)
	Configure the Hadoop files ( ~/hadoop/etc/hadoop/nano (filename))
	Python version (3.11.x)
### What will Approach 2) will do?
	The Mapper: Reads the CSV line by line, cleans the tweet/post text, and uses a lightweight lexicon to calculate a score. It outputs (sentiment_category, 1).
	The Reducer: Collects all the keys and sums them up to output the final count: (positive, 54300), (negative, 32100).
### Why This Approach: To showcase Hadoop/Big Data infrastructure skills on your resume, or if the dataset is too massive to fit into the computer’s RAM.



