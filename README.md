
 
<h1> RiceCloud: A Cloud integrated Ensemble learning based Rice leaf Diseases prediction System </h1>

[Abhimanyu Bhowmik](https://scholar.google.com/citations?user=r3bzJ7oAAAAJ&hl=en), [Madhushree Sannigrahi](https://scholar.google.com/citations?user=Mtnm7igAAAAJ&hl=en), [Deepraj Chowdhury](https://scholar.google.com/citations?user=9sZgeV4AAAAJ&hl=en), [Debanjan Das](https://scholar.google.com/citations?hl=en&user=ss7qwk4AAAAJ)

[![paper](https://img.shields.io/badge/IEEE-Paper-brightgreen)](https://doi.org/10.1002/itl2.395) 
[![dataset](https://img.shields.io/badge/Kaggle-Dataset-brightblue))](https://www.kaggle.com/datasets/shayanriyaz/riceleafs) 
[![slides](https://img.shields.io/badge/Presentation-Slides-yellow)](https://drive.google.com/file/d/1xo0QhifZ2juq-dHoke1nMhcgLlhQJKsj/view?usp=sharing) 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://abhimanyubhowmik-ricecloud-appmain-ryht61.streamlitapp.com/)



> **Abstract:** *Rice is one of the primary food items consumed by the humans. Farmers in developing countries like India face a lot of problems while cultivating the rice crop. One of such major problem is of rice leaf disease. A plethora of research has been carried out by the data scientist and machine learning expert to detect the disease of the rice leaf from the images. In the research, researchers had mostly used deep learning techniques to detect the rice leaf disease. In this paper, an ensemble learning architecture has been proposed, where the image is given input to a very famous transfer learning neural network, VGG 16 which is pretrained with ImageNet dataset and the features from the penultimate layer is considered as a input to the Light GBM. The Ensemble learning model is deployed on Heroku with a end to end user interface that can be accessed from mobile. The proposed method has given an accuracy of 96.49 % , where trained with 80 % images of dataset and validated on rest 20\% while classifying 4 types of rice leaf disease.*

<hr />

<h2>Proposed Methods</h2>


<!--
  ======================Global Architecture===========================
                          -->

<h3>1. Globar Architecture</h3>


<br><br>

<div align="center">
<img src = "./Images/Architecture of VGG + LGBM.png" width="100%">
<p>Conceptual view of the proposed architecture </p>
</div>

<br>

<!--
  =========================Data Preprocessing========================= 
                          -->
 

<h3>2. Data Preprocessing</h3>


<div align="center">
<img src = "./Images/preprocessed.png" width="70%">
<p>Preprocessed Image Sample for BrownSpot class </p>
</div>

<br>


<!--
  ============================Model=========================
                          -->

<h3>3. Proposed Model </h3>


<div align="center">
<img src = "./Images/VGG16_bn_lgbm.png" width="100%">
<p>Proposed model Architecture </p>
</div>

<br>




<!--
  ====================================RESULTS===============================
                          -->

<h2>Results </h2>
<h3>1. Classification Report</h3>

<div align="center">
<img src = "./Images/cr.jpeg" width="50%">
<p>Classification report for 75:25 train-validation ratio</p>
</div>


<h3>2. Confusion Matrix</h3>

<div align="center">
<img src = "./Images/confusion_matrics.png" width="50%">
<p>Confusion Matrix: All the classes</p>
</div>
<br><br>

<h3>3. ROC - AUC Curves</h3>

<div align="center">
<table>
  <tr>
    <td width="50%"> <img src = "./Images/ROC.png" width="100%"><br>(a) </td>
    <td width="50%"> <img src = "./Images/roc4.jpeg" width="100%"><br>(b) </td>
  </tr>
</table>
<p>(a), (b) Globar Receiver operating characteristic Curve (left) ROC curves for indevisual classes (right).</p>
</div>
<br><br>

<h3>4. RiceCloud: Application UI</h3>

<div align="center">
<img src = "./Images/UI.png" width="50%">
<p>UI of deployed application using Streamlit</p>
</div>
<br><br>


<hr />

<h2>Cite our work</h2>

    
    Bhowmik, A., Sannigrahi, M., Chowdhury, D., Das (2022). RiceCloud: A Cloud integrated Ensemble learning based Rice leaf Diseases prediction System. Acepted in IEEE 19th India Council International Conference, INDICON 2022.


<hr />

<h2>Contact</h2>
For any queries, please contact: <a href="mailto:bhowmikabhimnayu@gmail.com">bhowmikabhimnayu@gmail.com</a>