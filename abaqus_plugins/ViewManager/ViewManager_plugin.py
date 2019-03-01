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
# Note: The above form of the import statement is used for the prototype
# application to allow the module to be reloaded while the application is
# still running. In a non-prototype application you would use the form:
# from myDB import MyDB


###########################################################################
# Class definition
###########################################################################

class viewManagerForm(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):

        AFXForm.__init__(self, owner)
                

    def getFirstDialog(self):

        import ViewManagerDB
        reload(ViewManagerDB)
        return ViewManagerDB.viewManagerDB(self)

###########################################################################
# Register abaqus plugin
###########################################################################
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

toolset.registerGuiMenuButton(
        buttonText='My Utils|View Manager', 
        object=viewManagerForm(toolset),
#         kernelInitString='import viewSave; viewSave.init()',
        author='Benjamin Fuchs',
#         version=__version__,
        applicableModules=['Visualization'],
        description='Store and retrieve custom viewport views.')
