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


def printCurrentVp():
    
    from abaqus import session, getInputs
    from abaqusConstants import PNG
    name = getInputs( (('File name:', ''),),
                      'Print current viewport to PNG file')[0]
    vp = session.viewports[session.currentViewportName]
    session.printToFile(fileName=name, format=PNG, canvasObjects=(vp,))

    
def activateLegend():
    
    session.viewports[session.currentViewportName].viewportAnnotationOptions.setValues(legend=ON)

    
def deactivateLegend():
    
    session.viewports[session.currentViewportName].viewportAnnotationOptions.setValues(legend=OFF)


def activateTriad():
    
    session.viewports[session.currentViewportName].viewportAnnotationOptions.setValues(triad=ON)


def deactivateTriad():
    
    session.viewports[session.currentViewportName].viewportAnnotationOptions.setValues(triad=OFF)


def showMesh():
    
    session.viewports[session.currentViewportName].odbDisplay.commonOptions.setValues(visibleEdges=EXTERIOR)
    
    
def hideMesh():
    
    session.viewports[session.currentViewportName].odbDisplay.commonOptions.setValues(visibleEdges=FEATURE)

	
def showSessionCsys():
	
	curVP = session.currentViewportName
	session.viewports[curVP].odbDisplay.basicOptions.setValues(scratchCoordSystemDisplay=ON)
	

def hideSessionCsys():
	
	curVP = session.currentViewportName
	session.viewports[curVP].odbDisplay.basicOptions.setValues(scratchCoordSystemDisplay=OFF)
	
	
def setViewXposYneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,0.,-1.),cameraUpVector=(0.,-1.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)

	
def setViewXnegYneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,0.,1.),cameraUpVector=(0.,-1.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)

	
def setViewXnegZneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,-1.,0.),cameraUpVector=(0.,0.,-1.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)

	
def setViewXnegZpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,1.,0.),cameraUpVector=(0.,0.,1.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)

	
def setViewZposYneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(1.,0.,0.),cameraUpVector=(0.,-1.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)


def setViewZnegYneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(-1.,0.,0.),cameraUpVector=(0.,-1.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYposZneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(-1.,0.,0.),cameraUpVector=(0.,0.,-1.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYposZpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(1.,0.,0.),cameraUpVector=(0.,0.,1.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYnegZneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(1.,0.,0.),cameraUpVector=(0.,0.,-1.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYnegZpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(-1.,0.,0.),cameraUpVector=(0.,0.,1.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)

	
def setViewYposXpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,0.,-1.),cameraUpVector=(1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYnegXpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,0.,1.),cameraUpVector=(1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYnegXneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,0.,-1.),cameraUpVector=(-1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewYposXneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,0.,1.),cameraUpVector=(-1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)

	
def setViewZposXpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,1.,0.),cameraUpVector=(1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewZnegXpos():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,-1.,0.),cameraUpVector=(1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewZnegXneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,1.,0.),cameraUpVector=(-1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	
	
def setViewZposXneg():

    session.viewports[session.currentViewportName].view.setValues(cameraTarget=(0.,0.,0.), cameraPosition=(0.,-1.,0.),cameraUpVector=(-1.,0.,0.))
    session.viewports[session.currentViewportName].view.fitView(drawImmediately=True)
	

def removeAnnotations():
    
    cVp = session.viewports[session.currentViewportName]
    cOdb = cVp.displayedObject
    annotationNames = cOdb.userData.annotations.keys()
    
    for name in annotationNames:
        del cOdb.userData.annotations[name]
    

def hideAnnotations():
    
    cVp = session.viewports[session.currentViewportName]    
    del cVp.annotationsToPlot[:]
	

def showAnnotations():
    	
    cVp = session.viewports[session.currentViewportName]
    cOdb = cVp.displayedObject
    annotationNames = cOdb.userData.annotations.keys()
	
    for name in annotationNames:
        a = cOdb.userData.annotations[name]
        cVp.plotAnnotation(annotation=a)
	

def greenAnnotations():
    
    cVp = session.viewports[session.currentViewportName]
    cOdb = cVp.displayedObject
    annotationNames = cOdb.userData.annotations.keys()
    
    for name in annotationNames:
        
        if hasattr(cOdb.userData.annotations[name], 'text'):
            cOdb.userData.annotations[name].setValues(backgroundColor='#99FF99')
	

def redAnnotations():
    
    cVp = session.viewports[session.currentViewportName]
    cOdb = cVp.displayedObject
    annotationNames = cOdb.userData.annotations.keys()
    
    for name in annotationNames:
        
        if hasattr(cOdb.userData.annotations[name], 'text'):
            cOdb.userData.annotations[name].setValues(backgroundColor='#FF8181')
	

def greyAnnotations():
    
    cVp = session.viewports[session.currentViewportName]
    cOdb = cVp.displayedObject
    annotationNames = cOdb.userData.annotations.keys()
    
    for name in annotationNames:
        
        if hasattr(cOdb.userData.annotations[name], 'text'):
            cOdb.userData.annotations[name].setValues(backgroundColor='#CECECE')
	
	
