import pandas as pd
import os
import csv
import numpy as num
import markdown

filepath = os.path.join("..","..","UT-TOR-DATA-PT-09-2019-U-C","Unit 3 - Python","Extra Content","01_Stu_Resume_Analysis","Unsolved","resume.md")
with open(filepath, 'r') as resume:
    htmlmarkdown = markdown.markdown(resume.read())
    resume_words = []
    for i in htmlmarkdown:
        resume_words.append(i)
    print(resume_words)