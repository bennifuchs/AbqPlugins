'''
MIT License

Copyright (c) 2019 Benjamin Fuchs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from abaqus import *
from abaqusConstants import *


def setViewXposYpos_userCsys():    
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    
    # get name of displayed Odb in current viewport
    OdbName = curVp.displayedObject.name   
    
    # get scratch Odb
    scrOdb = session.scratchOdbs[OdbName]
    
    # get user coordinate system
    userCsys = scrOdb.rootAssembly.datumCsyses['CSYS-1']
    
    # get current view in viewport 1
    sessView = curVp.view
    
    # align current view with user coordinate system axis
    sessView.setValues(cameraTarget=userCsys.origin, cameraPosition=userCsys.origin+userCsys.zAxis, cameraUpVector=userCsys.yAxis)
    
    sessView.fitView()


def setViewXnegYpos_userCsys():
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    
    # get name of displayed Odb in current viewport
    OdbName = curVp.displayedObject.name   
    
    # get scratch Odb
    scrOdb = session.scratchOdbs[OdbName]
    
    # get user coordinate system
    userCsys = scrOdb.rootAssembly.datumCsyses['CSYS-1']
    
    # get current view in viewport 1
    sessView = curVp.view
    
    # align current view with user coordinate system axis
    sessView.setValues(cameraTarget=userCsys.origin, cameraPosition=userCsys.origin-userCsys.zAxis, cameraUpVector=userCsys.yAxis)
    
    sessView.fitView()


def setViewXposZneg_userCsys():
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    
    # get name of displayed Odb in current viewport
    OdbName = curVp.displayedObject.name   
    
    # get scratch Odb
    scrOdb = session.scratchOdbs[OdbName]

    # get user coordinate system
    userCsys = scrOdb.rootAssembly.datumCsyses['CSYS-1']

    # get current view in viewport 1
    sessView = curVp.view

    # align current view with user coordinate system axis
    sessView.setValues(cameraTarget=userCsys.origin, cameraPosition=userCsys.origin+userCsys.yAxis, cameraUpVector=-userCsys.zAxis)

    sessView.fitView()


def setViewXposZpos_userCsys():
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    
    # get name of displayed Odb in current viewport
    OdbName = curVp.displayedObject.name   
    
    # get scratch Odb
    scrOdb = session.scratchOdbs[OdbName]

    # get user coordinate system
    userCsys = scrOdb.rootAssembly.datumCsyses['CSYS-1']

    # get current view in viewport 1
    sessView = curVp.view

    # align current view with user coordinate system axis
    sessView.setValues(cameraTarget=userCsys.origin, cameraPosition=userCsys.origin-userCsys.yAxis, cameraUpVector=userCsys.zAxis)

    sessView.fitView()


def setViewZposYpos_userCsys():
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    
    # get name of displayed Odb in current viewport
    OdbName = curVp.displayedObject.name   
    
    # get scratch Odb
    scrOdb = session.scratchOdbs[OdbName]

    # get user coordinate system
    userCsys = scrOdb.rootAssembly.datumCsyses['CSYS-1']

    # get current view in viewport 1
    sessView = curVp.view

    # align current view with user coordinate system axis
    sessView.setValues(cameraTarget=userCsys.origin, cameraPosition=userCsys.origin-userCsys.xAxis, cameraUpVector=userCsys.yAxis)

    sessView.fitView()


def setViewZnegYpos_userCsys():
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    
    # get name of displayed Odb in current viewport
    OdbName = curVp.displayedObject.name   
    
    # get scratch Odb
    scrOdb = session.scratchOdbs[OdbName]

    # get user coordinate system
    userCsys = scrOdb.rootAssembly.datumCsyses['CSYS-1']

    # get current view in viewport 1
    sessView = curVp.view

    # align current view with user coordinate system axis
    sessView.setValues(cameraTarget=userCsys.origin, cameraPosition=userCsys.origin+userCsys.xAxis, cameraUpVector=userCsys.yAxis)

    sessView.fitView()


def rotateViewXaxisScreen_pos():

#     get current viewport
#    curVp = session.viewports[session.currentViewportName]    
#    # get current view in viewport 1
#    sessView = curVp.view
#    # rotate view about horizontal screen axis
#    sessView.rotate(xAngle=22.5, mode=SCREEN)
    rotateViewAxisScreen(22.5, 'xAngle')


def rotateViewXaxisScreen_neg():
    rotateViewAxisScreen(-22.5, 'xAngle')


def rotateViewYaxisScreen_pos():    
    rotateViewAxisScreen(22.5, 'yAngle')


def rotateViewYaxisScreen_neg():    
    rotateViewAxisScreen(-22.5, 'yAngle')


def rotateViewZaxisScreen_pos():    
    rotateViewAxisScreen(22.5, 'zAngle')


def rotateViewZaxisScreen_neg():    
    rotateViewAxisScreen(-22.5, 'zAngle')


def rotateViewAxisScreen(angle, axis):
    
    # get current viewport
    curVp = session.viewports[session.currentViewportName]    
    # get current view in viewport 1
    sessView = curVp.view
    # rotate view about horizontal screen axis
#    sessView.rotate(xAngle=22.5, mode=SCREEN)
    sessView.rotate(**{axis:angle, 'mode':SCREEN})