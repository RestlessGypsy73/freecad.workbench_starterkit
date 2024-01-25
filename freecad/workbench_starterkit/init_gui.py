import os
import FreeCADGui as Gui
import FreeCAD as App
from TranslateUtils import translate
from freecad.workbench_starterkit import ICONPATH, TRANSLATIONSPATH


class AISCWorkbench(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """
    MenuText = translate("starterkit", "AISC Workbench")
    ToolTip = translate("starterkit", "A workbench to design using AISC Structual Steel")
    Icon = os.path.join(ICONPATH, "template_resource.svg")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        # Add translations path
        Gui.addLanguagePath(TRANSLATIONSPATH)
        Gui.updateLocale()

        from freecad.workbench_starterkit import my_numpy_function
        App.Console.PrintMessage(translate("Console",
            "Switching to the AISC Workbench") + "\n")
        App.Console.PrintMessage(translate("Console", "Run a numpy function:") \
            + "sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar(translate("Toolbar", "Tools"), self.toolbox)
        self.appendMenu(translate("Menu", "Tools"), self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench(TemplateWorkbench())
