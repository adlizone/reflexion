"""Adapted from https://github.com/ysymyth/ReAct/blob/master/alfworld.ipynb"""

import os
import sys
import json
import yaml
import openai
import importlib
import alfworld
import alfworld.agents.environment
from utils import Model, get_chat, get_completion

from typing import List, Dict, Any, Tuple

def process_ob(ob):
    if ob.startswith('You arrive at loc '):
        ob = ob[ob.find('. ')+2:]    
    return ob

PREFIXES = {
    'pick_and_place': 'put',
    'pick_clean_then_place': 'clean',
    'pick_heat_then_place': 'heat',
    'pick_cool_then_place': 'cool',
    'look_at_obj': 'examine',
    'pick_two_obj': 'puttwo'
}

with open('base_config.yaml') as reader:
    config = yaml.safe_load(reader)
split = "eval_out_of_distribution"

#env = getattr(alfworld.agents.environment, config["env"]["type"])(config, train_eval=split)
#env = env.init_env(batch_size=1)

env_fn = alfworld.agents.environment.get_environment('AlfredTWEnv')(config, train_eval=split)
env = env_fn.init_env(batch_size=1)

for i in range(10):
    #Loads an instance of a task 
    #Provides initial observation
    #Logs task name and result
    ob, info = env.reset()
    ob = '\n'.join(ob[0].split('\n\n')[1:])
    name = '/'.join(info['extra.gamefile'][0].split('/')[-3:-1])

    print(f"using {name}")