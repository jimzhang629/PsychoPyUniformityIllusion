#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on July 29, 2021, at 09:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import math
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'UniformityIllusion'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\hesselmann\\Desktop\\PsychoPyUniformityIllusion\\UniformityIllusionPsychoPy\\UniformityIllusion.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to our Study!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Questionnaire"
QuestionnaireClock = core.Clock()
win.allowStencil = True
DepressionQuestionnaire = visual.Form(win=win, name='DepressionQuestionnaire',
    items='depression.xlsx',
    textHeight=0.03,
    randomize=False,
    size=(3.5, 1),
    pos=(0, 0),
    style='dark',
    itemPadding=0.1,)
button = visual.ButtonStim(win, 
   text='Submit', font='Arvo',
   pos=(0, -0.5),
   letterHeight=0.05,
   size=None, borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='bottom-center',
   name='button')
button.buttonClock = core.Clock()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructionsText = visual.TextStim(win=win, name='instructionsText',
    text='This task involves an optical illusion in which the central visual field is different from the peripheral visual field. However, when one fixates on the center, the central visual field may be extended to the periphery and one will experience a uniform visual field. \n\nEach trial will begin with a central red cross displayed on a white background. Please fixate your gaze on this red cross. During each trial, please look continuously at the red cross in the center of the screen. Do not look away from the red cross at any point during each trial. You will be given the ability to indicate if you looked away from the red cross after each trial.\n\nPress the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nextScreen = keyboard.Keyboard()

# Initialize components for Routine "Practice_Trials"
Practice_TrialsClock = core.Clock()
hasPeriphery = visual.ImageStim(
    win=win,
    name='hasPeriphery', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
noPeriphery = visual.ImageStim(
    win=win,
    name='noPeriphery', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
final = visual.ImageStim(
    win=win,
    name='final', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
blank_screen = visual.Rect(
    win=win, name='blank_screen',
    width=(2,2)[0], height=(2,2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
WelcomeText = visual.TextStim(win=win, name='WelcomeText',
    text='Welcome to our Study!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Test_Trials"
Test_TrialsClock = core.Clock()
hasPeriphery_2 = visual.ImageStim(
    win=win,
    name='hasPeriphery_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()
noPeriphery_2 = visual.ImageStim(
    win=win,
    name='noPeriphery_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Thanks_"
Thanks_Clock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [WelcomeText]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.tStart = t  # local t and not account for scr refresh
        WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    if WelcomeText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > WelcomeText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            WelcomeText.tStop = t  # not accounting for scr refresh
            WelcomeText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(WelcomeText, 'tStopRefresh')  # time at next scr refresh
            WelcomeText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)

# ------Prepare to start Routine "Questionnaire"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
QuestionnaireComponents = [DepressionQuestionnaire, button]
for thisComponent in QuestionnaireComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionnaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Questionnaire"-------
while continueRoutine:
    # get current time
    t = QuestionnaireClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionnaireClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *DepressionQuestionnaire* updates
    if DepressionQuestionnaire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        DepressionQuestionnaire.frameNStart = frameN  # exact frame index
        DepressionQuestionnaire.tStart = t  # local t and not account for scr refresh
        DepressionQuestionnaire.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(DepressionQuestionnaire, 'tStartRefresh')  # time at next scr refresh
        DepressionQuestionnaire.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionnaireComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Questionnaire"-------
for thisComponent in QuestionnaireComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
DepressionQuestionnaire.addDataToExp(thisExp, 'rows')
DepressionQuestionnaire.autodraw = False
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
# the Routine "Questionnaire" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
nextScreen.keys = []
nextScreen.rt = []
_nextScreen_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructionsText, nextScreen]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionsText* updates
    if instructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionsText.frameNStart = frameN  # exact frame index
        instructionsText.tStart = t  # local t and not account for scr refresh
        instructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionsText, 'tStartRefresh')  # time at next scr refresh
        instructionsText.setAutoDraw(True)
    
    # *nextScreen* updates
    waitOnFlip = False
    if nextScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nextScreen.frameNStart = frameN  # exact frame index
        nextScreen.tStart = t  # local t and not account for scr refresh
        nextScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextScreen, 'tStartRefresh')  # time at next scr refresh
        nextScreen.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(nextScreen.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(nextScreen.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if nextScreen.status == STARTED and not waitOnFlip:
        theseKeys = nextScreen.getKeys(keyList=['space'], waitRelease=False)
        _nextScreen_allKeys.extend(theseKeys)
        if len(_nextScreen_allKeys):
            nextScreen.keys = _nextScreen_allKeys[-1].name  # just the last key pressed
            nextScreen.rt = _nextScreen_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionsText.started', instructionsText.tStartRefresh)
thisExp.addData('instructionsText.stopped', instructionsText.tStopRefresh)
# check responses
if nextScreen.keys in ['', [], None]:  # No response was made
    nextScreen.keys = None
thisExp.addData('nextScreen.keys',nextScreen.keys)
if nextScreen.keys != None:  # we had a response
    thisExp.addData('nextScreen.rt', nextScreen.rt)
thisExp.addData('nextScreen.started', nextScreen.tStartRefresh)
thisExp.addData('nextScreen.stopped', nextScreen.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracticeTrialsLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('picPaths.xlsx', selection='0:6'),
    seed=None, name='PracticeTrialsLoop')
thisExp.addLoop(PracticeTrialsLoop)  # add the loop to the experiment
thisPracticeTrialsLoop = PracticeTrialsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrialsLoop.rgb)
if thisPracticeTrialsLoop != None:
    for paramName in thisPracticeTrialsLoop:
        exec('{} = thisPracticeTrialsLoop[paramName]'.format(paramName))

for thisPracticeTrialsLoop in PracticeTrialsLoop:
    currentLoop = PracticeTrialsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrialsLoop.rgb)
    if thisPracticeTrialsLoop != None:
        for paramName in thisPracticeTrialsLoop:
            exec('{} = thisPracticeTrialsLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practice_Trials"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimulusInterval = randint(low = 2, high = 4) # choose a value
    thisExp.addData('stimulusInterval', stimulusInterval) # record it in the data file
    hasPeriphery.setImage(midImage)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    noPeriphery.setImage(startImage)
    final.setImage(endImage)
    blank_screen.setFillColor('black')
    blank_screen.setLineColor(win.color)
    # keep track of which components have finished
    Practice_TrialsComponents = [hasPeriphery, key_resp, noPeriphery, final, blank_screen, text]
    for thisComponent in Practice_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice_TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice_Trials"-------
    while continueRoutine:
        # get current time
        t = Practice_TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice_TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        

        
        # *hasPeriphery* updates
        if hasPeriphery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hasPeriphery.frameNStart = frameN  # exact frame index
            hasPeriphery.tStart = t  # local t and not account for scr refresh
            hasPeriphery.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hasPeriphery, 'tStartRefresh')  # time at next scr refresh
            hasPeriphery.setAutoDraw(True)
        if hasPeriphery.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hasPeriphery.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                hasPeriphery.tStop = t  # not accounting for scr refresh
                hasPeriphery.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hasPeriphery, 'tStopRefresh')  # time at next scr refresh
                hasPeriphery.setAutoDraw(False)
        if hasPeriphery.status == STARTED:  # only update if drawing
            hasPeriphery.setOpacity(frameN/(10 * stimulusInterval))
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noPeriphery* updates
        if noPeriphery.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noPeriphery.frameNStart = frameN  # exact frame index
            noPeriphery.tStart = t  # local t and not account for scr refresh
            noPeriphery.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noPeriphery, 'tStartRefresh')  # time at next scr refresh
            noPeriphery.setAutoDraw(True)
        if noPeriphery.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noPeriphery.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                noPeriphery.tStop = t  # not accounting for scr refresh
                noPeriphery.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noPeriphery, 'tStopRefresh')  # time at next scr refresh
                noPeriphery.setAutoDraw(False)
        if noPeriphery.status == STARTED:  # only update if drawing
            noPeriphery.setOpacity(1-frameN/(10 * stimulusInterval))
        
        # *final* updates
        if final.status == NOT_STARTED and frameN >= 10 * stimulusInterval:
            # keep track of start time/frame for later
            final.frameNStart = frameN  # exact frame index
            final.tStart = t  # local t and not account for scr refresh
            final.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(final, 'tStartRefresh')  # time at next scr refresh
            final.setAutoDraw(True)
        if final.status == STARTED:
            final.setOpacity((math.floor(frameN/7)) / 10)
        if final.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > final.tStartRefresh + 12.0-frameTolerance:
                # keep track of stop time/frame for later
                final.tStop = t  # not accounting for scr refresh
                final.frameNStop = frameN  # exact frame index
                win.timeOnFlip(final, 'tStopRefresh')  # time at next scr refresh
                final.setAutoDraw(False)
        print(frameN % 7)
        # *blank_screen* updates
        if blank_screen.status == NOT_STARTED and frameN >= 10 * stimulusInterval and frameN % 7 == 0 and t < 10.0:
            # keep track of start time/frame for later
            blank_screen.frameNStart = frameN  # exact frame index
            blank_screen.tStart = t  # local t and not account for scr refresh
            blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_screen, 'tStartRefresh')  # time at next scr refresh
            blank_screen.setAutoDraw(True)
        if blank_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_screen.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                blank_screen.tStop = t  # not accounting for scr refresh
                blank_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_screen, 'tStopRefresh')  # time at next scr refresh
                blank_screen.setAutoDraw(False)
                blank_screen.status = NOT_STARTED
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice_Trials"-------
    for thisComponent in Practice_TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeTrialsLoop.addData('hasPeriphery.started', hasPeriphery.tStartRefresh)
    PracticeTrialsLoop.addData('hasPeriphery.stopped', hasPeriphery.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    PracticeTrialsLoop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        PracticeTrialsLoop.addData('key_resp.rt', key_resp.rt)
    PracticeTrialsLoop.addData('key_resp.started', key_resp.tStartRefresh)
    PracticeTrialsLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
    PracticeTrialsLoop.addData('noPeriphery.started', noPeriphery.tStartRefresh)
    PracticeTrialsLoop.addData('noPeriphery.stopped', noPeriphery.tStopRefresh)
    PracticeTrialsLoop.addData('final.started', final.tStartRefresh)
    PracticeTrialsLoop.addData('final.stopped', final.tStopRefresh)
    PracticeTrialsLoop.addData('blank_screen.started', blank_screen.tStartRefresh)
    PracticeTrialsLoop.addData('blank_screen.stopped', blank_screen.tStopRefresh)
    PracticeTrialsLoop.addData('text.started', text.tStartRefresh)
    PracticeTrialsLoop.addData('text.stopped', text.tStopRefresh)
    # the Routine "Practice_Trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PracticeTrialsLoop'


# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [WelcomeText]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeText* updates
    if WelcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeText.frameNStart = frameN  # exact frame index
        WelcomeText.tStart = t  # local t and not account for scr refresh
        WelcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeText, 'tStartRefresh')  # time at next scr refresh
        WelcomeText.setAutoDraw(True)
    if WelcomeText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > WelcomeText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            WelcomeText.tStop = t  # not accounting for scr refresh
            WelcomeText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(WelcomeText, 'tStopRefresh')  # time at next scr refresh
            WelcomeText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeText.started', WelcomeText.tStartRefresh)
thisExp.addData('WelcomeText.stopped', WelcomeText.tStopRefresh)

# set up handler to look after randomisation of conditions etc
TestTrialsLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('picPaths.xlsx', selection='6:30'),
    seed=None, name='TestTrialsLoop')
thisExp.addLoop(TestTrialsLoop)  # add the loop to the experiment
thisTestTrialsLoop = TestTrialsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTestTrialsLoop.rgb)
if thisTestTrialsLoop != None:
    for paramName in thisTestTrialsLoop:
        exec('{} = thisTestTrialsLoop[paramName]'.format(paramName))

for thisTestTrialsLoop in TestTrialsLoop:
    currentLoop = TestTrialsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTestTrialsLoop.rgb)
    if thisTestTrialsLoop != None:
        for paramName in thisTestTrialsLoop:
            exec('{} = thisTestTrialsLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Test_Trials"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimulusInterval = randint(low = 1, high = 9) # choose a value
    thisExp.addData('stimulusInterval', stimulusInterval) # record it in the data file
    hasPeriphery_2.setImage(endImage)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    noPeriphery_2.setImage(startImage)
    # keep track of which components have finished
    Test_TrialsComponents = [hasPeriphery_2, key_resp_2, noPeriphery_2, text_2]
    for thisComponent in Test_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Test_Trials"-------
    while continueRoutine:
        # get current time
        t = Test_TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hasPeriphery_2* updates
        if hasPeriphery_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hasPeriphery_2.frameNStart = frameN  # exact frame index
            hasPeriphery_2.tStart = t  # local t and not account for scr refresh
            hasPeriphery_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hasPeriphery_2, 'tStartRefresh')  # time at next scr refresh
            hasPeriphery_2.setAutoDraw(True)
        if hasPeriphery_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hasPeriphery_2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                hasPeriphery_2.tStop = t  # not accounting for scr refresh
                hasPeriphery_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hasPeriphery_2, 'tStopRefresh')  # time at next scr refresh
                hasPeriphery_2.setAutoDraw(False)
        if hasPeriphery_2.status == STARTED:  # only update if drawing
            hasPeriphery_2.setOpacity(frameN/(10 * stimulusInterval))
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *noPeriphery_2* updates
        if noPeriphery_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            noPeriphery_2.frameNStart = frameN  # exact frame index
            noPeriphery_2.tStart = t  # local t and not account for scr refresh
            noPeriphery_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(noPeriphery_2, 'tStartRefresh')  # time at next scr refresh
            noPeriphery_2.setAutoDraw(True)
        if noPeriphery_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > noPeriphery_2.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                noPeriphery_2.tStop = t  # not accounting for scr refresh
                noPeriphery_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(noPeriphery_2, 'tStopRefresh')  # time at next scr refresh
                noPeriphery_2.setAutoDraw(False)
        if noPeriphery_2.status == STARTED:  # only update if drawing
            noPeriphery_2.setOpacity(1-frameN/(10 * stimulusInterval))
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_Trials"-------
    for thisComponent in Test_TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TestTrialsLoop.addData('hasPeriphery_2.started', hasPeriphery_2.tStartRefresh)
    TestTrialsLoop.addData('hasPeriphery_2.stopped', hasPeriphery_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    TestTrialsLoop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        TestTrialsLoop.addData('key_resp_2.rt', key_resp_2.rt)
    TestTrialsLoop.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    TestTrialsLoop.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    TestTrialsLoop.addData('noPeriphery_2.started', noPeriphery_2.tStartRefresh)
    TestTrialsLoop.addData('noPeriphery_2.stopped', noPeriphery_2.tStopRefresh)
    TestTrialsLoop.addData('text_2.started', text_2.tStartRefresh)
    TestTrialsLoop.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "Test_Trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'TestTrialsLoop'


# ------Prepare to start Routine "Thanks_"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Thanks_Components = []
for thisComponent in Thanks_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Thanks_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thanks_"-------
while continueRoutine:
    # get current time
    t = Thanks_Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Thanks_Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thanks_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks_"-------
for thisComponent in Thanks_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thanks_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
