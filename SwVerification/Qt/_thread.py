from PySide6.QtCore import QThread


class TaskThread(QThread):
    """ Main Function Thread(parent:QThread) """
    def __init__(self, task_model):
        super().__init__()
        self._task = task_model

    def run(self):
        self._task.run()

    def stop(self):
        self._task.stop()
        self.terminate()
        self.wait(2)
