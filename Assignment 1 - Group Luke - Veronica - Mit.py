"""
HIT137 SOFTWARE NOW
ASSIGNMENT 1
Topic: Image Processing Models
Submitted By [Mittonu]
GitHub:
https://github.com/HIT137-Group-Veronica-Mit-Luke/Assignment1

Member: Name – ID – GitHub ID
Luke Han: S214459 : sigami79
Veronica Perpetua Thomas: S366004 : V3R0N1CA7
Thi To Nu Dinh : S374680 : Mittonu

Submitted To 
Abhijith Beeravolu

CHARLES DARWIN UNIVERSITY FACULTY OF SCIENCE AND TECHNOLOGY
25 March 2022 

Introduction

In recent years, Python-based image processing models have become essential tools for many fields, such as healthcare, focusing on skin cancer diagnosis and enhancing early detection and diagnosis accuracy, surveillance, facial recognition, and education. Patient outcomes are improved by methods such as preprocessing and feature extraction. However, with all these advancements, ethical considerations must be made in accordance with people's privacy and data security.
 
Methodology

We will review academic papers, research studies, and cases that discuss Python-based image processing models in healthcare, with a focus on skin cancer diagnosis. By analysing these sources, we hope to uncover important insights into how these models are changing healthcare practices and outcomes.

Preliminary Research

Skin cancer, particularly melanoma, is responsible for 75% of skin cancer-related deaths (Vijayalakshmi M M. 2019). However, advancements in image processing have significantly impacted its diagnosis and treatment. Image processing models consist of three main stages: preprocessing, segmentation, and feature extraction. These stages help reduce the time taken to diagnose skin cancer and increase the accuracy of the diagnosis.
One of the key benefits of using image processing models their impact on early detection. In case of stage 1 skin cancer, the survival rate is almost 100%, reaching 99.9%. this highlights the critical role of early detection in improving patient outcomes.
Additionally recent studies by G Bizel (2024) have highlighted the positive impact of increased machine learning methods on patient outcomes, not only in skin cancer but also in other skin diseases. Machine learning algorithms can classify images and gather patient- related data, enabling the detection of skin diseases during analysis.

Discussion

When utilising tools and libraries like Scikt-image, a collection of algorithms for image processing in Python, the accuracy of cancer diagnosis can be significantly enhanced, leading to improved treatment outcomes. However, it is crucial to consider ethical issues, such as patient privacy and data security, throughout the development and implementation of these technologies. Ensuring patient information is protected and used responsibly is paramount to the successful and ethical use of these advancements in healthcare.
Facial recognition is a category of biometric security and can be used to identify people in proctoring systems, such as Face IDs in smartphones. The use of facial recognition technology inherently involves the collection, storage, and analysis of biometric data. It is a very successful application of image processing analysis using mathematical models in processing during data generation, face analysis, and image classification. To do that, the Python programming language was used with the library from OpenCV and the Viola–Jones algorithm for face detection with the Convolutions Neural Networks (CNNs) for deep learning (Nurpeisova et al, 2022). The main advantage of the deep learning method CNNs is that you can use a large amount of data for training to get a reliable idea of the changes that occur in the training data. While facial recognition can offer many security and authentication benefits, facial recognition systems can put consumers at risk, potentially leading to misuse of personal information.
 
Lung cancer is a killer disease, and only early detection by medical history and physical examination, such as The Chest x-ray and computed tomography (CT) scan, prevents the death of mankind. However, an existing image-based CT lung classification technique applies a generative adversarial network (GAN) based classification approach, which gives a poor classification result due to the preprocessed CT image. To explain the experiment, the proposed study utilised the chest CT scan images from Kaggle, the open-source library deployed using Python. In this work (Murthy, S., & Krishna Prasad, P. M., 2023), by using the transformer-aided GAN technique (T-GAN), the classification is done by optimising the parameters of each layer in deep learning networks that have been implemented for classicising the image. Many AI-based systems raise concerns regarding data security and privacy. Because health records are important and vulnerable, hackers often target them during data breaches. Therefore, maintaining the confidentiality of medical records is crucial.

Python-based image processing models have transformed the surveillance industry. The models provide new tools that monitor and analyse with unparalleled precision and efficiency. The programs use complex algorithms that recognise, classify and track objects and individuals in video streams (Zhang et al., 2019). They use this information to address crucial demands for improved security and situational awareness in public and private areas. These models were constructed using the library OpenCV, which uses deep learning approaches to understand and analyse visual data in real time (Choudhary et al., 2022). However, using and applying this technology creates an ethical dilemma that challenges privacy concerns and risks misuse. Hence, as the models and technology continue to advance, they must do so with respect for individual rights and societal values. 
Education is arguably the most important thing for humans, after food, water and family. And in this contemporary world, it is constantly changing and shifting, especially with the development of Python-based image processing models. The models are powered by the SimpleITK and the SciPy library, enabling the automatic analysis of visual resources and the creation of dynamic instructional aids (Ziv Yaniv et al., 2017). These features make learning more dynamic and personalised to students' individual needs, aiding their learning and helping them to achieve their goals. The ethical application of AI in education is essential, especially when protecting students' privacy. Additionally, it must be ensured that this technology only complements human teaching methods rather than replaces them (Marshall et al., 2022). It must also be noted that the deployment requires rigorous thought and contemplation to maintain educational equity and ensure all advancements benefit all students.

Conclusion

In conclusion, Python-based image processing models revolutionise health, education, surveillance, and facial recognition. The models enable advancements in the fields by using libraries such as OpenCV. They improve diagnostic precision and speed. However, ethical issues like privacy and security must drive the implementation of such technology. As these models are integrated into many industries, ethical deployment is critical for maximising benefits while minimising hazards.

 
References

Vijayalakshmi M M. (2019). Melanoma Skin Cancer Detection using Image Processing and Machine Learning. International Journal of Trend in Scientific Research and Development. 3(4). 780-784.
G Bizel, A Einstein, A G Jaunjare, S K Jagannathan. (2024). Machine Learning Study: Identification of skin diseases for various skin types by using image classification. Journal of big data and Artificial intelligence. 2. 43-54. https://doi.org/10.54116/jbdai.v2i1.32.
The Study of Mathematical Models and Algorithms for Face Recognition in Images Using Python in Proctoring System https://www.mdpi.com/2079-3197/10/8/136 by Ardak Nurpeisova and others Computation 2022, 10(8), 136; https://doi.org/10.3390/computation10080136
Submission received: 7 July 2022 / Revised: 26 July 2022 / Accepted: 28 July 2022 / Published: 9 August 2022 (CNNs, OpenCV)
Adversarial transformer network for classification of lung cancer disease from CT scan images,
Biomedical Signal Processing and Control, (https://www.sciencedirect.com/science/article/pii/S1746809423007607) by S.V.S.N. Murthy, P. Murali Krishna Prasad, https://doi.org/10.1016/j.bspc.2023.105327 Received 15 May 2023, Revised 15 July 2023, Accepted 1 August 2023, Available online 12 August 2023, Version of Record 12 August 2023. (the transformer-aided generative adversarial network (T-GAN) , Kaggle)
Nurpeisova, A.; Shaushenova, A.; Mutalova, Z.; Zulpykhar, Z.; Ongarbayeva, M.; Niyazbekova, S.; Semenov, A.; Maisigova, L. (2022). The Study of Mathematical Models and Algorithms for Face Recognition in Images Using Python in Proctoring System. Computation, 10(136), Article e10080136, https://doi.org/10.3390/computation10080136
Murthy, S., & Krishna Prasad, P. M. (2023). Adversarial transformer network for classification of lung cancer disease from CT scan images. Biomedical Signal Processing and Control.
https://doi.org/10.1016/j.bspc.2023.105327
Choudhary, S., Likith, H., Varma, S., Kumar, L., Lekhith and Students (2022). SMART SURVEILLANCE MONITORING SYSTEM USING MACHINE LEARNING AND RASPBERRY PI. [online] International Research Journal of Modernization in Engineering Technology and Science, pp.2582–5208. Available at: https://www.irjmets.com/uploadedfiles/paper/issue_2_february_2022/19011/final/fin_irjmets1644514778.pdf 
Marshall, R., Pardo, A., Smith, D. and Watson, T. (2022). Implementing next generation privacy and ethics research in education technology. British Journal of Educational Technology, [online] 53(4), pp.737–755. doi:https://doi.org/10.1111/bjet.13224.
Zhang, X., Yi, W.-J. and Saniie, J. (2019). Home Surveillance System using Computer Vision and Convolutional Neural Network. [online] Available at: http://ecasp.ece.iit.edu/publications/2012-present/2019-06.pdf  
Ziv Yaniv, Lowekamp, B.C., Johnson, H.J. and Beare, R. (2017). SimpleITK Image-Analysis Notebooks: a Collaborative Environment for Education and Reproducible Research. Journal of Digital Imaging, [online] 31(3), pp.290–303. doi:https://doi.org/10.1007/s10278-017-0037-8.
"""