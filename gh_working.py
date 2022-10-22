import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
import inspect
from pathlib import Path
import math
import random
from operator import itemgetter

class Keeper:

  def __init__(self,name_pickle="model_def.pickle"):
    self.name_pickle=name_pickle
    #reward per episode
    self.reward_per_episode=[]
    #action per episode
    self.action_per_episode=[]
    #reward per action
    self.reward_per_action=[[]]

    #secret_actions
    self.secret_actions=[]

    #spisuk efectivnes
    self.efectivnes_per_episode=[]

    #summurary
    self.summury_model=''
    #weights
    self.weights_of_model_1=''
    self.weights_of_model_2=''

    self.ime_arch=""

    #grads
    self.states=[]
    self.grads=[]

    #excecution time
    self.time_keeper=0

  def plts(self, rewards="graph na nagradi ili deistwiq",name_fig="ime", x_L="otstrani ", y_L="otdolu"):
    plt.xlabel(x_L)
    plt.ylabel(y_L)
    plt.title(name_fig)
    plt.plot(rewards)
    plt.savefig(str(name_fig))
    plt.close()


  def plts_reward_per_episode(self ,name_fig="Rewards per episode", x_L="Episodes", y_L="Reward"):
    plt.xlabel(x_L)
    plt.ylabel(y_L)
    plt.title(name_fig)
    plt.plot(self.reward_per_episode)
    plt.savefig(str(name_fig))
    plt.close()

  def plts_actions_per_episode(self ,name_fig="Actions per episode", x_L="Actions", y_L="Reward"):
    plt.xlabel(x_L)
    plt.ylabel(y_L)
    plt.title(name_fig)
    plt.plot(self.action_per_episode)
    plt.savefig(str(name_fig))
    plt.close()

  def plts_efectivnes_per_episode(self ,name_fig="Efectivnes per episode", x_L="Episode", y_L="Efectivnes"):
    plt.xlabel(x_L)
    plt.ylabel(y_L)
    plt.title(name_fig)
    plt.plot(self.efectivnes_per_episode)
    plt.savefig(str(name_fig))
    plt.close()



  def save(self):
    f = open(self.name_pickle, 'wb')
    pickle.dump(self.__dict__,f)
    f.close()
    print("saved sucsefully")
    print(self.name_pickle)

  def load(self):
    f = open(self.name_pickle, 'rb')
    unpickled_animals = pickle.load(f)
    #print(unpickled_animals)
    f.close()
    self.__dict__.update(unpickled_animals) 
    print ("loaded suxefullufy")
    #self=unpickled_animals
    #print(self.name_pickle)


