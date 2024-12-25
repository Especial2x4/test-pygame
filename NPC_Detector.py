
import time


class NPC_Detector:

    def __init__(self, npc_list, random_flag):
        
        self.npc_list = npc_list
        self.random_flag = random_flag
    

    def show_npc_list(self):
        print(self.npc_list)
        for npc_name in self.npc_list:
            print(npc_name.name)

    def shooter(self):
        print(self.random_flag)
        for npc in self.npc_list:
            if npc.shooter_num == self.random_flag:
                print(f"{npc.name} dice : WAIT!")
                time.sleep(5)