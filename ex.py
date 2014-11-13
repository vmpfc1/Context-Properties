#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), August 30, 2014, at 02:53
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

# Store info about the experiment session
expName = u'ArgumentsEx'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Text = visual.TextStim(win=win, ori=0, name='Text',
    text='default text',    font='fuzzy.ttf',
    units=u'cm', pos=[0,0], height=1, wrapWidth=35,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "code"
codeClock = core.Clock()



number = 0
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='default text',    font='fuzzy.ttf',
    units=u'cm', pos=[0, 0], height=1, wrapWidth=35,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Text_Trial = visual.TextStim(win=win, ori=0, name='Text_Trial',
    text='default text',    font=u'Helvetica',
    units=u'cm', pos=[0,0], height=1, wrapWidth=35,
    color=u'green', colorSpace=u'rgb', opacity=.1,
    depth=0.0)

# Initialize components for Routine "Reply"
ReplyClock = core.Clock()
Reply_Text = visual.TextStim(win=win, ori=0, name='Reply_Text',
    text='default text',    font='fuzzy.ttf',
    units=u'cm', pos=[0,0], height=1, wrapWidth=35,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Instructions_file = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'Instructions.xlsx'),
    seed=None, name='Instructions_file')
thisExp.addLoop(Instructions_file)  # add the loop to the experiment
thisInstructions_file = Instructions_file.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstructions_file.rgb)
if thisInstructions_file != None:
    for paramName in thisInstructions_file.keys():
        exec(paramName + '= thisInstructions_file.' + paramName)

for thisInstructions_file in Instructions_file:
    currentLoop = Instructions_file
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_file.rgb)
    if thisInstructions_file != None:
        for paramName in thisInstructions_file.keys():
            exec(paramName + '= thisInstructions_file.' + paramName)
    
    #------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Text.setText(text)
    Text.setPos([0, 0])
    Next = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Next.status = NOT_STARTED
    # keep track of which components have finished
    InstructionsComponents = []
    InstructionsComponents.append(Text)
    InstructionsComponents.append(Next)
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Text* updates
        if t >= 0.0 and Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Text.tStart = t  # underestimates by a little under one frame
            Text.frameNStart = frameN  # exact frame index
            Text.setAutoDraw(True)
        
        # *Next* updates
        if t >= 0.0 and Next.status == NOT_STARTED:
            # keep track of start time/frame for later
            Next.tStart = t  # underestimates by a little under one frame
            Next.frameNStart = frameN  # exact frame index
            Next.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if Next.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
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
        for thisComponent in InstructionsComponents:
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
    
    #-------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Instructions_file'


# set up handler to look after randomisation of conditions etc
Trial_Loop = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'sentences.xlsx'),
    seed=None, name='Trial_Loop')
thisExp.addLoop(Trial_Loop)  # add the loop to the experiment
thisTrial_Loop = Trial_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_Loop.rgb)
if thisTrial_Loop != None:
    for paramName in thisTrial_Loop.keys():
        exec(paramName + '= thisTrial_Loop.' + paramName)

for thisTrial_Loop in Trial_Loop:
    currentLoop = Trial_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_Loop.rgb)
    if thisTrial_Loop != None:
        for paramName in thisTrial_Loop.keys():
            exec(paramName + '= thisTrial_Loop.' + paramName)
    
    #------Prepare to start Routine "code"-------
    t = 0
    codeClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    
    number += 1 # this counts which sentence we're on, starting with 1
    
    """
    write a script to take a horizontal spreadsheet with x
    rows and make it into x individual spreadsheets with one column.
    
    Also get it to make the 'Trial_Loop' spreadsheet that contains only
    the names of the sentence spreadsheets
    
    """
    text_2.setText(number)
    # keep track of which components have finished
    codeComponents = []
    codeComponents.append(text_2)
    for thisComponent in codeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "code"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = codeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        elif text_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "code"-------
    for thisComponent in codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # set up handler to look after randomisation of conditions etc
    Practice = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(which_text),
        seed=None, name='Practice')
    thisExp.addLoop(Practice)  # add the loop to the experiment
    thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice.keys():
            exec(paramName + '= thisPractice.' + paramName)
    
    for thisPractice in Practice:
        currentLoop = Practice
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice.keys():
                exec(paramName + '= thisPractice.' + paramName)
        
        #------Prepare to start Routine "Trial"-------
        t = 0
        TrialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        Text_Trial.setText(text)
        Text_Trial.setPos([0, 0])
        # keep track of which components have finished
        TrialComponents = []
        TrialComponents.append(Text_Trial)
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Text_Trial* updates
            if t >= 0.0 and Text_Trial.status == NOT_STARTED:
                # keep track of start time/frame for later
                Text_Trial.tStart = t  # underestimates by a little under one frame
                Text_Trial.frameNStart = frameN  # exact frame index
                Text_Trial.setAutoDraw(True)
            elif Text_Trial.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                Text_Trial.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Practice'
    
    
    #------Prepare to start Routine "Reply"-------
    t = 0
    ReplyClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Reply_Text.setText(u'Please rate this argument on a scale from 1 to 7')
    Reply_Text.setPos([0, 0])
    Reply_Key = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Reply_Key.status = NOT_STARTED
    # keep track of which components have finished
    ReplyComponents = []
    ReplyComponents.append(Reply_Text)
    ReplyComponents.append(Reply_Key)
    for thisComponent in ReplyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Reply"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ReplyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Reply_Text* updates
        if t >= 0.0 and Reply_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Reply_Text.tStart = t  # underestimates by a little under one frame
            Reply_Text.frameNStart = frameN  # exact frame index
            Reply_Text.setAutoDraw(True)
        elif Reply_Text.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Reply_Text.setAutoDraw(False)
        
        # *Reply_Key* updates
        if t >= 0.0 and Reply_Key.status == NOT_STARTED:
            # keep track of start time/frame for later
            Reply_Key.tStart = t  # underestimates by a little under one frame
            Reply_Key.frameNStart = frameN  # exact frame index
            Reply_Key.status = STARTED
            # keyboard checking is just starting
            Reply_Key.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if Reply_Key.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Reply_Key.keys = theseKeys[-1]  # just the last key pressed
                Reply_Key.rt = Reply_Key.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReplyComponents:
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
    
    #-------Ending Routine "Reply"-------
    for thisComponent in ReplyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Reply_Key.keys in ['', [], None]:  # No response was made
       Reply_Key.keys=None
    # store data for Trial_Loop (TrialHandler)
    Trial_Loop.addData('Reply_Key.keys',Reply_Key.keys)
    if Reply_Key.keys != None:  # we had a response
        Trial_Loop.addData('Reply_Key.rt', Reply_Key.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Trial_Loop'


win.close()
core.quit()
