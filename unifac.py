from __future__ import annotations
from typing import NamedTuple


data_gr:list[Group] = [None]*51


def reset_gr():
    for gr in data_gr:
        if gr is not None:
            gr.X = 0
            gr.Theta = 0

class Group:
    def __init__(self,
                 id:int=None,
                 gr:str=None,
                 sub_gr:list[str]=None,
                 Rk:list[float]=None,
                 Qk:list[float]=None,
                 a_mn:list[float]=None):
        if id is not None:
            self.id:int=id
        else:
            raise ValueError('Void id is not allowed.')

        self.gr:str=gr
        self.sub_gr:list[str]=sub_gr if sub_gr is not None else []
        self.Rk:list[float]=Rk if Rk is not None else []
        self.Qk:list[float]=Qk if Qk is not None else []
        self.a_mn:list[float]=a_mn if a_mn is not None else []
        self.X:float = 0
        self.Theta:float = 0

    def set_gr(self, gr:str):
        if gr is not None:
            self.gr = gr
        else:
            raise ValueError('"add_group()" is called, but group name is not given.')

    def set_sub_gr_list(self, list_gr:list[str]):
        if list_gr is not None:
            self.sub_gr = list_gr
        else:
            raise ValueError('"add_sub_group_list()" is called, but sub group list is not given.')

    def add_sub_gr(self, id_sub_gr:int, name_sub_gr:str):
        if id_sub_gr is None:
            raise ValueError('"add_sub_group()" is called, but "id_sub_group" is not given.')
        if name_sub_gr is None:
            raise ValueError('"add_sub_group()" is called, but "name_sub_group" is not given.')

        if len(self.sub_gr)-1 < id_sub_gr:
            self.sub_gr += [None]*(id_sub_gr-(len(self.sub_gr)-1))
        self.sub_gr[id_sub_gr] = name_sub_gr

    def set_r_k_list(self, Rk:list[float]):
        if Rk is None:
            raise ValueError('"set_r_k_list()" is called, but the list "r_k" is not given.')
        self.Rk = Rk

    def set_r_k(self, id_sub_gr:int, name_sub_gr:str, single_Rk:float):
        if len(self.Rk)-1 < id_sub_gr:
            self.Rk += [None]*(id_sub_gr - (len(self.Rk)-1))

        if (len(self.sub_gr)-1 >= id_sub_gr
            and self.sub_gr[id_sub_gr] is not None
            and self.sub_gr[id_sub_gr] != name_sub_gr):
            raise ValueError(f'set_r_k(): sub group name mismatch. Stored: "{self.sub_gr[id_sub_gr]}" vs newly gven: "{name_sub_gr}"')

        self.Rk[id_sub_gr] = single_Rk

    def set_q_k_list(self, Qk:list[float]):
        if Qk is None:
            raise ValueError('"set_q_k_list()" is called, but the list "q_k" is not given.')
        self.Qk = Qk

    def set_q_k(self, id_sub_gr:int, name_sub_gr:str, single_Qk:float):
        if len(self.Qk)-1 < id_sub_gr:
            self.Qk += [None]*(id_sub_gr - (len(self.Qk)-1))

        if (len(self.sub_gr)-1 >= id_sub_gr
            and self.sub_gr[id_sub_gr] is not None
            and self.sub_gr[id_sub_gr] != name_sub_gr):
            raise ValueError(f'set_q_k(): sub group name mismatch. Stored: "{self.sub_gr[id_sub_gr]}" vs newly gven: "{name_sub_gr}"')        

        self.Qk[id_sub_gr] = single_Qk

    def set_a_mn_list(self, a_mn:list[float]):
        if a_mn is None:
            raise ValueError('"set_a_mn_list()" is called, but the list "amn" is not given.')
        self.a_mn = a_mn

    def set_a_mn(self, id_sub_gr:int, name_sub_gr:str, single_a_mn:float):
        if len(self.a_mn)-1 < id_sub_gr:
            self.a_mn += [None]*(id_sub_gr - (len(self.a_mn)-1))

        if (len(self.sub_gr)-1 >= id_sub_gr
            and self.sub_gr[id_sub_gr] is not None
            and self.sub_gr[id_sub_gr] != name_sub_gr):
            raise ValueError(f'set_a_mn(): sub group name mismatch. Stored: "{self.sub_gr[id_sub_gr]}" vs newly gven: "{name_sub_gr}"')        

        self.a_mn[id_sub_gr] = single_a_mn

    def get_R(self, id_sub_gr:int=None, name_sub_gr:str=None)->float:
        if id_sub_gr is not None and name_sub_gr is not None:
            if self.sub_gr[id_sub_gr] != name_sub_gr:
                raise ValueError(f'get_Rk(): Group "{self.gr}". Inconsistent sub group ID "{id_sub_gr}" and sub group name "{name_sub_gr}".')

        if id_sub_gr is not None:
            return self.Rk[id_sub_gr]
        elif name_sub_gr is not None:
            temp_id = self.sub_gr.index(name_sub_gr)
            return self.Rk[temp_id]
        else:
            raise ValueError('Both "id_sub_gr" and "name_sub_gr" are not given.')

    def get_Q(self, id_sub_gr:int=None, name_sub_gr:str=None)->float:
        """
        Do something.
        """
        if id_sub_gr is not None and name_sub_gr is not None:
            if self.sub_gr[id_sub_gr] != name_sub_gr:
                raise ValueError(f'get_Qk(): Group "{self.gr}". Inconsistent sub group ID "{id_sub_gr}" and sub group name "{name_sub_gr}".')

        if id_sub_gr is not None:
            return self.Qk[id_sub_gr]
        elif name_sub_gr is not None:
            temp_id = self.sub_gr.index(name_sub_gr)
            return self.Qk[temp_id]
        else:
            raise ValueError('Both "id_sub_gr" and "name_sub_gr" are not given.')


class GrComposition:
    def __init__(self, gr_main: int, gr_sub: int, num_gr: int):
        self.id_gr_main:int = gr_main
        self.id_gr_sub:int = gr_sub
        self.num_gr:int = num_gr
        

class Solvent:
    def __init__(self, list_gr:list[GrComposition]=None):
        self.list_gr:list[GrComposition] = list_gr if list_gr is not None else []
        self.r:float = None
        self.q:float = None
        self.Theta:float = None

    def add_composition(self, gr_main:int, gr_sub: int, num_gr:int):
        new_gr = GrComposition(gr_main=gr_main, gr_sub=gr_sub, num_gr=num_gr)
        self.list_gr.append(new_gr)

    def calc_inherent_params(self):
        temp_r = 0.0
        temp_q = 0.0
        for gr in self.list_gr:
            id_main_gr_this = gr.id_gr_main
            id_sub_gr_this = gr.id_gr_sub
            num_gr_this = gr.num_gr

            R = data_gr[id_main_gr_this].get_R(id_sub_gr_this)
            temp_r += R*num_gr_this

            Q = data_gr[id_main_gr_this].get_Q(id_sub_gr_this)
            temp_q += Q*num_gr_this

        self.r = temp_r
        self.q = temp_q

    def calc_gamma_self(self, temp:float):
        for gr_piv in self.list_gr:
            id_main_piv:int = gr_piv.id_gr_main
            id_sub_piv:int = gr_piv.id_gr_sub
            for gr_cyc in self.list_gr:
                if gr_cyc != gr_piv:
                    id_main_cyc = gr_cyc.id_gr_main
                    






class System:
    def __init__(self, list_solv:list[Solvent]=None, solv_composition:list[float]=None):
        self.list_solv = list_solv if list_solv is not None else []
        self.solv_composition = solv_composition if solv_composition is not None else []

        if len(list_solv) != len(solv_composition):
            raise RuntimeError(f'System.__init__(): Length mismatched. len(list_solv)=={len(list_solv)}, len(solv_composition)=={len(solv_composition)}')

    
        


        





        







        




    