#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on November 14, 2024, at 20:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'experiment'  # from the Builder filename that created this script
expInfo = {
    'task': 'calib',
    'participant': '',
}
# --- Show participant info dialog --
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
    originPath='U:\\cpsc4120\\resume_experiment\\experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.gazepoint.gp3.EyeTracker'] = {
    'name': 'tracker',
    'network_settings': {
        'ip_address': '127.0.0.1',
        'port': 4242.0
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='experiment', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "calib_instr" ---
calib_instr_text = visual.TextStim(win=win, name='calib_instr_text',
    text="We must first calibrate the eye tracker.\n\nKeep your eye on the calibration do but don't anticipate it's movement.\n\nThere will be a 9-point calibration process followed by a 5-point validation step to ensure the calibration was successful.\n\nPress space to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
calib_instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "calib_cont" ---
# Run 'Begin Experiment' code from code
timeout = 10
ave_error = 0.0
valid_calib_points = 0
calib_text = visual.TextStim(win=win, name='calib_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
calib_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ready_up" ---
text = visual.TextStim(win=win, name='text',
    text='You will have 8 seconds to view each resume and 3 questions will be asked after each resume.\n\nThe job posting will be presented to you before viewing each resume.\n\nPress the space bar to begin the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "job_posting" ---
job_description = visual.ImageStim(
    win=win,
    name='job_description', 
    image='Eye Tracking Expeirement Job App.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
job_posting_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "exp1_stimulus" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "question1" ---
candidate_rating_question = visual.TextStim(win=win, name='candidate_rating_question',
    text='How fit is this candidate? (1-5)\n\n1 = Not qualified\n5 = Very qualified',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
candidate_rating = visual.Slider(win=win, name='candidate_rating',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "question2" ---
image_clarity_question = visual.TextStim(win=win, name='image_clarity_question',
    text='Viewing this image was... (1-5)\n\n1 = Very difficult\n5 = Very easy',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_clarity_rating = visual.Slider(win=win, name='image_clarity_rating',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "question3" ---
comprehension_question = visual.TextStim(win=win, name='comprehension_question',
    text='How well did you comprehend the information presented? (1-5)\n\n1 = Little comprehension\n5 = Good comprehension',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
comprehension_rating = visual.Slider(win=win, name='comprehension_rating',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "ready_up" ---
text = visual.TextStim(win=win, name='text',
    text='You will have 8 seconds to view each resume and 3 questions will be asked after each resume.\n\nThe job posting will be presented to you before viewing each resume.\n\nPress the space bar to begin the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "job_posting" ---
job_description = visual.ImageStim(
    win=win,
    name='job_description', 
    image='Eye Tracking Expeirement Job App.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
job_posting_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "exp2_stimulus" ---
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
etRecord_2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)

# --- Initialize components for Routine "question1" ---
candidate_rating_question = visual.TextStim(win=win, name='candidate_rating_question',
    text='How fit is this candidate? (1-5)\n\n1 = Not qualified\n5 = Very qualified',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
candidate_rating = visual.Slider(win=win, name='candidate_rating',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "question2" ---
image_clarity_question = visual.TextStim(win=win, name='image_clarity_question',
    text='Viewing this image was... (1-5)\n\n1 = Very difficult\n5 = Very easy',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_clarity_rating = visual.Slider(win=win, name='image_clarity_rating',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "question3" ---
comprehension_question = visual.TextStim(win=win, name='comprehension_question',
    text='How well did you comprehend the information presented? (1-5)\n\n1 = Little comprehension\n5 = Good comprehension',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
comprehension_rating = visual.Slider(win=win, name='comprehension_rating',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=win.units,
    labels=None, ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "calib_instr" ---
continueRoutine = True
# update component parameters for each repeat
calib_instr_resp.keys = []
calib_instr_resp.rt = []
_calib_instr_resp_allKeys = []
# keep track of which components have finished
calib_instrComponents = [calib_instr_text, calib_instr_resp]
for thisComponent in calib_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "calib_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calib_instr_text* updates
    
    # if calib_instr_text is starting this frame...
    if calib_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_instr_text.frameNStart = frameN  # exact frame index
        calib_instr_text.tStart = t  # local t and not account for scr refresh
        calib_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_instr_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'calib_instr_text.started')
        # update status
        calib_instr_text.status = STARTED
        calib_instr_text.setAutoDraw(True)
    
    # if calib_instr_text is active this frame...
    if calib_instr_text.status == STARTED:
        # update params
        pass
    
    # *calib_instr_resp* updates
    waitOnFlip = False
    
    # if calib_instr_resp is starting this frame...
    if calib_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_instr_resp.frameNStart = frameN  # exact frame index
        calib_instr_resp.tStart = t  # local t and not account for scr refresh
        calib_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_instr_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'calib_instr_resp.started')
        # update status
        calib_instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(calib_instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(calib_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if calib_instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = calib_instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _calib_instr_resp_allKeys.extend(theseKeys)
        if len(_calib_instr_resp_allKeys):
            calib_instr_resp.keys = _calib_instr_resp_allKeys[-1].name  # just the last key pressed
            calib_instr_resp.rt = _calib_instr_resp_allKeys[-1].rt
            calib_instr_resp.duration = _calib_instr_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calib_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "calib_instr" ---
for thisComponent in calib_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "calib_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
calib_loop = data.TrialHandler(nReps=timeout, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='calib_loop')
thisExp.addLoop(calib_loop)  # add the loop to the experiment
thisCalib_loop = calib_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
if thisCalib_loop != None:
    for paramName in thisCalib_loop:
        exec('{} = thisCalib_loop[paramName]'.format(paramName))

for thisCalib_loop in calib_loop:
    currentLoop = calib_loop
    # abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
    if thisCalib_loop != None:
        for paramName in thisCalib_loop:
            exec('{} = thisCalib_loop[paramName]'.format(paramName))
    # define target for calibration
    calibrationTarget = visual.TargetStim(win, 
        name='calibrationTarget',
        radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
        innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for calibration
    calibration = hardware.eyetracker.EyetrackerCalibration(win, 
        eyetracker, calibrationTarget,
        units=None, colorSpace='rgb',
        progressMode='time', targetDur=1.5, expandScale=1.5,
        targetLayout='NINE_POINTS', randomisePos=True, textColor='white',
        movementAnimation=True, targetDelay=1.0
    )
    # run calibration
    calibration.run()
    # clear any keypresses from during calibration so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # define target for validation
    validationTarget = visual.TargetStim(win, 
        name='validationTarget',
        radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
        innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for validation
    validation = iohub.ValidationProcedure(win,
        target=validationTarget,
        gaze_cursor='green', 
        positions='FIVE_POINTS', randomize_positions=True,
        expand_scale=1.5, target_duration=1.5,
        enable_position_animation=True, target_delay=1.0,
        progress_on_key=None, text_color='auto',
        show_results_screen=True, save_results_screen=False,
        color_space='rgb', unit_type=None
    )
    # run validation
    validation.run()
    # clear any keypresses from during validation so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "validation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "calib_cont" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    ave_error = calibration.last['SUMMARY']['AVE_ERROR']
    valid_calib_points = calibration.last['SUMMARY']['VALID_POINTS']
    
    calib_query = "Average error is: %f\n\nValid points: %d\n\nRecalibrate (y/n)?" % (ave_error, valid_calib_points)
    calib_text.setText(calib_query)
    calib_resp.keys = []
    calib_resp.rt = []
    _calib_resp_allKeys = []
    # keep track of which components have finished
    calib_contComponents = [calib_text, calib_resp]
    for thisComponent in calib_contComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "calib_cont" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *calib_text* updates
        
        # if calib_text is starting this frame...
        if calib_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_text.frameNStart = frameN  # exact frame index
            calib_text.tStart = t  # local t and not account for scr refresh
            calib_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_text.started')
            # update status
            calib_text.status = STARTED
            calib_text.setAutoDraw(True)
        
        # if calib_text is active this frame...
        if calib_text.status == STARTED:
            # update params
            pass
        
        # *calib_resp* updates
        waitOnFlip = False
        
        # if calib_resp is starting this frame...
        if calib_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_resp.frameNStart = frameN  # exact frame index
            calib_resp.tStart = t  # local t and not account for scr refresh
            calib_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_resp.started')
            # update status
            calib_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(calib_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(calib_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if calib_resp.status == STARTED and not waitOnFlip:
            theseKeys = calib_resp.getKeys(keyList=['y','n'], waitRelease=False)
            _calib_resp_allKeys.extend(theseKeys)
            if len(_calib_resp_allKeys):
                calib_resp.keys = [key.name for key in _calib_resp_allKeys]  # storing all keys
                calib_resp.rt = [key.rt for key in _calib_resp_allKeys]
                calib_resp.duration = [key.duration for key in _calib_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calib_contComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calib_cont" ---
    for thisComponent in calib_contComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code
    # calib_resp Keyboard component must have set Store: all keys
    if calib_resp is not None and 'n' in calib_resp.keys:
        calib_loop.finished = True
    # check responses
    if calib_resp.keys in ['', [], None]:  # No response was made
        calib_resp.keys = None
    calib_loop.addData('calib_resp.keys',calib_resp.keys)
    if calib_resp.keys != None:  # we had a response
        calib_loop.addData('calib_resp.rt', calib_resp.rt)
        calib_loop.addData('calib_resp.duration', calib_resp.duration)
    # the Routine "calib_cont" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed timeout repeats of 'calib_loop'


# set up handler to look after randomisation of conditions etc
exp1_stimulus_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp1_stim.csv'),
    seed=None, name='exp1_stimulus_loop')
thisExp.addLoop(exp1_stimulus_loop)  # add the loop to the experiment
thisExp1_stimulus_loop = exp1_stimulus_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExp1_stimulus_loop.rgb)
if thisExp1_stimulus_loop != None:
    for paramName in thisExp1_stimulus_loop:
        exec('{} = thisExp1_stimulus_loop[paramName]'.format(paramName))

for thisExp1_stimulus_loop in exp1_stimulus_loop:
    currentLoop = exp1_stimulus_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExp1_stimulus_loop.rgb)
    if thisExp1_stimulus_loop != None:
        for paramName in thisExp1_stimulus_loop:
            exec('{} = thisExp1_stimulus_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ready_up" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ready_upComponents = [text, key_resp]
    for thisComponent in ready_upComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ready_up" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
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
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_upComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ready_up" ---
    for thisComponent in ready_upComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ready_up" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "job_posting" ---
    continueRoutine = True
    # update component parameters for each repeat
    job_posting_key_resp.keys = []
    job_posting_key_resp.rt = []
    _job_posting_key_resp_allKeys = []
    # keep track of which components have finished
    job_postingComponents = [job_description, job_posting_key_resp]
    for thisComponent in job_postingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "job_posting" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *job_description* updates
        
        # if job_description is starting this frame...
        if job_description.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            job_description.frameNStart = frameN  # exact frame index
            job_description.tStart = t  # local t and not account for scr refresh
            job_description.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(job_description, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'job_description.started')
            # update status
            job_description.status = STARTED
            job_description.setAutoDraw(True)
        
        # if job_description is active this frame...
        if job_description.status == STARTED:
            # update params
            pass
        
        # *job_posting_key_resp* updates
        waitOnFlip = False
        
        # if job_posting_key_resp is starting this frame...
        if job_posting_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            job_posting_key_resp.frameNStart = frameN  # exact frame index
            job_posting_key_resp.tStart = t  # local t and not account for scr refresh
            job_posting_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(job_posting_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'job_posting_key_resp.started')
            # update status
            job_posting_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(job_posting_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(job_posting_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if job_posting_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = job_posting_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _job_posting_key_resp_allKeys.extend(theseKeys)
            if len(_job_posting_key_resp_allKeys):
                job_posting_key_resp.keys = _job_posting_key_resp_allKeys[-1].name  # just the last key pressed
                job_posting_key_resp.rt = _job_posting_key_resp_allKeys[-1].rt
                job_posting_key_resp.duration = _job_posting_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in job_postingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "job_posting" ---
    for thisComponent in job_postingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if job_posting_key_resp.keys in ['', [], None]:  # No response was made
        job_posting_key_resp.keys = None
    exp1_stimulus_loop.addData('job_posting_key_resp.keys',job_posting_key_resp.keys)
    if job_posting_key_resp.keys != None:  # we had a response
        exp1_stimulus_loop.addData('job_posting_key_resp.rt', job_posting_key_resp.rt)
        exp1_stimulus_loop.addData('job_posting_key_resp.duration', job_posting_key_resp.duration)
    # the Routine "job_posting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp1_stimulus" ---
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(exp1_stim)
    # keep track of which components have finished
    exp1_stimulusComponents = [image, etRecord]
    for thisComponent in exp1_stimulusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp1_stimulus" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # if image is stopping this frame...
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                # update status
                image.status = FINISHED
                image.setAutoDraw(False)
        # *etRecord* updates
        
        # if etRecord is starting this frame...
        if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord.started', t)
            # update status
            etRecord.status = STARTED
        
        # if etRecord is stopping this frame...
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord.stopped', t)
                # update status
                etRecord.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp1_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp1_stimulus" ---
    for thisComponent in exp1_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # --- Prepare to start Routine "question1" ---
    continueRoutine = True
    # update component parameters for each repeat
    candidate_rating.reset()
    # keep track of which components have finished
    question1Components = [candidate_rating_question, candidate_rating]
    for thisComponent in question1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *candidate_rating_question* updates
        
        # if candidate_rating_question is starting this frame...
        if candidate_rating_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            candidate_rating_question.frameNStart = frameN  # exact frame index
            candidate_rating_question.tStart = t  # local t and not account for scr refresh
            candidate_rating_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(candidate_rating_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'candidate_rating_question.started')
            # update status
            candidate_rating_question.status = STARTED
            candidate_rating_question.setAutoDraw(True)
        
        # if candidate_rating_question is active this frame...
        if candidate_rating_question.status == STARTED:
            # update params
            pass
        
        # *candidate_rating* updates
        
        # if candidate_rating is starting this frame...
        if candidate_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            candidate_rating.frameNStart = frameN  # exact frame index
            candidate_rating.tStart = t  # local t and not account for scr refresh
            candidate_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(candidate_rating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'candidate_rating.started')
            # update status
            candidate_rating.status = STARTED
            candidate_rating.setAutoDraw(True)
        
        # if candidate_rating is active this frame...
        if candidate_rating.status == STARTED:
            # update params
            pass
        
        # Check candidate_rating for response to end routine
        if candidate_rating.getRating() is not None and candidate_rating.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question1" ---
    for thisComponent in question1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp1_stimulus_loop.addData('candidate_rating.response', candidate_rating.getRating())
    exp1_stimulus_loop.addData('candidate_rating.rt', candidate_rating.getRT())
    # the Routine "question1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "question2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_clarity_rating.reset()
    # keep track of which components have finished
    question2Components = [image_clarity_question, image_clarity_rating]
    for thisComponent in question2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_clarity_question* updates
        
        # if image_clarity_question is starting this frame...
        if image_clarity_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_clarity_question.frameNStart = frameN  # exact frame index
            image_clarity_question.tStart = t  # local t and not account for scr refresh
            image_clarity_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_clarity_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_clarity_question.started')
            # update status
            image_clarity_question.status = STARTED
            image_clarity_question.setAutoDraw(True)
        
        # if image_clarity_question is active this frame...
        if image_clarity_question.status == STARTED:
            # update params
            pass
        
        # *image_clarity_rating* updates
        
        # if image_clarity_rating is starting this frame...
        if image_clarity_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_clarity_rating.frameNStart = frameN  # exact frame index
            image_clarity_rating.tStart = t  # local t and not account for scr refresh
            image_clarity_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_clarity_rating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_clarity_rating.started')
            # update status
            image_clarity_rating.status = STARTED
            image_clarity_rating.setAutoDraw(True)
        
        # if image_clarity_rating is active this frame...
        if image_clarity_rating.status == STARTED:
            # update params
            pass
        
        # Check image_clarity_rating for response to end routine
        if image_clarity_rating.getRating() is not None and image_clarity_rating.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question2" ---
    for thisComponent in question2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp1_stimulus_loop.addData('image_clarity_rating.response', image_clarity_rating.getRating())
    exp1_stimulus_loop.addData('image_clarity_rating.rt', image_clarity_rating.getRT())
    # the Routine "question2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "question3" ---
    continueRoutine = True
    # update component parameters for each repeat
    comprehension_rating.reset()
    # keep track of which components have finished
    question3Components = [comprehension_question, comprehension_rating]
    for thisComponent in question3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *comprehension_question* updates
        
        # if comprehension_question is starting this frame...
        if comprehension_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comprehension_question.frameNStart = frameN  # exact frame index
            comprehension_question.tStart = t  # local t and not account for scr refresh
            comprehension_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comprehension_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'comprehension_question.started')
            # update status
            comprehension_question.status = STARTED
            comprehension_question.setAutoDraw(True)
        
        # if comprehension_question is active this frame...
        if comprehension_question.status == STARTED:
            # update params
            pass
        
        # *comprehension_rating* updates
        
        # if comprehension_rating is starting this frame...
        if comprehension_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comprehension_rating.frameNStart = frameN  # exact frame index
            comprehension_rating.tStart = t  # local t and not account for scr refresh
            comprehension_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comprehension_rating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'comprehension_rating.started')
            # update status
            comprehension_rating.status = STARTED
            comprehension_rating.setAutoDraw(True)
        
        # if comprehension_rating is active this frame...
        if comprehension_rating.status == STARTED:
            # update params
            pass
        
        # Check comprehension_rating for response to end routine
        if comprehension_rating.getRating() is not None and comprehension_rating.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question3" ---
    for thisComponent in question3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp1_stimulus_loop.addData('comprehension_rating.response', comprehension_rating.getRating())
    exp1_stimulus_loop.addData('comprehension_rating.rt', comprehension_rating.getRT())
    # the Routine "question3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'exp1_stimulus_loop'


# set up handler to look after randomisation of conditions etc
exp2_stimulus_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp2_stim.csv'),
    seed=None, name='exp2_stimulus_loop')
thisExp.addLoop(exp2_stimulus_loop)  # add the loop to the experiment
thisExp2_stimulus_loop = exp2_stimulus_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExp2_stimulus_loop.rgb)
if thisExp2_stimulus_loop != None:
    for paramName in thisExp2_stimulus_loop:
        exec('{} = thisExp2_stimulus_loop[paramName]'.format(paramName))

for thisExp2_stimulus_loop in exp2_stimulus_loop:
    currentLoop = exp2_stimulus_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExp2_stimulus_loop.rgb)
    if thisExp2_stimulus_loop != None:
        for paramName in thisExp2_stimulus_loop:
            exec('{} = thisExp2_stimulus_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ready_up" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    ready_upComponents = [text, key_resp]
    for thisComponent in ready_upComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ready_up" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
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
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_upComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ready_up" ---
    for thisComponent in ready_upComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ready_up" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "job_posting" ---
    continueRoutine = True
    # update component parameters for each repeat
    job_posting_key_resp.keys = []
    job_posting_key_resp.rt = []
    _job_posting_key_resp_allKeys = []
    # keep track of which components have finished
    job_postingComponents = [job_description, job_posting_key_resp]
    for thisComponent in job_postingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "job_posting" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *job_description* updates
        
        # if job_description is starting this frame...
        if job_description.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            job_description.frameNStart = frameN  # exact frame index
            job_description.tStart = t  # local t and not account for scr refresh
            job_description.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(job_description, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'job_description.started')
            # update status
            job_description.status = STARTED
            job_description.setAutoDraw(True)
        
        # if job_description is active this frame...
        if job_description.status == STARTED:
            # update params
            pass
        
        # *job_posting_key_resp* updates
        waitOnFlip = False
        
        # if job_posting_key_resp is starting this frame...
        if job_posting_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            job_posting_key_resp.frameNStart = frameN  # exact frame index
            job_posting_key_resp.tStart = t  # local t and not account for scr refresh
            job_posting_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(job_posting_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'job_posting_key_resp.started')
            # update status
            job_posting_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(job_posting_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(job_posting_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if job_posting_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = job_posting_key_resp.getKeys(keyList=['space'], waitRelease=False)
            _job_posting_key_resp_allKeys.extend(theseKeys)
            if len(_job_posting_key_resp_allKeys):
                job_posting_key_resp.keys = _job_posting_key_resp_allKeys[-1].name  # just the last key pressed
                job_posting_key_resp.rt = _job_posting_key_resp_allKeys[-1].rt
                job_posting_key_resp.duration = _job_posting_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in job_postingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "job_posting" ---
    for thisComponent in job_postingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if job_posting_key_resp.keys in ['', [], None]:  # No response was made
        job_posting_key_resp.keys = None
    exp2_stimulus_loop.addData('job_posting_key_resp.keys',job_posting_key_resp.keys)
    if job_posting_key_resp.keys != None:  # we had a response
        exp2_stimulus_loop.addData('job_posting_key_resp.rt', job_posting_key_resp.rt)
        exp2_stimulus_loop.addData('job_posting_key_resp.duration', job_posting_key_resp.duration)
    # the Routine "job_posting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp2_stimulus" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_2.setImage(exp2_stim)
    # keep track of which components have finished
    exp2_stimulusComponents = [image_2, etRecord_2]
    for thisComponent in exp2_stimulusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp2_stimulus" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        
        # if image_2 is starting this frame...
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2.started')
            # update status
            image_2.status = STARTED
            image_2.setAutoDraw(True)
        
        # if image_2 is active this frame...
        if image_2.status == STARTED:
            # update params
            pass
        
        # if image_2 is stopping this frame...
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.stopped')
                # update status
                image_2.status = FINISHED
                image_2.setAutoDraw(False)
        # *etRecord_2* updates
        
        # if etRecord_2 is starting this frame...
        if etRecord_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_2.frameNStart = frameN  # exact frame index
            etRecord_2.tStart = t  # local t and not account for scr refresh
            etRecord_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_2.started', t)
            # update status
            etRecord_2.status = STARTED
        
        # if etRecord_2 is stopping this frame...
        if etRecord_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_2.tStop = t  # not accounting for scr refresh
                etRecord_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_2.stopped', t)
                # update status
                etRecord_2.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp2_stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp2_stimulus" ---
    for thisComponent in exp2_stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord_2.status != FINISHED:
        etRecord_2.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # --- Prepare to start Routine "question1" ---
    continueRoutine = True
    # update component parameters for each repeat
    candidate_rating.reset()
    # keep track of which components have finished
    question1Components = [candidate_rating_question, candidate_rating]
    for thisComponent in question1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *candidate_rating_question* updates
        
        # if candidate_rating_question is starting this frame...
        if candidate_rating_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            candidate_rating_question.frameNStart = frameN  # exact frame index
            candidate_rating_question.tStart = t  # local t and not account for scr refresh
            candidate_rating_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(candidate_rating_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'candidate_rating_question.started')
            # update status
            candidate_rating_question.status = STARTED
            candidate_rating_question.setAutoDraw(True)
        
        # if candidate_rating_question is active this frame...
        if candidate_rating_question.status == STARTED:
            # update params
            pass
        
        # *candidate_rating* updates
        
        # if candidate_rating is starting this frame...
        if candidate_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            candidate_rating.frameNStart = frameN  # exact frame index
            candidate_rating.tStart = t  # local t and not account for scr refresh
            candidate_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(candidate_rating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'candidate_rating.started')
            # update status
            candidate_rating.status = STARTED
            candidate_rating.setAutoDraw(True)
        
        # if candidate_rating is active this frame...
        if candidate_rating.status == STARTED:
            # update params
            pass
        
        # Check candidate_rating for response to end routine
        if candidate_rating.getRating() is not None and candidate_rating.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question1" ---
    for thisComponent in question1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp2_stimulus_loop.addData('candidate_rating.response', candidate_rating.getRating())
    exp2_stimulus_loop.addData('candidate_rating.rt', candidate_rating.getRT())
    # the Routine "question1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "question2" ---
    continueRoutine = True
    # update component parameters for each repeat
    image_clarity_rating.reset()
    # keep track of which components have finished
    question2Components = [image_clarity_question, image_clarity_rating]
    for thisComponent in question2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_clarity_question* updates
        
        # if image_clarity_question is starting this frame...
        if image_clarity_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_clarity_question.frameNStart = frameN  # exact frame index
            image_clarity_question.tStart = t  # local t and not account for scr refresh
            image_clarity_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_clarity_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_clarity_question.started')
            # update status
            image_clarity_question.status = STARTED
            image_clarity_question.setAutoDraw(True)
        
        # if image_clarity_question is active this frame...
        if image_clarity_question.status == STARTED:
            # update params
            pass
        
        # *image_clarity_rating* updates
        
        # if image_clarity_rating is starting this frame...
        if image_clarity_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_clarity_rating.frameNStart = frameN  # exact frame index
            image_clarity_rating.tStart = t  # local t and not account for scr refresh
            image_clarity_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_clarity_rating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_clarity_rating.started')
            # update status
            image_clarity_rating.status = STARTED
            image_clarity_rating.setAutoDraw(True)
        
        # if image_clarity_rating is active this frame...
        if image_clarity_rating.status == STARTED:
            # update params
            pass
        
        # Check image_clarity_rating for response to end routine
        if image_clarity_rating.getRating() is not None and image_clarity_rating.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question2" ---
    for thisComponent in question2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp2_stimulus_loop.addData('image_clarity_rating.response', image_clarity_rating.getRating())
    exp2_stimulus_loop.addData('image_clarity_rating.rt', image_clarity_rating.getRT())
    # the Routine "question2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "question3" ---
    continueRoutine = True
    # update component parameters for each repeat
    comprehension_rating.reset()
    # keep track of which components have finished
    question3Components = [comprehension_question, comprehension_rating]
    for thisComponent in question3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "question3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *comprehension_question* updates
        
        # if comprehension_question is starting this frame...
        if comprehension_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comprehension_question.frameNStart = frameN  # exact frame index
            comprehension_question.tStart = t  # local t and not account for scr refresh
            comprehension_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comprehension_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'comprehension_question.started')
            # update status
            comprehension_question.status = STARTED
            comprehension_question.setAutoDraw(True)
        
        # if comprehension_question is active this frame...
        if comprehension_question.status == STARTED:
            # update params
            pass
        
        # *comprehension_rating* updates
        
        # if comprehension_rating is starting this frame...
        if comprehension_rating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comprehension_rating.frameNStart = frameN  # exact frame index
            comprehension_rating.tStart = t  # local t and not account for scr refresh
            comprehension_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comprehension_rating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'comprehension_rating.started')
            # update status
            comprehension_rating.status = STARTED
            comprehension_rating.setAutoDraw(True)
        
        # if comprehension_rating is active this frame...
        if comprehension_rating.status == STARTED:
            # update params
            pass
        
        # Check comprehension_rating for response to end routine
        if comprehension_rating.getRating() is not None and comprehension_rating.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in question3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "question3" ---
    for thisComponent in question3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp2_stimulus_loop.addData('comprehension_rating.response', comprehension_rating.getRating())
    exp2_stimulus_loop.addData('comprehension_rating.rt', comprehension_rating.getRT())
    # the Routine "question3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'exp2_stimulus_loop'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
