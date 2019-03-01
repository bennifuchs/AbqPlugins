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


from abaqusGui import *
from kernelAccess import session


###########################################################################
# Class definition
###########################################################################

class viewManagerDB(AFXDataDialog):

    [
        ID_VIEW_LIST,
        ID_ADD_VIEW,
        ID_RENAME_VIEW,
        ID_DEL_VIEW,
        ID_SET_VIEW,
        ID_SAVE_VIEWS,
        ID_LOAD_VIEWS,
        ID_LAST
    ] = range(AFXDataDialog.ID_LAST, AFXDataDialog.ID_LAST+8)
    
    def __init__(self, form):

        # call base class's init method
        AFXDataDialog.__init__(self, mode=form, title="View Manager", 
                               actionButtonIds=self.DISMISS,
                               opts=DIALOG_NORMAL|DECOR_RESIZE)

        self.viewDict = {}
        self.storageFilename = AFXStringTarget(initialValue="")
        self.loadFilename = AFXStringTarget(initialValue="")
        
        # create horizontal frame for view list
        mainframe = FXHorizontalFrame(p=self, opts=LAYOUT_FILL_X | LAYOUT_FILL_Y)
        
        # create vertical frame for view list
        vvf = FXVerticalFrame(p=mainframe, opts=FRAME_SUNKEN | LAYOUT_FILL_X | LAYOUT_FILL_Y)
        # create view list in vertical frame
        self.viewList = AFXList(p=vvf, nvis=15, tgt=self, sel=self.ID_VIEW_LIST,
                       opts= LIST_SINGLESELECT | LAYOUT_FILL_X | LAYOUT_FILL_Y | AFXLIST_NO_AUTOCOMMIT)
        FXMAPFUNC(self, SEL_DOUBLECLICKED, self.ID_VIEW_LIST, viewManagerDB.onSetView)
        
        # create vertical frame for buttons
        vbf = FXVerticalFrame(p=mainframe, opts=LAYOUT_FILL_Y)
        
        # create group box
        modGroupBox = FXGroupBox(p=vbf, text='View Modifications', opts=LAYOUT_SIDE_LEFT|LAYOUT_FILL_X|FRAME_GROOVE)
        
        # create add view button
        addViewButton = FXButton(p=modGroupBox, text='Add View', ic=None, tgt=self, sel=self.ID_ADD_VIEW,
                      opts=BUTTON_NORMAL|LAYOUT_FILL_X)
        addViewButton.setDefault()
        # command map for button
        FXMAPFUNC(self, SEL_COMMAND, self.ID_ADD_VIEW, viewManagerDB.onAddView)

        # create rename view button
        renameViewButton = FXButton(p=modGroupBox, text='Rename View', ic=None, tgt=self, sel=self.ID_RENAME_VIEW,
                      opts=BUTTON_NORMAL|LAYOUT_FILL_X)
        # command map for button
        FXMAPFUNC(self, SEL_COMMAND, self.ID_RENAME_VIEW, viewManagerDB.onRenameView)
        
        # create delete view button
        delViewButton = FXButton(p=modGroupBox, text='Delete View', ic=None, tgt=self, sel=self.ID_DEL_VIEW,
                                 opts=BUTTON_NORMAL|LAYOUT_FILL_X)
        # command map for button
        FXMAPFUNC(self, SEL_COMMAND, self.ID_DEL_VIEW, viewManagerDB.onDelView)
        
        # create group box
        saveGroupBox = FXGroupBox(p=vbf, text='Save/Load Views', opts=LAYOUT_SIDE_LEFT|LAYOUT_FILL_X|FRAME_GROOVE)        
        
        # create save views to file button
        saveViewsButton = FXButton(p=saveGroupBox, text='Save Views', ic=None, tgt=self, sel=self.ID_SAVE_VIEWS,
                                 opts=BUTTON_NORMAL|LAYOUT_FILL_X)
        # command map for button
        FXMAPFUNC(self, SEL_COMMAND, self.ID_SAVE_VIEWS, viewManagerDB.onSaveViews)
        
        # create load saved views button
        loadViewsButton = FXButton(p=saveGroupBox, text='Load Views', ic=None, tgt=self, sel=self.ID_LOAD_VIEWS,
                                 opts=BUTTON_NORMAL|LAYOUT_FILL_X)
        # command map for button
        FXMAPFUNC(self, SEL_COMMAND, self.ID_LOAD_VIEWS, viewManagerDB.onLoadViews)
        
        # create group box
        saveGroupBox = FXGroupBox(p=vbf, text='', opts=LAYOUT_SIDE_LEFT|LAYOUT_FILL_X)        
        # create set view button
        setViewButton = FXButton(p=vbf, text='Set View', ic=None, tgt=self, sel=self.ID_SET_VIEW,
                                 opts=BUTTON_NORMAL|LAYOUT_FILL_X)
        # command map for button
        FXMAPFUNC(self, SEL_COMMAND, self.ID_SET_VIEW, viewManagerDB.onSetView)
        
         
    def onAddView(self, sender, sel, ptr):

        ViewDB = AddViewDB(self.viewList, self.viewDict)
        ViewDB.create()
        ViewDB.showModal()


    def onRenameView(self, sender, sel, ptr):

        RenameDB = RenameViewDB(self.viewList, self.viewDict)
        RenameDB.create()
        RenameDB.showModal()

    
    def onSetView(self, sender, sel, ptr):

        # get index of currently selected list item
        i = self.viewList.getSingleSelection()
        # check if index is valid
        if i > -1:
            # get name of item
            vname = self.viewList.getItemText(i)
            # get viewDict object corresponding to vname
            vo = self.viewDict[vname]
            # call set method
            vo.set()

        return 1


    def onDelView(self, sender, sel, ptr):
        
        # get index of currently selected list item
        i = self.viewList.getSingleSelection()
        # check if index is valid
        if i > -1:
            # get name of item
            vname = self.viewList.getItemText(i)
            # remove item from list
            self.viewList.removeItem(i)
#             remove corresponding viewdata object from dictionary
            del self.viewDict[vname]
        
        return 1
        
        
    def onSaveViews(self, sender, sel, ptr):
        
        saveDialog = SaveViewsDB(pathNameTgt=self.storageFilename, viewData=self.viewDict)
        saveDialog.create()
        saveDialog.showModal()
        

        
    def onLoadViews(self, sender, sel, ptr):
        
        loadDialog = LoadViewsDB(pathNameTgt=self.loadFilename, viewData=self.viewDict, viewList=self.viewList)
        loadDialog.create()
        loadDialog.showModal()
         
     
class AddViewDB(AFXDialog):
     
    def __init__(self, viewList, viewDict):
        
        # call base class's init method
        AFXDialog.__init__(self, title='Add View', 
                          actionButtonIds=self.OK|self.CANCEL)
        
        # create class members from passed in view list and view dictionary
        self.vl = viewList
        self.vDict = viewDict
        
        # get ok button
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        # set button text
        okBtn.setText('Add')
        # set button as default
        okBtn.setDefault()
        # create function map for button activation to class method
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CLICKED_OK, AddViewDB.onAdd)
         
        # create text field to enter view name
        self.textField = AFXTextField(p=self, ncols=10, labelText='View Name:')

    
    # method to be called upon add button activation    
    def onAdd(self, sender, sel, ptr):
        
        vName = self.textField.getText()
        
        # check if view name already exists
        i = self.vl.findItem(vName)
        if i == -1:
            # view name does not exist, thus, append name to view list
            self.vl.appendItem(vName)
        
            # create view data object
            vd = viewData(vName, i)
            
            # add current view settings to view data dictionary
            self.vDict.update({vName: vd})
        
            # hide dialog box
            self.hide()        

        else:
            showAFXErrorDialog(owner=self, message='View name already exists!')

        return 1


class RenameViewDB(AFXDialog):
     
    def __init__(self, viewList, viewDict):
        
        # call base class's init method
        AFXDialog.__init__(self, title='Add View', 
                          actionButtonIds=self.OK|self.CANCEL)
        
        # create class members from passed in view list and view dictionary
        self.vl = viewList
        self.vDict = viewDict
        
        # get ok button
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        # set button text
        okBtn.setText('Rename')
        # set button as default
        okBtn.setDefault()
        # create function map for button activation to class method
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CLICKED_OK, RenameViewDB.onRename)
         
        # create text field to enter view name
        self.textField = AFXTextField(p=self, ncols=10, labelText='View Name:')

    
    # method to be called upon add button activation    
    def onRename(self, sender, sel, ptr):

        getAFXApp().getAFXMainWindow().writeToMessageArea(
            'View dictionary keys before rename:\n'+str(self.vDict.keys()))

        
        # get new name str from text field 
        newName = self.textField.getText()
        
        # check if new name already exists in view list
        k = self.vl.findItem(newName)
        if k != -1:
            showAFXErrorDialog(owner=self, message='View name already exists!')
        else:
            # new name is unique in list, proceed
            
            # get index of currently selected view list item
            i = self.vl.getSingleSelection()
            # get old name str from currently selected item in view list
            oldName = self.vl.getItemText(i)
            # replace selected view list item with a new one containing the new name
            self.vl.replaceItem(i, newName)
                        
            # get view object associated with old view name in view data dictionary
            vd = self.vDict[oldName]
            # update view object's name
            vd.name = newName
            # delete entry associated with old name in view data dictionary
            del self.vDict[oldName]
            # create new entry in view data dictionary with new view name but old view data
            self.vDict.update({newName: vd})
            
            self.hide()
                    
            getAFXApp().getAFXMainWindow().writeToMessageArea(
                'View dictionary keys after rename:\n'+str(self.vDict.keys()))
                
        return 1


class SaveViewsDB(AFXDialog):
    
    # create IDs used in class
    [   
        ID_FILE_SELECTOR,
        ID_LAST
    ] = range(AFXDialog.ID_LAST, AFXDialog.ID_LAST+2)
    
    def __init__(self, pathNameTgt, viewData):

        # call base class's init method
        AFXDialog.__init__(self, title='Save View', 
                           actionButtonIds=self.OK|self.CANCEL,
                           opts=DIALOG_NORMAL|DECOR_RESIZE)
        
        # create class members from passed in path name target and view dictionary
        self.pathNameTgt = pathNameTgt
        self.viewDict = viewData
        
        # get ok button
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        # set button text
        okBtn.setText('Save')
        # set button as default
        okBtn.setDefault()
        # create function map for button activation to class method        
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CLICKED_OK, SaveViewsDB.onSave)
        
        Hf = FXHorizontalFrame(p=self, opts=LAYOUT_FILL_X)
        
        # create text field to enter file name
        self.textField = AFXTextField(p=Hf, ncols=15, labelText='File Path:', tgt=self.pathNameTgt, opts=LAYOUT_FILL_X)
        
        # create file selection button next to text field
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL)
        FXButton(p=Hf, text='\tSelect File\nFrom Dialog', ic=icon, tgt=self, sel=self.ID_FILE_SELECTOR)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_FILE_SELECTOR, SaveViewsDB.onSelectFile)

        
    def onSave(self, sender, sel, ptr):
        import pickle

        # open file for writing
        fname = self.pathNameTgt.getValue()
        if len(fname) == 0:
            showAFXErrorDialog(owner=self, message='Invalid Filename!')
        else:
            if not fname.endswith('.pkl'):
                fname+='.pkl'
            vDatabase = open(fname, 'wb')
            # store view dictionary
            pickle.dump(self.viewDict, vDatabase)
            # close file
            vDatabase.close()
    
            getAFXApp().getAFXMainWindow().writeToMessageArea('View settings written to file %s' % fname)
            
            self.hide()

        return 1


    def onSelectFile(self, sender, sel, ptr):

#         fileDialog = AFXFileSelectorDialog(owner=self, 
#                                            title='Select File',
#                                            pathNameTgt=self.pathNameTgt,
#                                            readOnlyKw=None,
#                                            patterns='*.pkl')
        fileDialog = CustomFileSelectorDB(owner=self, 
                                           title='Select File',
                                           pathNameTgt=self.pathNameTgt,
                                           readOnlyKw=None,
                                           patterns='*.pkl')
        fileDialog.create()
        fileDialog.showModal()
        
 
class LoadViewsDB(AFXDialog):

    [   
        ID_FILE_SELECTOR,
        ID_LAST
    ] = range(AFXDialog.ID_LAST, AFXDialog.ID_LAST+2)
    
    def __init__(self, pathNameTgt, viewData, viewList):

        # call base class's init method
        AFXDialog.__init__(self, title='Load View', 
                           actionButtonIds=self.OK|self.CANCEL,
                           opts=DIALOG_NORMAL|DECOR_RESIZE)
        
        self.pathNameTgt = pathNameTgt
        self.viewDict = viewData
        self.viewList = viewList
        
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('Load')
        okBtn.setDefault()
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CLICKED_OK, LoadViewsDB.onLoad)
        
        Hf = FXHorizontalFrame(p=self, opts=LAYOUT_FILL_X)
        
        self.textField = AFXTextField(p=Hf, ncols=15, labelText='File Path:', tgt=self.pathNameTgt, opts=LAYOUT_FILL_X)
        
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL)
        FXButton(p=Hf, text='\tSelect File\nFrom Dialog', ic=icon, tgt=self, sel=self.ID_FILE_SELECTOR)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_FILE_SELECTOR, LoadViewsDB.onSelectFile)

        
    def onLoad(self, sender, sel, ptr):
        import pickle
        
        # open file for reading
        fname = self.pathNameTgt.getValue()
        if not fname.endswith('.pkl'):
            fname+='.pkl'

        vDatabase = open(fname, 'rb')
        # get stored view dictionary from file
        importViewDict = pickle.load(vDatabase)
        # close file
        vDatabase.close()
        
        # update view dictionary with new values
        self.viewDict.update(importViewDict)
        
        # loop through loaded view names
        for vName in importViewDict.keys():
            
            # get index of item in view list corresponding to the imported view name
            i = self.viewList.findItem(vName)
            if i == -1:
                # new view name, append to view list
                self.viewList.appendItem(vName)

            # update index of the corresponding object in view dictionary
            self.viewDict[vName].index = self.viewList.findItem(vName)
                    
#         getAFXApp().getAFXMainWindow().writeToMessageArea(
#             'Load Views button functionality not implemented yet!')
        
        self.hide()
        return 1


    def onSelectFile(self, sender, sel, ptr):

        fileDialog = AFXFileSelectorDialog(owner=self, 
                                           title='Select File',
                                           pathNameTgt=self.pathNameTgt,
                                           readOnlyKw=None,
                                           mode=AFXSELECTFILE_EXISTING,
                                           patterns='*.pkl')
        fileDialog.create()
        fileDialog.showModal()
       
        
class CustomFileSelectorDB(AFXFileSelectorDialog):
    # customized version of the AFXFileSelectorDialog
    # adds filename ending to path name target before hiding the dialog box
    
    
    def __init__(self, owner, title, pathNameTgt, readOnlyKw=None, mode=AFXSELECTFILE_ANY, patterns='*', patternIndexTarget=None):
        
        # create class member of passed in path name target
        self.pathNameTgt = pathNameTgt
        
        # call base class's init method
        AFXFileSelectorDialog.__init__(self, owner, title, pathNameTgt, readOnlyKw, mode, patterns, patternIndexTarget)
        
    def hide(self):
        
        # get path str
        path = self.pathNameTgt.getValue()
        # check if path contains filename ending .pkl
        # and add it if necessary
        if not path.endswith('.pkl'):
            path+='.pkl'
            self.pathNameTgt.setValue(path)
        
        # call base class's hide method
        AFXFileSelectorDialog.hide(self)

class viewData():
    
    def __init__(self, name, index):
        
        self.name = name
        self.index = index
        tmp = self.getCurrentViewValues()
        self.cameraPosition = tmp['cameraPosition']
        self.cameraTarget = tmp['camerTarget']
        self.cameraUpVector = tmp['cameraUpVector']
        self.farPlane = tmp['farPlane']
        self.farPlaneMode = tmp['farPlaneMode']
        self.nearPlane = tmp['nearPlane']
        self.fieldOfViewAngle = tmp['fieldOfViewAngle']
        self.height = tmp['height']
        self.width = tmp['width']
        self.projection = tmp['projection']
        self.movieMode = tmp['movieMode']
        self.viewOffsetX = tmp['viewOffsetX']
        self.viewOffsetY = tmp['viewOffsetY']
    

    def getCurrentViewValues(self):

        vp = session.viewports[session.currentViewportName]
        return {'cameraPosition': vp.view.cameraPosition,
                'camerTarget': vp.view.cameraTarget,
                'cameraUpVector': vp.view.cameraUpVector,
                'farPlane': vp.view.farPlane,
                'farPlaneMode': vp.view.farPlaneMode,
                'nearPlane': vp.view.nearPlane,
                'fieldOfViewAngle': vp.view.fieldOfViewAngle,
                'height': vp.view.height,
                'width': vp.view.width,
                'projection': vp.view.projection,
                'movieMode': vp.view.movieMode,
                'viewOffsetX': vp.view.viewOffsetX,
                'viewOffsetY': vp.view.viewOffsetY}
   
    def set(self):

        vps = session.viewports
        vpNames = vps.keys()

        for name in vpNames:
            vps[name].view.setValues(cameraPosition=self.cameraPosition, cameraTarget=self.cameraTarget, cameraUpVector=self.cameraUpVector,
                                     farPlane=self.farPlane, farPlaneMode=self.farPlaneMode, nearPlane=self.nearPlane,
                                     height=self.height, width=self.width,
                                     projection=self.projection, movieMode=self.movieMode,
                                     viewOffsetX=self.viewOffsetX, viewOffsetY=self.viewOffsetY)

