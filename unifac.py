

class Group:
    def __init__(self,
                 id:int=None,
                 group:str=None,
                 sub_group:list[str]=None,
                 r_k:list[float]=[],
                 q_k:list[float]=[],
                 a_mn:list[float]=[]):
        if id is not None:
            self.id:int=id
        else:
            raise ValueError('Void id is not allowed.')

        self.group:str=group
        self.sub_group:str=sub_group
        self.r_k:list[float]=r_k
        self.q_k:list[float]=q_k
        self.a_mn:list[float]=a_mn

    def add_group(self, group:str):
        if group is not None:
            self.group = group
        else:
            raise ValueError('"add_group()" is called, but group name is not given.')

    def 



    