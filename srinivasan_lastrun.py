#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), November 18, 2014, at 13:45
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'srinivasan'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Cameron\\Google Drive\\Experiments\\Categories-Properties\\srinivasan.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.TextStim(win=win, ori=0, name='intro_text',
    text='default text',    font='Arial',
    pos=[0, .3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press SPACE to continue!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
sentence_stim = visual.TextStim(win=win, ori=0, name='sentence_stim',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
property_stim = visual.TextStim(win=win, ori=0, name='property_stim',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
sound_2 = sound.Sound('sound.wav', secs=1.0)
sound_2.setVolume(1)
playSound = True

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.TextStim(win=win, ori=0, name='intro_text',
    text='default text',    font='Arial',
    pos=[0, .3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Press SPACE to continue!',    font='Arial',
    pos=[0, -.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=None,    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
sentence_stim = visual.TextStim(win=win, ori=0, name='sentence_stim',
    text='default text',    font='Arial',
    pos=[0, .1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
property_stim = visual.TextStim(win=win, ori=0, name='property_stim',
    text='default text',    font='Arial',
    pos=[0, -.1], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
sound_2 = sound.Sound('sound.wav', secs=1.0)
sound_2.setVolume(1)
playSound = True

# Initialize components for Routine "end"
endClock = core.Clock()
ending = visual.TextStim(win=win, ori=0, name='ending',
    text='Thanks for participating! Turn around and tell the experimenter that you are finished!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instr1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath='C:\\Users\\Cameron\\Google Drive\\Experiments\\Categories-Properties\\srinivasan.psyexp',
    trialList=data.importConditions('instructions-p1.xlsx'),
    seed=None, name='instr1')
thisExp.addLoop(instr1)  # add the loop to the experiment
thisInstr1 = instr1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstr1.rgb)
if thisInstr1 != None:
    for paramName in thisInstr1.keys():
        exec(paramName + '= thisInstr1.' + paramName)

for thisInstr1 in instr1:
    currentLoop = instr1
    # abbreviate parameter names if possible (e.g. rgb = thisInstr1.rgb)
    if thisInstr1 != None:
        for paramName in thisInstr1.keys():
            exec(paramName + '= thisInstr1.' + paramName)
    
    #------Prepare to start Routine "intro"-------
    t = 0
    introClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    intro_text.setText(text)
    key1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key1.status = NOT_STARTED
    # keep track of which components have finished
    introComponents = []
    introComponents.append(intro_text)
    introComponents.append(key1)
    introComponents.append(text_2)
    for thisComponent in introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "intro"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_text* updates
        if t >= 0.0 and intro_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_text.tStart = t  # underestimates by a little under one frame
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.setAutoDraw(True)
        
        # *key1* updates
        if t >= 0.0 and key1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key1.tStart = t  # underestimates by a little under one frame
            key1.frameNStart = frameN  # exact frame index
            key1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'instr1'


# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\Cameron\\Google Drive\\Experiments\\Categories-Properties\\srinivasan.psyexp',
    trialList=data.importConditions('stim-prac.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice.keys():
        exec(paramName + '= thisPractice.' + paramName)

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice.keys():
            exec(paramName + '= thisPractice.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sentence_stim.setText(sentence)
    property_stim.setText(property)
    true_or_false = event.BuilderKeyResponse()  # create an object of type KeyResponse
    true_or_false.status = NOT_STARTED
    playSound = False
    for item in theseKeys:
        if (item == 'j' and response != 'j') or (item == 'f' and response != 'f'):
            playSound = True
    endroutine = event.BuilderKeyResponse()  # create an object of type KeyResponse
    endroutine.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(sentence_stim)
    trialComponents.append(property_stim)
    trialComponents.append(true_or_false)
    trialComponents.append(sound_2)
    trialComponents.append(endroutine)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentence_stim* updates
        if t >= 0.5 and sentence_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence_stim.tStart = t  # underestimates by a little under one frame
            sentence_stim.frameNStart = frameN  # exact frame index
            sentence_stim.setAutoDraw(True)
        elif sentence_stim.status == STARTED and t >= (0.5 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            sentence_stim.setAutoDraw(False)
        
        # *property_stim* updates
        if t >= 6.5 and property_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            property_stim.tStart = t  # underestimates by a little under one frame
            property_stim.frameNStart = frameN  # exact frame index
            property_stim.setAutoDraw(True)
        
        # *true_or_false* updates
        if t >= 6.5 and true_or_false.status == NOT_STARTED:
            # keep track of start time/frame for later
            true_or_false.tStart = t  # underestimates by a little under one frame
            true_or_false.frameNStart = frameN  # exact frame index
            true_or_false.status = STARTED
            # keyboard checking is just starting
            true_or_false.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if true_or_false.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                true_or_false.keys = theseKeys[-1]  # just the last key pressed
                true_or_false.rt = true_or_false.clock.getTime()
        # start/stop sound_2
        if (playSound == True) and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (sound_2.tStart + 1.0):
            sound_2.stop()  # stop the sound (if longer than duration)
        playSound = False
        for item in theseKeys:
            if (item == 'j' and response != 'j') or (item == 'f' and response != 'f'):
                playSound = True
        
        # *endroutine* updates
        if t >= true_or_false.status==FINISHED and endroutine.status == NOT_STARTED:
            # keep track of start time/frame for later
            endroutine.tStart = t  # underestimates by a little under one frame
            endroutine.frameNStart = frameN  # exact frame index
            endroutine.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if endroutine.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if true_or_false.keys in ['', [], None]:  # No response was made
       true_or_false.keys=None
    # store data for practice (TrialHandler)
    practice.addData('true_or_false.keys',true_or_false.keys)
    if true_or_false.keys != None:  # we had a response
        practice.addData('true_or_false.rt', true_or_false.rt)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice'


# set up handler to look after randomisation of conditions etc
instr2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath='C:\\Users\\Cameron\\Google Drive\\Experiments\\Categories-Properties\\srinivasan.psyexp',
    trialList=data.importConditions('instructions-p2.xlsx'),
    seed=None, name='instr2')
thisExp.addLoop(instr2)  # add the loop to the experiment
thisInstr2 = instr2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstr2.rgb)
if thisInstr2 != None:
    for paramName in thisInstr2.keys():
        exec(paramName + '= thisInstr2.' + paramName)

for thisInstr2 in instr2:
    currentLoop = instr2
    # abbreviate parameter names if possible (e.g. rgb = thisInstr2.rgb)
    if thisInstr2 != None:
        for paramName in thisInstr2.keys():
            exec(paramName + '= thisInstr2.' + paramName)
    
    #------Prepare to start Routine "intro"-------
    t = 0
    introClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    intro_text.setText(text)
    key1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key1.status = NOT_STARTED
    # keep track of which components have finished
    introComponents = []
    introComponents.append(intro_text)
    introComponents.append(key1)
    introComponents.append(text_2)
    for thisComponent in introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "intro"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_text* updates
        if t >= 0.0 and intro_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            intro_text.tStart = t  # underestimates by a little under one frame
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.setAutoDraw(True)
        
        # *key1* updates
        if t >= 0.0 and key1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key1.tStart = t  # underestimates by a little under one frame
            key1.frameNStart = frameN  # exact frame index
            key1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'instr2'


#------Prepare to start Routine "pause"-------
t = 0
pauseClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
pauseComponents = []
pauseComponents.append(key_resp_2)
pauseComponents.append(text_3)
for thisComponent in pauseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pause"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pauseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['l'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "pause"-------
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\Cameron\\Google Drive\\Experiments\\Categories-Properties\\srinivasan.psyexp',
    trialList=data.importConditions('stim-test.xlsx'),
    seed=None, name='test')
thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTest.rgb)
if thisTest != None:
    for paramName in thisTest.keys():
        exec(paramName + '= thisTest.' + paramName)

for thisTest in test:
    currentLoop = test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest.keys():
            exec(paramName + '= thisTest.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sentence_stim.setText(sentence)
    property_stim.setText(property)
    true_or_false = event.BuilderKeyResponse()  # create an object of type KeyResponse
    true_or_false.status = NOT_STARTED
    playSound = False
    for item in theseKeys:
        if (item == 'j' and response != 'j') or (item == 'f' and response != 'f'):
            playSound = True
    endroutine = event.BuilderKeyResponse()  # create an object of type KeyResponse
    endroutine.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(sentence_stim)
    trialComponents.append(property_stim)
    trialComponents.append(true_or_false)
    trialComponents.append(sound_2)
    trialComponents.append(endroutine)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentence_stim* updates
        if t >= 0.5 and sentence_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence_stim.tStart = t  # underestimates by a little under one frame
            sentence_stim.frameNStart = frameN  # exact frame index
            sentence_stim.setAutoDraw(True)
        elif sentence_stim.status == STARTED and t >= (0.5 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            sentence_stim.setAutoDraw(False)
        
        # *property_stim* updates
        if t >= 6.5 and property_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            property_stim.tStart = t  # underestimates by a little under one frame
            property_stim.frameNStart = frameN  # exact frame index
            property_stim.setAutoDraw(True)
        
        # *true_or_false* updates
        if t >= 6.5 and true_or_false.status == NOT_STARTED:
            # keep track of start time/frame for later
            true_or_false.tStart = t  # underestimates by a little under one frame
            true_or_false.frameNStart = frameN  # exact frame index
            true_or_false.status = STARTED
            # keyboard checking is just starting
            true_or_false.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if true_or_false.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                true_or_false.keys = theseKeys[-1]  # just the last key pressed
                true_or_false.rt = true_or_false.clock.getTime()
        # start/stop sound_2
        if (playSound == True) and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        elif sound_2.status == STARTED and t >= (sound_2.tStart + 1.0):
            sound_2.stop()  # stop the sound (if longer than duration)
        playSound = False
        for item in theseKeys:
            if (item == 'j' and response != 'j') or (item == 'f' and response != 'f'):
                playSound = True
        
        # *endroutine* updates
        if t >= true_or_false.status==FINISHED and endroutine.status == NOT_STARTED:
            # keep track of start time/frame for later
            endroutine.tStart = t  # underestimates by a little under one frame
            endroutine.frameNStart = frameN  # exact frame index
            endroutine.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if endroutine.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if true_or_false.keys in ['', [], None]:  # No response was made
       true_or_false.keys=None
    # store data for test (TrialHandler)
    test.addData('true_or_false.keys',true_or_false.keys)
    if true_or_false.keys != None:  # we had a response
        test.addData('true_or_false.rt', true_or_false.rt)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'test'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = []
endComponents.append(ending)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ending* updates
    if t >= 0.0 and ending.status == NOT_STARTED:
        # keep track of start time/frame for later
        ending.tStart = t  # underestimates by a little under one frame
        ending.frameNStart = frameN  # exact frame index
        ending.setAutoDraw(True)
    elif ending.status == STARTED and t >= (0.0 + (15-win.monitorFramePeriod*0.75)): #most of one frame period left
        ending.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


win.close()
core.quit()
