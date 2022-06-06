from PyQt6.QtWidgets import QCheckBox, QRadioButton, QSpinBox, QDoubleSpinBox
from json import JSONDecodeError
import json
import os


json_file_name = "WidgetStates.json"


class StateSavingFileOps:

    def __init__(self):
        # If file does not exist create it
        if not os.path.exists(json_file_name):
            open(json_file_name, "x")

    # Define as singleton so only 1 instance can be created
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(StateSavingFileOps, cls).__new__(cls)
        return cls.instance

    """
    Check if the file contains the item, if it does, retrieve the state.
    """
    @staticmethod
    def get_state(item):
        if os.path.exists(json_file_name):
            try:
                f = json.loads(open(json_file_name).read())
                if item in f.keys():
                    return f[item]
                else:
                    return False
            except JSONDecodeError:
                return False
        else:
            return False

    """
    Save the state of the item in the file.
    Since we are using a dict, the keys are unique, 
    so it does not matter what the old state is, or if it exists.
    """
    @staticmethod
    def save_state(item, state):
        if os.path.exists(json_file_name):
            try:
                f = json.loads(open(json_file_name).read())
            except JSONDecodeError:
                f = {}
            f[item] = state
            with open(json_file_name, "w+") as file:
                file.write(json.dumps(f, indent=1))


class StateSavingQCheckBox(QCheckBox):
    """
    QCheckBox that remembers if it was checked or not.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = StateSavingFileOps()
        self.objectNameChanged.connect(lambda x: self.setChecked(self.state.get_state(self.objectName())))
        self.stateChanged.connect(lambda x: self.state.save_state(item=self.objectName(), state=self.isChecked()))


class StateSavingQRadioButton(QRadioButton):
    """
    QRadioButton that remembers if it was checked or not.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = StateSavingFileOps()
        self.objectNameChanged.connect(lambda x: self.setChecked(self.state.get_state(self.objectName())))
        self.toggled.connect(lambda x: self.state.save_state(item=self.objectName(), state=self.isChecked()))


class StateSavingQSpinBox(QSpinBox):
    """
    QSpinBox that remembers the last value it was set on.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = StateSavingFileOps()
        self.objectNameChanged.connect(lambda x: self.setValue(self.state.get_state(self.objectName())))
        self.valueChanged.connect(lambda x: self.state.save_state(item=self.objectName(), state=self.value()))


class StateSavingQDoubleSpinBox(QDoubleSpinBox):
    """
    QSpinBox that remembers the last value it was set on.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = StateSavingFileOps()
        self.objectNameChanged.connect(lambda x: self.setValue(self.state.get_state(self.objectName())))
        self.valueChanged.connect(lambda x: self.state.save_state(item=self.objectName(), state=self.value()))
