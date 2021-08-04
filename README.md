# PsychoPyUniformityIllusion

## Description
This is a PsychoPy study that utilizes the Pupil Core eye tracker to measure the effect of depression and anxiety on perception of the uniformity illusion.

## Table of Contents
<ins> HowToRunTheStudy.docx </ins> - This word document contains screenshots and instructions on how to run the study.

<ins> UniformityIllusion.psyexp </ins> - This is the Builder view. This does not have eye tracker integration, so only use it for adding new components to the study. Then, convert to coder view and reinsert the Pupil Core code. Do not run the study from this view.

<ins> UniformityIllusion.py </ins> - This is the Coder view. Run the experiment using this file. You can run it from the terminal, or from the PsychoPy Coder. Make sure to open Pupil Capture, put on and calibrate the eye tracker, and gaze at the monitor before running this code, otherwise it will not work.

<ins> UniformityIllusion_lastrun.py </ins> - This is the coder view that is automatically generated when you run the experiment from the Builder view. Do not run the experiment from this file.

<ins> depression.xlsx </ins> - The depression questionnaire file. Refer to the PsychoPy documentation (https://www.psychopy.org/builder/components/form.html) for how to fill the entries.

<ins> picPaths.xlsx </ins> - The paths to the stimuli images. startImage is always the blank periphery version. midImage is always the illusionary trial, with different periphery and center. endImage is either the illusionary trial or the control trial (which has the same periphery and center).

<ins> Pics </ins> - The stimuli files. If the name starts with web, it is optimized for web use.

<ins> Data </ins> - The data is saved here as .log, .psydat, and .csv. Supposedly, .psydat is the best for data analysis. https://www.psychopy.org/general/dataOutputs.html#excelfile

<ins> pupil_dilation_analysis.ipynb </ins> - Example code for how to get the pupil dilation data around each key press. Note that you'll need Jupyter Notebook, DeepNote, Google Colab, or similar software to open this file.

<ins> requirements.txt </ins> - Additional python dependencies needed. 

## Required Packages And Installation


<ins> PsychoPy </ins> - https://www.psychopy.org/download.html

<ins> Python 3 </ins> (recommend getting Anaconda) - https://www.anaconda.com/products/individual

<ins> Pupil Player, Capture, Service </ins> - https://docs.pupil-labs.com/core/#_1-put-on-pupil-core


In order to get this code running on another computer, do the following steps.

1. Download PsychoPy, Python 3, and Pupil Apps
2. Clone this repository by running the following code in the terminal. Make sure to change your directory to where you want to save it.
   ```
   $git clone https://github.com/jimzhang629/PsychoPyUniformityIllusion.git
   ```
3. Download the required Python dependencies by running the following code in the cloned repository
   ```
   $pip install -r requirements.txt
   ```
   
    


