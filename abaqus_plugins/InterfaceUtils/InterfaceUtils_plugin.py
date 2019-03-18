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


from abaqusGui import getAFXApp, FXXPMIcon, afxCreateIcon
#from myIcons import vpIconData
#vpIcon = FXXXPMIcon(getAFXApp(), vpIconData)

# # create icon from png file
# vpIcon = afxCreateIcon('testIcon.png')

# get plugin toolset
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

# ===========================================================
# TOOLBOX REGISTER COMMANDS
# ===========================================================

# # add legend activation button to my utils toolbox
# toolset.registerKernelToolButton(toolboxName='Interface Utilities',
#                                  buttonText='\tActivate Legend', icon=vpIcon,
#                                  moduleName='InterfaceUtils', functionName='activateLegend()')
#
# # add legend deactivation button to my utils toolbox
# toolset.registerKernelToolButton(toolboxName='Interface Utilities',
#                                  buttonText='\tDeactivate Legend', icon=vpIcon,
#                                  moduleName='InterfaceUtils', functionName='deactivateLegend()')

# ===========================================================
# MENU ENTRY REGISTER COMMANDS
# ===========================================================

# ADDITIONAL ITEMS DISPLAY COMMANDS
# ---------------------------------

# add legend activation entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Activate Legend',
                                 moduleName='InterfaceUtils', functionName='activateLegend()')

# add legend deactivation entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Deactivate Legend',
                                 moduleName='InterfaceUtils', functionName='deactivateLegend()')

# add triad activation entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Activate Triad',
                                 moduleName='InterfaceUtils', functionName='activateTriad()')

# add triad deactivation entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Deactivate Triad',
                                 moduleName='InterfaceUtils', functionName='deactivateTriad()')

# add mesh showing entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Show Mesh',
                                 moduleName='InterfaceUtils', functionName='showMesh()')

# add mesh hiding entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Hide Mesh',
                                 moduleName='InterfaceUtils', functionName='hideMesh()')

# add session coordinate system showing entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Show Session Csys',
								moduleName='InterfaceUtils', functionName='showSessionCsys()')


# add session coordinate system hiding entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Display Utilities|Hide Session Csys',
								moduleName='InterfaceUtils', functionName='hideSessionCsys()')


# ADDITIONAL STANDARD VIEW COMMANDS
# ---------------------------------

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Xpos-Yneg View',
                                 moduleName='InterfaceUtils', functionName='setViewXposYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Xneg-Yneg View',
                                 moduleName='InterfaceUtils', functionName='setViewXnegYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Xneg-Zneg View',
                                 moduleName='InterfaceUtils', functionName='setViewXnegZneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Xneg-Zpos View',
                                 moduleName='InterfaceUtils', functionName='setViewXnegZpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Zpos-Yneg View',
                                 moduleName='InterfaceUtils', functionName='setViewZposYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Zneg-Yneg View',
                                 moduleName='InterfaceUtils', functionName='setViewZnegYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Ypos-Zneg View',
                                 moduleName='InterfaceUtils', functionName='setViewYposZneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Ypos-Zpos View',
                                 moduleName='InterfaceUtils', functionName='setViewYposZpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Yneg-Zneg View',
                                 moduleName='InterfaceUtils', functionName='setViewYnegZneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Yneg-Zpos View',
                                 moduleName='InterfaceUtils', functionName='setViewYnegZpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Ypos-Xpos View',
                                 moduleName='InterfaceUtils', functionName='setViewYposXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Yneg-Xpos View',
                                 moduleName='InterfaceUtils', functionName='setViewYnegXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Yneg-Xneg View',
                                 moduleName='InterfaceUtils', functionName='setViewYnegXneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Ypos-Xneg View',
                                 moduleName='InterfaceUtils', functionName='setViewYposXneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Zpos-Xpos View',
                                 moduleName='InterfaceUtils', functionName='setViewZposXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Zneg-Xpos View',
                                 moduleName='InterfaceUtils', functionName='setViewZnegXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Zneg-Xneg View',
                                 moduleName='InterfaceUtils', functionName='setViewZnegXneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Zpos-Xneg View',
                                 moduleName='InterfaceUtils', functionName='setViewZposXneg()')


# ADDITIONAL STANDARD VIEW COMMANDS
# ---------------------------------

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|User-Csys|Xpos-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewXposYpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|User-Csys|Xneg-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewXnegYpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|User-Csys|Xpos-Zneg View',
                                 moduleName='ViewUtils', functionName='setViewXposZneg_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|User-Csys|Xpos-Zpos View',
                                 moduleName='ViewUtils', functionName='setViewXposZpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|User-Csys|Zpos-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewZposYpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|User-Csys|Zneg-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewZnegYpos_userCsys()')



# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Rotate view about screen x-axis (+)',
                                 moduleName='ViewUtils', functionName='rotateViewXaxisScreen_pos()',)

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Rotate view about screen y-axis (+)',
                                 moduleName='ViewUtils', functionName='rotateViewYaxisScreen_pos()')

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Rotate view about screen z-axis (+)',
                                 moduleName='ViewUtils', functionName='rotateViewZaxisScreen_pos()')

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Rotate view about screen x-axis (-)',
                                 moduleName='ViewUtils', functionName='rotateViewXaxisScreen_neg()')

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Rotate view about screen y-axis (-)',
                                 moduleName='ViewUtils', functionName='rotateViewYaxisScreen_neg()')

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Views|Rotate view about screen z-axis (-)',
                                 moduleName='ViewUtils', functionName='rotateViewZaxisScreen_neg()')



# ADDITIONAL ANNOTATIONS RELATED COMMANDS
# ---------------------------------------

# add delete all annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Annotations|Delete All Annotations',
                                 moduleName='InterfaceUtils', functionName='removeAnnotations()')

# add hide all annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Annotations|Hide All Annotations',
                                 moduleName='InterfaceUtils', functionName='hideAnnotations()')

# add show all annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Annotations|Show All Annotations',
                                 moduleName='InterfaceUtils', functionName='showAnnotations()')

# add green annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Annotations|Green Annotations',
                                 moduleName='InterfaceUtils', functionName='greenAnnotations()')

# add red annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Annotations|Red Annotations',
                                 moduleName='InterfaceUtils', functionName='redAnnotations()')

# add grey annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='Interface Utilities|Annotations|Grey Annotations',
                                 moduleName='InterfaceUtils', functionName='greyAnnotations()')
