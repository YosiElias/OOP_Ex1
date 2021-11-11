import sys

class Calls:

    def __init__(self, arrive_time: float = None, src: int = None, dest: int =None):
        self._arrive_time = arrive_time
        self._src = src
        self._dest = dest
        self._dst_time = sys.maxsize
        self._src_time = sys.maxsize
        if src < dest:
            self._dirc = "UP"
        else:
            self._dirc = "DOWN"

    def alcate(self, src_time:float=None, dst_time:float=None, id:str=None):
        """
        :return: void. update value of call to is alocate
        """
        self.add_src_time(src_time)
        self.add_dst_time(dst_time)
        self._alocateTo = id


    def add_src_time(self, time:float=None):
        self._src_time = time


    def add_dst_time(self, time:float=None):
        self._dst_time = time

    def get_dirc(self) -> str:
        return self._dirc
    def get_time_arrive(self)-> float:
        return self._arrive_time
    def get_time_src(self)-> float:
        return self._src_time
    def get_time_dst(self)-> float:
        return self._dst_time

    def get_src(self) -> int:
        return self._src

    def get_dest(self) -> int:
        return self._dest