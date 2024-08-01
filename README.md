# MindSync: A Second Brain Assistant for people with Neurodegenerative diseases

## Install Instructions
1. Download conda at: [Anaconda Website](https://www.anaconda.com/download)
2. Create an environment: 
```bash 
conda create -n mindsync python=3.9
```
3. Activate environment: 
```bash 
conda activate mindsync
```
4. Use pip to install required libraries: 
```bash 
pip install -r requirements.txt
```
5. Clone the repo
6. Run the code: 
```bash 
python main.py
```

## What problem are you going to solve?
More than 50 million people worldwide are affected by neurodegenerative diseases. Our solution, MindSync, is a Second Brain Assistant designed to transform their daily lives. With a focus on empowering individuals facing cognitive challenges, MindSync enhances cognitive capabilities, streamlines information management, and promotes a renewed sense of independence. Tailored for personalization, it adapts to unique needs, offering intuitive features for organizing tasks, managing schedules, and facilitating seamless information retrieval. MindSync goes beyond being a mere tool; it's a dedicated companion committed to improving the quality of life for those navigating neurodegenerative conditions, providing essential support, and fostering a more empowered and fulfilling daily experience.

## What are you going to build to solve this problem? How is it different from existing solutions? Why is it useful?
MindSync would incorporate advanced cognitive support systems using a combination of cutting edge AI Algorithms like Large Language Models and Natural Language Processing to assist individuals in organizing thoughts, managing tasks, and facilitating information retrieval while creating a user experience personalized to the needs of the user.

MindSync would be built with AI algorithms at its foundation rather than as an additional feature to provide more accurate and adaptive cognitive support, setting it apart from other solutions like Notion and Mem AI which use AI for only certain aspects. Specifically, our solution's ability to learn and adapt to each user's unique needs would distinguish it, providing a level of personalization that goes well beyond what existing solutions offer.

By addressing cognitive challenges and providing practical support, MindSync aims to significantly improve the quality of life for individuals facing neurodegenerative diseases, empowering them to maintain a sense of independence and control over their daily lives.

We envision a transformative solution that combines cutting-edge technology, personalized assistance, and a holistic approach to enhance the lives of individuals dealing with neurodegenerative diseases.

How does your solution work? What are the main features? Please specify how you will use the AMD AI Hardware in your solution.
At its core, our solution uses small foundational large language models to curate the user input into a knowledge base in which the user can reliably store and retrieve their information. This is accompanied by using Speech to Text, Text to Speech and Computer Vision models for improving accessibility to account for a wide range of disabilities. Lastly, Reinforcement Learning is implemented for task and time management.

The main features of MindSync are:
1) Cognitive Support System: MindSync would incorporate advanced cognitive support systems using artificial intelligence to assist individuals in organizing thoughts, managing tasks, and facilitating information retrieval.
2) Adaptive Personalization: The platform would be designed to adapt to the unique needs and preferences of each user, offering personalized assistance and reminders based on individual behavior and cognitive patterns.
3) Task and Time Management: MindSync would include robust task and time management functionalities, helping users plan their daily activities, set priorities.
4) User-Friendly Interface: A simple and intuitive user interface would be a core feature, ensuring accessibility for individuals with varying levels of physical and mental ability and technological proficiency.

The key advantage of using AMD AI Hardware for this solution lies in its ability to concurrently run multiple AI algorithms. This is a core requirement for my solution as it needs to run LLMs, Reinforcement Models and Computer Vision and NLP models at the same time which is possible on the AMD AI Hardware platform. Specifically, we use a quantized Gemma 2 2B running at BF-16 on the AMD ROCm platform.