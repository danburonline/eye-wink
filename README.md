# Eye Wink Classifier

![A picture of myself with the IDUN Guardian Earbuds](/docs/imgs/thumbnail.png)

This repository contains the code for the project eye wink classifier, which was the final project for the SIT Academy's [Applied Machine Learning](https://learning.constructor.org/remote/applied-machine-learning) bootcamp. The project involved creating a classifier for detecting eye winks from electroencephalographic (EEG) signals. To collect the necessary data, I used [in-ear EEG earbuds](https://iduntechnologies.com/idun-guardian) from IDUN Technologies. The classifier was trained on a dataset derived from these recordings, and demonstrated its ability to distinguish between eye winks and other EEG signals.

## Workflow

> **Note**
> The following workflow overview is a high-level summary. For more details as well as figures and graphs, please refer to the [presentation](/presentation/presentation.pdf) document inside the presentation directory.

1. **Feasibility:** The initial phase of the project involved conducting a feasibility study to assess the presence of patterns in processed and transformed neural signals. I was pleased to discover discernible patterns, indicating the potential viability of developing a classifier to identify them.

2. **Data Collection:** I used the company's Python SDK to create an experiment script and administered it to ten subjects in a single evening. This streamlined the data collection process and facilitated the rapid generation of a dataset for training and evaluating the classifier. I then cleaned and preprocessed the data for the machine-learning phase.

3. **Preprocessing:** The data collection process generated multiple merged CSV files containing the timestamps of the markers for the features and the raw EEG signal. These CSV files provided the input for the subsequent preprocessing and machine learning phases of the project.

4. **Epoching:** I epoched the data around the three different types of markers and stored the processed and filtered epochs in the repository. This facilitated the generation of a dataset suitable for training and evaluating the classifier.

5. **Model selection:** I used MLflow and [AutoML](https://azure.microsoft.com/en-us/products/machine-learning/automatedml) to train and evaluate a range of machine learning models on the preprocessed data. This approach allowed for efficient and systematic exploration of multiple model architectures and hyperparameter settings, facilitating the identification of the most promising models for further analysis and refinement.

6. **Review model performance:** Although I was satisfied with the results of the automated machine learning process, I encountered a few challenges. For instance, the collected data was somewhat noisy, which made training accurate models difficult. Additionally, there is potential for further improvement, as indicated by the observed limitations in the performance of the models generated by the AutoML process.

## Conclusion

![A graph showing the processed neural signal overlaid to a baseline recording](/docs/imgs/exploration.png)

One of the key insights I have gained from this project is the difficulty of collecting neural signal data in a controlled manner, highlighting the challenges of generating datasets for machine learning applications in the domain of brain-computer interfaces (BCI). This emphasises the importance of carefully designing and executing the data collection process in order to obtain high-quality and relevant data for training and evaluating BCI models.

### Next steps

I plan to generate a larger dataset and devote more time to model selection to avoid relying too heavily on automated methods for this task in the future. This will enable a more thorough exploration of potential model architectures and hyperparameter settings, allowing for the identification of the most promising models for further development and evaluation.

### Disclaimer

Unfortunately, due to strict IP constraints, I am unable to share the details of the AutoML pipeline and preprocessing steps used in this project. These methods are proprietary technology owned by the company, and I am not permitted to disclose them publicly. As a result, they are not included in this repository.
