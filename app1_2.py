import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import base64





def app():
    st.title("🌱 Omdena Algeria Chapter 🌱")
    st.write("\n")
    st.write("\n")
    st.markdown("Collaborate, Learn, Build, Grow",)
    st.subheader("Part:2 🌾Building an Intelligent Control System for Greenhouses")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    """### gif from local file"""
    file_ = open("Images/part2.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )
    # st.image(img1)
    st.write("\n")
    st.header("🔍Problem Statement")
    st.markdown("""
        - The management of all equipment under one control system, including heating, venting, and irrigation, is a hard task in terms of systems management and data collection. As a seasonal grower with product cycles of up to two years in duration, patience is necessary. It takes time to collect the data for these systems to work and learn.

        - Greenhouse environments are also challenging for technology implementation due to broad temperature and humidity ranges, which influence both the electronic and mechanical components that contribute to their ongoing development. This can be a frustration for staff trying to complete their weekly plans.

        - AI solutions for greenhouse growers are still in their initial phases of development. The integration of intelligent control systems requires changes to processes, which can be disruptive to production, so flexibility and managing expectations are important to manage the greenhouses effectively.
        """)
    st.write("\n")
    st.header("🎯Goal")
    st.markdown("""
        Build a strong community for sharing knowledge of AI and ML models in agriculture. Decide the best values for managing the levels of temperature, humidity, the use of water, the light and other parameters inside the greenhouse. Notify the growers when there are issues within the crop relating to growth rate, pests, and disease.
        """)
    st.write("\n")
    st.header("📊Directory Structure")
    st.code("""
        ├── Part 2
        │   ├── Subproject1- Indoor Climate Factors
        │     ├── Reports
        │     ├── src
        │       ├── data
        │       ├── documents
        │       ├── references
        │       ├── tasks
        │          ├── Task1- Research
        │          ├── Task2- EDA
        │          ├── Task3- Preprocessing
        │          ├── Task4- Model Building
        │          └── Task5- Deployment
        │       ├── visualizations
        │       └── results

        │   ├── Subproject2- Diseases and Pests Detection
        │     ├── Reports
        │     ├── src
        │       ├── data
        │       ├── documents
        │       ├── references
        │       ├── tasks
        │          ├── Task1- Research
        │          ├── Task2- EDA
        │          ├── Task3- Preprocessing
        │          ├── Task4- Model Building
        │          └── Task5- Deployment
        │       ├── visualizations
        │       └── results

        │   ├── Subproject3- Recommendation Systems
        │     ├── Reports
        │     ├── src
        │       ├── data
        │       ├── documents
        │       ├── references
        │       ├── tasks
        │          ├── Task1- Research
        │          ├── Task2- EDA
        │          ├── Task3- Preprocessing
        │          ├── Task4- Model Building
        │          └── Task5- Deployment
        │       ├── visualizations
        │       └── results
        │
        └── README.md
        """)
    st.write("\n")
    st.header("🌐Website")
    link='Check out this [link](https://github.com/OmdenaAI/Algeria-Chapter-Green/tree/main/Part%202)'
    st.markdown(link,unsafe_allow_html=True)
    st.markdown("© 2022 Omdena")

    