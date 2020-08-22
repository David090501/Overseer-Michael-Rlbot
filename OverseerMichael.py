from tools import  *
from objects import *
from routines import *


#This file is for strategy

class ExampleBot(GoslingAgent):
    def run(agent):
        if len(agent.stack) < 1:
            targets = {"goal" : (agent.foe_goal.left_post,agent.foe_goal.right_post)}
            shots = find_hits(agent,targets)
            if len(shots["goal"]) > 0:
                agent.push(shots["goal"][0])
            else:
                relative = agent.friend_goal.location - agent.me.location
                defaultPD(agent, agent.me.local(relative))
                defaultThrottle(agent, 1410)