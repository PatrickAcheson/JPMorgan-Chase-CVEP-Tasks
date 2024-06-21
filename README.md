<h1> JPMorgan Chase & Co Program </h1>

<h2>Task1 - Fraud Analysis</h2>

<p>As the first part of the Cybersecurity Virtual Experience Program by JPMorgan and Chase & Co., I completed an engaging project focused on <strong>fraud analysis</strong>. The following steps encapsulate my approach:</p>

<h2>1. Dataset Acquisition and Analysis</h2>
<p>The first stage involved acquiring a specific dataset (transactions.csv) from <a href="https://www.kaggle.com/ealaxi/paysim1/version/2">Kaggle</a>, which was previously used in a research study on fraud detection. I read the data into a Pandas dataframe and proceeded to return the column names, a specific number of rows, and a list of unique transaction types from the dataset. </p>

<h2>2. Advanced Data Operations</h2>
<p>I then performed a number of advanced operations on the data. This included sampling the dataset, returning a series of the top 10 transaction destinations, and isolating all instances of detected fraud. Furthermore, I engaged with the bonus challenge, returning a dataframe that showed the number of unique destinations each source has interacted with, sorted in descending order.</p>

<h2>3. Data Visualization</h2>
<p>Next, I created various visualizations to better understand the data. I created bar charts to depict transaction types, instances of fraud, and the average transaction amount by type. Additionally, I created a scatter plot to illustrate the relationship between origin account balance and destination account balance for specific transaction types.</p>

![image](https://github.com/PatrickAcheson/JPMorgan-Chase-CVEP-Tasks/assets/90014630/eb7ea4af-39e5-41ff-914b-177542c01aaf)

<h2>4. Custom Data Exploration</h2>
<p>Lastly, I utilized my Pandas skills to unearth unique insights from the dataset. I calculated the mean transaction amount by type and assigned it to a new column in the original dataframe. Then, I visualized this data to illustrate the average transaction amount for each type of transaction.</p>

<p>Through this project, I was able to deepen my understanding of Python, Pandas, and data visualization tools, and their use in analyzing data for cybersecurity purposes within financial services. The task highlighted the critical role of data in ensuring secure financial systems and offered valuable hands-on exposure to real-world cybersecurity issues.</p>
<br>
<h2>Task2 - Spam Detection</h2>
<p>As an integral part of the AI and Machine Learning Virtual Experience Program, I was tasked with a stimulating <strong>Email Spam Detection</strong> project. I was given a rough guide of what I was to impliment, this was great as I have little experience using sklearn. The following illustrates my approach and the key aspects of the project:</p>
<h2>1. Dataset Acquisition and Processing</h2>
<p>The initial stage involved unzipping and reading a dataset (enron1.zip) into a Pandas dataframe. The dataset, containing both 'spam' and 'ham' (non-spam) emails, was then divided into separate dataframes based on the category and concatenated into a single dataframe for further processing.</p>
<h2>2. Data Preprocessing</h2>
<p>The next phase included preprocessing of the email text to remove all non-alphabet characters and convert the remaining text to lowercase. This ensured that the machine learning model treated similar words with different cases as the same, thereby aiding in the accurate prediction of spam emails.</p>

![image](https://github.com/PatrickAcheson/JPMorgan-Chase-CVEP-Tasks/assets/90014630/f79cf754-33d8-46f8-a45f-2ca9b0359d4b)
<h2>3. Model Training and Validation</h2>
<p>After preprocessing, I implemented a Logistic Regression model for the spam detection task. The CountVectorizer was used to convert the email text into numerical vectors suitable for machine learning. The dataset was split into training and testing sets, and the model was trained and validated using these sets. Model performance was evaluated using accuracy, confusion matrix, and a detailed classification report.</p>

![image](https://github.com/PatrickAcheson/JPMorgan-Chase-CVEP-Tasks/assets/90014630/47435cdc-81d5-4206-99f6-42b3fb048e87)
<h2>4. Feature Importance Analysis</h2>
<p>Lastly, the top 10 features (words) most predictive of an email being 'spam' or 'ham' were identified using the coefficients assigned by the Logistic Regression model. This provided insights into the words most frequently used in spam and non-spam emails, offering valuable information about the patterns spam emails typically follow.</p>
<p>Through this project, I enhanced my understanding of Python, Pandas, and machine learning tools, particularly in the context of text classification for spam detection. This task underlined the importance of data and machine learning in building robust email filters and offered valuable practical experience with real-world spam detection problems.</p>

![image](https://github.com/PatrickAcheson/JPMorgan-Chase-CVEP-Tasks/assets/90014630/fa28a7af-403c-4590-af1d-9cae492ef20c)
