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
# toolset.registerKernelToolButton(toolboxName='My Utils',
#                                  buttonText='\tActivate Legend', icon=vpIcon,
#                                  moduleName='myUtils', functionName='activateLegend()')
#                                 
# # add legend deactivation button to my utils toolbox
# toolset.registerKernelToolButton(toolboxName='My Utils',
#                                  buttonText='\tDeactivate Legend', icon=vpIcon,
#                                  moduleName='myUtils', functionName='deactivateLegend()')

# ===========================================================
# MENU ENTRY REGISTER COMMANDS
# ===========================================================

# ADDITIONAL ITEMS DISPLAY COMMANDS
# ---------------------------------
								 
# add legend activation entry to my utils submenu 
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Activate Legend',
                                 moduleName='myUtils', functionName='activateLegend()')

# add legend deactivation entry to my utils submenu 
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Deactivate Legend',
                                 moduleName='myUtils', functionName='deactivateLegend()')

# add triad activation entry to my utils submenu 
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Activate Triad',
                                 moduleName='myUtils', functionName='activateTriad()')

# add triad deactivation entry to my utils submenu 
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Deactivate Triad',
                                 moduleName='myUtils', functionName='deactivateTriad()')
                                 
# add mesh showing entry to my utils submenu 
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Show Mesh',
                                 moduleName='myUtils', functionName='showMesh()')

# add mesh hiding entry to my utils submenu 
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Hide Mesh',
                                 moduleName='myUtils', functionName='hideMesh()')

# add session coordinate system showing entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Show Session Csys',
								moduleName='myUtils', functionName='showSessionCsys()')


# add session coordinate system hiding entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Display Utils|Hide Session Csys',
								moduleName='myUtils', functionName='hideSessionCsys()')

								 
# ADDITIONAL STANDARD VIEW COMMANDS
# ---------------------------------
								 
# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Xpos-Yneg View',
                                 moduleName='myUtils', functionName='setViewXposYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Xneg-Yneg View',
                                 moduleName='myUtils', functionName='setViewXnegYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Xneg-Zneg View',
                                 moduleName='myUtils', functionName='setViewXnegZneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Xneg-Zpos View',
                                 moduleName='myUtils', functionName='setViewXnegZpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Zpos-Yneg View',
                                 moduleName='myUtils', functionName='setViewZposYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Zneg-Yneg View',
                                 moduleName='myUtils', functionName='setViewZnegYneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Ypos-Zneg View',
                                 moduleName='myUtils', functionName='setViewYposZneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Ypos-Zpos View',
                                 moduleName='myUtils', functionName='setViewYposZpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Yneg-Zneg View',
                                 moduleName='myUtils', functionName='setViewYnegZneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Yneg-Zpos View',
                                 moduleName='myUtils', functionName='setViewYnegZpos()')
								 
# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Ypos-Xpos View',
                                 moduleName='myUtils', functionName='setViewYposXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Yneg-Xpos View',
                                 moduleName='myUtils', functionName='setViewYnegXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Yneg-Xneg View',
                                 moduleName='myUtils', functionName='setViewYnegXneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Ypos-Xneg View',
                                 moduleName='myUtils', functionName='setViewYposXneg()')
								 
# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Zpos-Xpos View',
                                 moduleName='myUtils', functionName='setViewZposXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Zneg-Xpos View',
                                 moduleName='myUtils', functionName='setViewZnegXpos()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Zneg-Xneg View',
                                 moduleName='myUtils', functionName='setViewZnegXneg()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Zpos-Xneg View',
                                 moduleName='myUtils', functionName='setViewZposXneg()')
								

# ADDITIONAL STANDARD VIEW COMMANDS
# ---------------------------------

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Xpos-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewXposYpos_userCsys()')
								
# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Xneg-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewXnegYpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Xpos-Zneg View',
                                 moduleName='ViewUtils', functionName='setViewXposZneg_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Xpos-Zpos View',
                                 moduleName='ViewUtils', functionName='setViewXposZpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Zpos-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewZposYpos_userCsys()')

# add further standard view entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Zneg-Ypos View',
                                 moduleName='ViewUtils', functionName='setViewZnegYpos_userCsys()')


								
# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Rotate view about screen x-axis (+)',
                                 moduleName='ViewUtils', functionName='rotateViewXaxisScreen_pos()',)
								
# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Rotate view about screen y-axis (+)',
                                 moduleName='ViewUtils', functionName='rotateViewYaxisScreen_pos()')

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Rotate view about screen z-axis (+)',
                                 moduleName='ViewUtils', functionName='rotateViewZaxisScreen_pos()')
								
# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Rotate view about screen x-axis (-)',
                                 moduleName='ViewUtils', functionName='rotateViewXaxisScreen_neg()')
								
# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Rotate view about screen y-axis (-)',
                                 moduleName='ViewUtils', functionName='rotateViewYaxisScreen_neg()')

# add rotate view by constant angle entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|View User-Csys|Rotate view about screen z-axis (-)',
                                 moduleName='ViewUtils', functionName='rotateViewZaxisScreen_neg()')
								
								
                                
# ADDITIONAL ANNOTATIONS RELATED COMMANDS
# ---------------------------------------

# add delete all annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Annotations|Delete All Annotations',
                                 moduleName='myUtils', functionName='removeAnnotations()')
								
# add hide all annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Annotations|Hide All Annotations',
                                 moduleName='myUtils', functionName='hideAnnotations()')
								
# add show all annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Annotations|Show All Annotations',
                                 moduleName='myUtils', functionName='showAnnotations()')
								
# add green annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Annotations|Green Annotations',
                                 moduleName='myUtils', functionName='greenAnnotations()')
                                
# add red annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Annotations|Red Annotations',
                                 moduleName='myUtils', functionName='redAnnotations()')
								
# add grey annotations entry to my utils submenu
toolset.registerKernelMenuButton(buttonText='My Utils|Annotations|Grey Annotations',
                                 moduleName='myUtils', functionName='greyAnnotations()')
								
								
								
								
								
