# PsychoPyUniformityIllusion

## Description
This is a PsychoPy study that utilizes the Pupil Core eye tracker to measure the effect of depression and anxiety on perception of the uniformity illusion.

## Table of Contents
HowToRunTheStudy.docx - This word document contains screenshots and instructions on how to run the study.

UniformityIllusion.psyexp - This is the Builder view. This does not have eye tracker integration, so only use it for adding new components to the study. Then, convert to coder view and reinsert the Pupil Core code. Do not run the study from this view.

UniformityIllusion.py - This is the Coder view. Run the experiment using this file. You can run it from the terminal, or from the PsychoPy Coder. Make sure to open Pupil Capture before running this code, otherwise it will not work.

UniformityIllusion_lastrun.py - This is the coder view that is automatically generated when you run the experiment from the Builder view. Do not run the experiment from this file.

depression.xlsx - The depression questionnaire file. Refer to the PsychoPy documentation (https://www.psychopy.org/builder/components/form.html) for how to fill the entries.

picPaths.xlsx - The paths to the stimuli images. startImage is always the blank periphery version. midImage is always the illusionary trial, with different periphery and center. endImage is either the illusionary trial or the control trial (which has the same periphery and center).

Pics - The stimuli files. If the name starts with web, it is optimized for web use.

Data - The data is saved here as .log, .psydat, and .csv. Supposedly, .psydat is the best for data analysis. https://www.psychopy.org/general/dataOutputs.html#excelfile
