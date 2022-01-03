#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on Thu 25 Nov 2021 12:02:30 PM CET
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'MemLear_ses-01_part-02_label-phase2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Expra Code': ''}
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
    originPath='/home/francesco/PowerFolders/MemLear/2_Project_Documents/Data_acquisition/task/MemLear_ses-01_part-02_label-phase2/MemLear_ses-01_part-02_label-phase2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
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

# Initialize components for Routine "initialise"
initialiseClock = core.Clock()
cond_file =  'select_list'+( str((int(expInfo['participant']) % 4) + 1)) +'.csv'
print(cond_file)
print("we are here")

# Initialize components for Routine "instr_nback"
instr_nbackClock = core.Clock()
instr_nBack = visual.TextStim(win=win, name='instr_nBack',
    text='Now we would like you to work on a slightly different task. \n\nA series of words will be presented on the screen.\n\nYour task is to press the D button for YES \nwhen the word you are currently seeing is the same as the word that you have seen two trials earlier.\n\nIf this is not the case, press the L button for NO.\n\nPress SPACE to see an illustration of the task. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
istr_nback = keyboard.Keyboard()

# Initialize components for Routine "illustration"
illustrationClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "nBack_intro"
nBack_introClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You will now engage in the task. \n\nPlease place your left finger on the D button and the right finger on the L button. \n\n\nPress SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "nBack_task"
nBack_taskClock = core.Clock()
nBack_task_pres = visual.TextStim(win=win, name='nBack_task_pres',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "end_nback"
end_nbackClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thank you for completing this task!\n\nPlease return to the experimenter.\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstTop = visual.TextStim(win=win, name='InstTop',
    text='default text',
    font='bold',
    pos=(0, 0.2), height=0.05, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
InstMiddle = visual.TextStim(win=win, name='InstMiddle',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
InstrBottom = visual.TextStim(win=win, name='InstrBottom',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Inst_resp = keyboard.Keyboard()

# Initialize components for Routine "fixcross"
fixcrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "identity"
identityClock = core.Clock()
object_id = visual.ImageStim(
    win=win,
    name='object_id', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
prompt_id = visual.TextStim(win=win, name='prompt_id',
    text='Have you seen this object before?',
    font='Arial',
    pos=(0, -0.12), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prompt_id2 = visual.TextStim(win=win, name='prompt_id2',
    text='YES               NO',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
recog_resp = keyboard.Keyboard()

# Initialize components for Routine "ident_feedb"
ident_feedbClock = core.Clock()
x_square=None

feedb_objectID = visual.ImageStim(
    win=win,
    name='feedb_objectID', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
identity_fedb = visual.Rect(
    win=win, name='identity_fedb',
    width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
feedb_id = visual.TextStim(win=win, name='feedb_id',
    text='YES               NO',
    font='Arial',
    pos=(0, -0.3), height=0.1, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
feedb_idPrompt = visual.TextStim(win=win, name='feedb_idPrompt',
    text='Have you seen this object before?',
    font='arial',
    pos=(0, -0.12), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "confidence"
confidenceClock = core.Clock()
conf_resp = keyboard.Keyboard()
object_id2 = visual.ImageStim(
    win=win,
    name='object_id2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
conf_choiceprompt = visual.TextStim(win=win, name='conf_choiceprompt',
    text='How sure are you of your response?',
    font='Arial',
    pos=(0, -0.12), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='mem_optionsENG.png', mask=None,
    ori=0, pos=(0, -0.35), size=(1.3, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "confid_feedback"
confid_feedbackClock = core.Clock()
object_id3 = visual.ImageStim(
    win=win,
    name='object_id3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.2), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.35), size=(1.3, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
conf_choicefeedbprompt = visual.TextStim(win=win, name='conf_choicefeedbprompt',
    text='How sure are you of your response?',
    font='arial',
    pos=(0, -0.12), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_break = keyboard.Keyboard()
msg= "You completed half of this last task!You can take a break now if you want. Please press SPACE to continue"
loopn=1

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initialise"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initialiseComponents = []
for thisComponent in initialiseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initialiseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initialise"-------
while continueRoutine:
    # get current time
    t = initialiseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initialiseClock)
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
    for thisComponent in initialiseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initialise"-------
for thisComponent in initialiseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initialise" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_nback"-------
continueRoutine = True
# update component parameters for each repeat
istr_nback.keys = []
istr_nback.rt = []
_istr_nback_allKeys = []
# keep track of which components have finished
instr_nbackComponents = [instr_nBack, istr_nback]
for thisComponent in instr_nbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_nbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_nback"-------
while continueRoutine:
    # get current time
    t = instr_nbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_nbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_nBack* updates
    if instr_nBack.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_nBack.frameNStart = frameN  # exact frame index
        instr_nBack.tStart = t  # local t and not account for scr refresh
        instr_nBack.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_nBack, 'tStartRefresh')  # time at next scr refresh
        instr_nBack.setAutoDraw(True)
    
    # *istr_nback* updates
    waitOnFlip = False
    if istr_nback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        istr_nback.frameNStart = frameN  # exact frame index
        istr_nback.tStart = t  # local t and not account for scr refresh
        istr_nback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(istr_nback, 'tStartRefresh')  # time at next scr refresh
        istr_nback.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(istr_nback.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(istr_nback.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if istr_nback.status == STARTED and not waitOnFlip:
        theseKeys = istr_nback.getKeys(keyList=['space'], waitRelease=False)
        _istr_nback_allKeys.extend(theseKeys)
        if len(_istr_nback_allKeys):
            istr_nback.keys = _istr_nback_allKeys[-1].name  # just the last key pressed
            istr_nback.rt = _istr_nback_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_nbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_nback"-------
for thisComponent in instr_nbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr_nback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
illustration_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('illustrations.xlsx'),
    seed=None, name='illustration_loop')
thisExp.addLoop(illustration_loop)  # add the loop to the experiment
thisIllustration_loop = illustration_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisIllustration_loop.rgb)
if thisIllustration_loop != None:
    for paramName in thisIllustration_loop:
        exec('{} = thisIllustration_loop[paramName]'.format(paramName))

for thisIllustration_loop in illustration_loop:
    currentLoop = illustration_loop
    # abbreviate parameter names if possible (e.g. rgb = thisIllustration_loop.rgb)
    if thisIllustration_loop != None:
        for paramName in thisIllustration_loop:
            exec('{} = thisIllustration_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "illustration"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(images)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    illustrationComponents = [image_3, key_resp]
    for thisComponent in illustrationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    illustrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "illustration"-------
    while continueRoutine:
        # get current time
        t = illustrationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=illustrationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        
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
            theseKeys = key_resp.getKeys(keyList=['space', 'd', 'l'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in illustrationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "illustration"-------
    for thisComponent in illustrationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "illustration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'illustration_loop'


# ------Prepare to start Routine "nBack_intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
nBack_introComponents = [text_2, key_resp_2]
for thisComponent in nBack_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
nBack_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "nBack_intro"-------
while continueRoutine:
    # get current time
    t = nBack_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=nBack_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nBack_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "nBack_intro"-------
for thisComponent in nBack_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "nBack_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
nback_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nBack_list.xlsx'),
    seed=None, name='nback_loop')
thisExp.addLoop(nback_loop)  # add the loop to the experiment
thisNback_loop = nback_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNback_loop.rgb)
if thisNback_loop != None:
    for paramName in thisNback_loop:
        exec('{} = thisNback_loop[paramName]'.format(paramName))

for thisNback_loop in nback_loop:
    currentLoop = nback_loop
    # abbreviate parameter names if possible (e.g. rgb = thisNback_loop.rgb)
    if thisNback_loop != None:
        for paramName in thisNback_loop:
            exec('{} = thisNback_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "nBack_task"-------
    continueRoutine = True
    routineTimer.add(1.700000)
    # update component parameters for each repeat
    nBack_task_pres.setText(word)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    nBack_taskComponents = [nBack_task_pres, blank, key_resp_4]
    for thisComponent in nBack_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nBack_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nBack_task"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = nBack_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nBack_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *nBack_task_pres* updates
        if nBack_task_pres.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nBack_task_pres.frameNStart = frameN  # exact frame index
            nBack_task_pres.tStart = t  # local t and not account for scr refresh
            nBack_task_pres.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nBack_task_pres, 'tStartRefresh')  # time at next scr refresh
            nBack_task_pres.setAutoDraw(True)
        if nBack_task_pres.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nBack_task_pres.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                nBack_task_pres.tStop = t  # not accounting for scr refresh
                nBack_task_pres.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nBack_task_pres, 'tStopRefresh')  # time at next scr refresh
                nBack_task_pres.setAutoDraw(False)
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # *key_resp_4* updates
        if key_resp_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            key_resp_4.clock.reset()  # now t=0
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED:
            theseKeys = key_resp_4.getKeys(keyList=['l', 'd'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                # was this correct?
                if (key_resp_4.keys == str(CORRanswer)) or (key_resp_4.keys == CORRanswer):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nBack_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nBack_task"-------
    for thisComponent in nBack_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nback_loop.addData('nBack_task_pres.started', nBack_task_pres.tStartRefresh)
    nback_loop.addData('nBack_task_pres.stopped', nBack_task_pres.tStopRefresh)
    nback_loop.addData('blank.started', blank.tStartRefresh)
    nback_loop.addData('blank.stopped', blank.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(CORRanswer).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for nback_loop (TrialHandler)
    nback_loop.addData('key_resp_4.keys',key_resp_4.keys)
    nback_loop.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        nback_loop.addData('key_resp_4.rt', key_resp_4.rt)
    nback_loop.addData('key_resp_4.started', key_resp_4.tStart)
    nback_loop.addData('key_resp_4.stopped', key_resp_4.tStop)
# completed 1 repeats of 'nback_loop'


# ------Prepare to start Routine "end_nback"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
end_nbackComponents = [text_3, key_resp_5]
for thisComponent in end_nbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_nbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_nback"-------
while continueRoutine:
    # get current time
    t = end_nbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_nbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_nbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_nback"-------
for thisComponent in end_nbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "end_nback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructions_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('InstructionsPhase3.csv'),
    seed=None, name='instructions_loop')
thisExp.addLoop(instructions_loop)  # add the loop to the experiment
thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
if thisInstructions_loop != None:
    for paramName in thisInstructions_loop:
        exec('{} = thisInstructions_loop[paramName]'.format(paramName))

for thisInstructions_loop in instructions_loop:
    currentLoop = instructions_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
    if thisInstructions_loop != None:
        for paramName in thisInstructions_loop:
            exec('{} = thisInstructions_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    InstTop.setText(text1)
    InstMiddle.setText(text2)
    InstrBottom.setText(text3)
    Inst_resp.keys = []
    Inst_resp.rt = []
    _Inst_resp_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [InstTop, InstMiddle, InstrBottom, Inst_resp]
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
        
        # *InstTop* updates
        if InstTop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstTop.frameNStart = frameN  # exact frame index
            InstTop.tStart = t  # local t and not account for scr refresh
            InstTop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstTop, 'tStartRefresh')  # time at next scr refresh
            InstTop.setAutoDraw(True)
        
        # *InstMiddle* updates
        if InstMiddle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstMiddle.frameNStart = frameN  # exact frame index
            InstMiddle.tStart = t  # local t and not account for scr refresh
            InstMiddle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstMiddle, 'tStartRefresh')  # time at next scr refresh
            InstMiddle.setAutoDraw(True)
        
        # *InstrBottom* updates
        if InstrBottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstrBottom.frameNStart = frameN  # exact frame index
            InstrBottom.tStart = t  # local t and not account for scr refresh
            InstrBottom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstrBottom, 'tStartRefresh')  # time at next scr refresh
            InstrBottom.setAutoDraw(True)
        
        # *Inst_resp* updates
        waitOnFlip = False
        if Inst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Inst_resp.frameNStart = frameN  # exact frame index
            Inst_resp.tStart = t  # local t and not account for scr refresh
            Inst_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_resp, 'tStartRefresh')  # time at next scr refresh
            Inst_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Inst_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Inst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Inst_resp.status == STARTED and not waitOnFlip:
            theseKeys = Inst_resp.getKeys(keyList=['space'], waitRelease=False)
            _Inst_resp_allKeys.extend(theseKeys)
            if len(_Inst_resp_allKeys):
                Inst_resp.keys = _Inst_resp_allKeys[-1].name  # just the last key pressed
                Inst_resp.rt = _Inst_resp_allKeys[-1].rt
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
    instructions_loop.addData('InstMiddle.started', InstMiddle.tStartRefresh)
    instructions_loop.addData('InstMiddle.stopped', InstMiddle.tStopRefresh)
    instructions_loop.addData('InstrBottom.started', InstrBottom.tStartRefresh)
    instructions_loop.addData('InstrBottom.stopped', InstrBottom.tStopRefresh)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructions_loop'


# set up handler to look after randomisation of conditions etc
list_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file),
    seed=None, name='list_loop')
thisExp.addLoop(list_loop)  # add the loop to the experiment
thisList_loop = list_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisList_loop.rgb)
if thisList_loop != None:
    for paramName in thisList_loop:
        exec('{} = thisList_loop[paramName]'.format(paramName))

for thisList_loop in list_loop:
    currentLoop = list_loop
    # abbreviate parameter names if possible (e.g. rgb = thisList_loop.rgb)
    if thisList_loop != None:
        for paramName in thisList_loop:
            exec('{} = thisList_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    recog_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(recog_list),
        seed=None, name='recog_loop')
    thisExp.addLoop(recog_loop)  # add the loop to the experiment
    thisRecog_loop = recog_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecog_loop.rgb)
    if thisRecog_loop != None:
        for paramName in thisRecog_loop:
            exec('{} = thisRecog_loop[paramName]'.format(paramName))
    
    for thisRecog_loop in recog_loop:
        currentLoop = recog_loop
        # abbreviate parameter names if possible (e.g. rgb = thisRecog_loop.rgb)
        if thisRecog_loop != None:
            for paramName in thisRecog_loop:
                exec('{} = thisRecog_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixcross"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixcrossComponents = [fix]
        for thisComponent in fixcrossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixcrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixcross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixcrossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixcrossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                fix.setAutoDraw(True)
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                    fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixcrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixcross"-------
        for thisComponent in fixcrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recog_loop.addData('fix.started', fix.tStartRefresh)
        recog_loop.addData('fix.stopped', fix.tStopRefresh)
        
        # ------Prepare to start Routine "identity"-------
        continueRoutine = True
        # update component parameters for each repeat
        object_id.setImage(images)
        recog_resp.keys = []
        recog_resp.rt = []
        _recog_resp_allKeys = []
        # keep track of which components have finished
        identityComponents = [object_id, prompt_id, prompt_id2, recog_resp]
        for thisComponent in identityComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        identityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "identity"-------
        while continueRoutine:
            # get current time
            t = identityClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=identityClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *object_id* updates
            if object_id.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                object_id.frameNStart = frameN  # exact frame index
                object_id.tStart = t  # local t and not account for scr refresh
                object_id.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_id, 'tStartRefresh')  # time at next scr refresh
                object_id.setAutoDraw(True)
            
            # *prompt_id* updates
            if prompt_id.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_id.frameNStart = frameN  # exact frame index
                prompt_id.tStart = t  # local t and not account for scr refresh
                prompt_id.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_id, 'tStartRefresh')  # time at next scr refresh
                prompt_id.setAutoDraw(True)
            
            # *prompt_id2* updates
            if prompt_id2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_id2.frameNStart = frameN  # exact frame index
                prompt_id2.tStart = t  # local t and not account for scr refresh
                prompt_id2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_id2, 'tStartRefresh')  # time at next scr refresh
                prompt_id2.setAutoDraw(True)
            
            # *recog_resp* updates
            waitOnFlip = False
            if recog_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recog_resp.frameNStart = frameN  # exact frame index
                recog_resp.tStart = t  # local t and not account for scr refresh
                recog_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recog_resp, 'tStartRefresh')  # time at next scr refresh
                recog_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(recog_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(recog_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if recog_resp.status == STARTED and not waitOnFlip:
                theseKeys = recog_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _recog_resp_allKeys.extend(theseKeys)
                if len(_recog_resp_allKeys):
                    recog_resp.keys = _recog_resp_allKeys[-1].name  # just the last key pressed
                    recog_resp.rt = _recog_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in identityComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "identity"-------
        for thisComponent in identityComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        recog_loop.addData('object_id.started', object_id.tStartRefresh)
        recog_loop.addData('object_id.stopped', object_id.tStopRefresh)
        recog_loop.addData('prompt_id.started', prompt_id.tStartRefresh)
        recog_loop.addData('prompt_id.stopped', prompt_id.tStopRefresh)
        # check responses
        if recog_resp.keys in ['', [], None]:  # No response was made
            recog_resp.keys = None
        recog_loop.addData('recog_resp.keys',recog_resp.keys)
        if recog_resp.keys != None:  # we had a response
            recog_loop.addData('recog_resp.rt', recog_resp.rt)
        # the Routine "identity" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ident_feedb"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if recog_resp.keys=="right":
            x_square=0.3
            assoc=0
        else:
            x_square=-0.3
            assoc=1
        
        feedb_objectID.setImage(images)
        identity_fedb.setPos([x_square,-0.3])
        # keep track of which components have finished
        ident_feedbComponents = [feedb_objectID, identity_fedb, feedb_id, feedb_idPrompt]
        for thisComponent in ident_feedbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ident_feedbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ident_feedb"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ident_feedbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ident_feedbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedb_objectID* updates
            if feedb_objectID.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedb_objectID.frameNStart = frameN  # exact frame index
                feedb_objectID.tStart = t  # local t and not account for scr refresh
                feedb_objectID.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedb_objectID, 'tStartRefresh')  # time at next scr refresh
                feedb_objectID.setAutoDraw(True)
            if feedb_objectID.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedb_objectID.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedb_objectID.tStop = t  # not accounting for scr refresh
                    feedb_objectID.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedb_objectID, 'tStopRefresh')  # time at next scr refresh
                    feedb_objectID.setAutoDraw(False)
            
            # *identity_fedb* updates
            if identity_fedb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                identity_fedb.frameNStart = frameN  # exact frame index
                identity_fedb.tStart = t  # local t and not account for scr refresh
                identity_fedb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(identity_fedb, 'tStartRefresh')  # time at next scr refresh
                identity_fedb.setAutoDraw(True)
            if identity_fedb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > identity_fedb.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    identity_fedb.tStop = t  # not accounting for scr refresh
                    identity_fedb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(identity_fedb, 'tStopRefresh')  # time at next scr refresh
                    identity_fedb.setAutoDraw(False)
            
            # *feedb_id* updates
            if feedb_id.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedb_id.frameNStart = frameN  # exact frame index
                feedb_id.tStart = t  # local t and not account for scr refresh
                feedb_id.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedb_id, 'tStartRefresh')  # time at next scr refresh
                feedb_id.setAutoDraw(True)
            if feedb_id.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedb_id.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedb_id.tStop = t  # not accounting for scr refresh
                    feedb_id.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedb_id, 'tStopRefresh')  # time at next scr refresh
                    feedb_id.setAutoDraw(False)
            
            # *feedb_idPrompt* updates
            if feedb_idPrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedb_idPrompt.frameNStart = frameN  # exact frame index
                feedb_idPrompt.tStart = t  # local t and not account for scr refresh
                feedb_idPrompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedb_idPrompt, 'tStartRefresh')  # time at next scr refresh
                feedb_idPrompt.setAutoDraw(True)
            if feedb_idPrompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedb_idPrompt.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedb_idPrompt.tStop = t  # not accounting for scr refresh
                    feedb_idPrompt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedb_idPrompt, 'tStopRefresh')  # time at next scr refresh
                    feedb_idPrompt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ident_feedbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ident_feedb"-------
        for thisComponent in ident_feedbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        x_square=None
        recog_loop.addData('feedb_objectID.started', feedb_objectID.tStartRefresh)
        recog_loop.addData('feedb_objectID.stopped', feedb_objectID.tStopRefresh)
        recog_loop.addData('feedb_idPrompt.started', feedb_idPrompt.tStartRefresh)
        recog_loop.addData('feedb_idPrompt.stopped', feedb_idPrompt.tStopRefresh)
        
        # ------Prepare to start Routine "confidence"-------
        continueRoutine = True
        # update component parameters for each repeat
        conf_resp.keys = []
        conf_resp.rt = []
        _conf_resp_allKeys = []
        object_id2.setImage(images)
        # keep track of which components have finished
        confidenceComponents = [conf_resp, object_id2, conf_choiceprompt, image]
        for thisComponent in confidenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        confidenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "confidence"-------
        while continueRoutine:
            # get current time
            t = confidenceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=confidenceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *conf_resp* updates
            waitOnFlip = False
            if conf_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conf_resp.frameNStart = frameN  # exact frame index
                conf_resp.tStart = t  # local t and not account for scr refresh
                conf_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conf_resp, 'tStartRefresh')  # time at next scr refresh
                conf_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(conf_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(conf_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if conf_resp.status == STARTED and not waitOnFlip:
                theseKeys = conf_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                _conf_resp_allKeys.extend(theseKeys)
                if len(_conf_resp_allKeys):
                    conf_resp.keys = _conf_resp_allKeys[-1].name  # just the last key pressed
                    conf_resp.rt = _conf_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *object_id2* updates
            if object_id2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                object_id2.frameNStart = frameN  # exact frame index
                object_id2.tStart = t  # local t and not account for scr refresh
                object_id2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_id2, 'tStartRefresh')  # time at next scr refresh
                object_id2.setAutoDraw(True)
            
            # *conf_choiceprompt* updates
            if conf_choiceprompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conf_choiceprompt.frameNStart = frameN  # exact frame index
                conf_choiceprompt.tStart = t  # local t and not account for scr refresh
                conf_choiceprompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conf_choiceprompt, 'tStartRefresh')  # time at next scr refresh
                conf_choiceprompt.setAutoDraw(True)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in confidenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "confidence"-------
        for thisComponent in confidenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if conf_resp.keys in ['', [], None]:  # No response was made
            conf_resp.keys = None
        recog_loop.addData('conf_resp.keys',conf_resp.keys)
        if conf_resp.keys != None:  # we had a response
            recog_loop.addData('conf_resp.rt', conf_resp.rt)
        # the Routine "confidence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "confid_feedback"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        if conf_resp.keys=="1":
            imagfeedb="mem_optionsENG1.png"
        elif conf_resp.keys=="2":
            imagfeedb="mem_optionsENG2.png"
        elif conf_resp.keys=="3":
            imagfeedb="mem_optionsENG3.png"
        elif conf_resp.keys=="4":
            imagfeedb="mem_optionsENG4.png"
        object_id3.setImage(images)
        image_2.setImage(imagfeedb)
        # keep track of which components have finished
        confid_feedbackComponents = [object_id3, image_2, conf_choicefeedbprompt]
        for thisComponent in confid_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        confid_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "confid_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = confid_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=confid_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *object_id3* updates
            if object_id3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                object_id3.frameNStart = frameN  # exact frame index
                object_id3.tStart = t  # local t and not account for scr refresh
                object_id3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_id3, 'tStartRefresh')  # time at next scr refresh
                object_id3.setAutoDraw(True)
            if object_id3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > object_id3.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    object_id3.tStop = t  # not accounting for scr refresh
                    object_id3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(object_id3, 'tStopRefresh')  # time at next scr refresh
                    object_id3.setAutoDraw(False)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(False)
            
            # *conf_choicefeedbprompt* updates
            if conf_choicefeedbprompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conf_choicefeedbprompt.frameNStart = frameN  # exact frame index
                conf_choicefeedbprompt.tStart = t  # local t and not account for scr refresh
                conf_choicefeedbprompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conf_choicefeedbprompt, 'tStartRefresh')  # time at next scr refresh
                conf_choicefeedbprompt.setAutoDraw(True)
            if conf_choicefeedbprompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > conf_choicefeedbprompt.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    conf_choicefeedbprompt.tStop = t  # not accounting for scr refresh
                    conf_choicefeedbprompt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(conf_choicefeedbprompt, 'tStopRefresh')  # time at next scr refresh
                    conf_choicefeedbprompt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in confid_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "confid_feedback"-------
        for thisComponent in confid_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        x_square=None
        
           
        recog_loop.addData('image_2.started', image_2.tStartRefresh)
        recog_loop.addData('image_2.stopped', image_2.tStopRefresh)
        recog_loop.addData('conf_choicefeedbprompt.started', conf_choicefeedbprompt.tStartRefresh)
        recog_loop.addData('conf_choicefeedbprompt.stopped', conf_choicefeedbprompt.tStopRefresh)
    # completed 1 repeats of 'recog_loop'
    
    
    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text.setText(msg)
    key_resp_break.keys = []
    key_resp_break.rt = []
    _key_resp_break_allKeys = []
    loopn=loopn+1
    if loopn==2:
        msg="Thank you for completing the task! Please do not close the browser window until data has finished loading. Press SPACE to continue"
    
    print(loopn)
    # keep track of which components have finished
    break_2Components = [text, key_resp_break]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp_break* updates
        waitOnFlip = False
        if key_resp_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_break.frameNStart = frameN  # exact frame index
            key_resp_break.tStart = t  # local t and not account for scr refresh
            key_resp_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_break, 'tStartRefresh')  # time at next scr refresh
            key_resp_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_break.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_break.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_break_allKeys.extend(theseKeys)
            if len(_key_resp_break_allKeys):
                key_resp_break.keys = _key_resp_break_allKeys[-1].name  # just the last key pressed
                key_resp_break.rt = _key_resp_break_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    list_loop.addData('text.started', text.tStartRefresh)
    list_loop.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp_break.keys in ['', [], None]:  # No response was made
        key_resp_break.keys = None
    list_loop.addData('key_resp_break.keys',key_resp_break.keys)
    if key_resp_break.keys != None:  # we had a response
        list_loop.addData('key_resp_break.rt', key_resp_break.rt)
    list_loop.addData('key_resp_break.started', key_resp_break.tStartRefresh)
    list_loop.addData('key_resp_break.stopped', key_resp_break.tStopRefresh)
    trialn=2
    
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'list_loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
