import time
import random
import numpy as np 

from rlbot.agents.base_script import BaseScript
from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3, Rotator, GameInfoState
from rlbot.utils.structures.game_data_struct import GameTickPacket


#GameMode Probability, whole numbers only
ones_prob = 10
twos_prob = 10
threes_prob = 10
fours_prob = 10
fives_prob = 10

#Set to 1 if you want a simulated kickoff when goal reset is disabled, 0 if you don't want kickoff
simulated_kickoff = 1



class RandomStandard(BaseScript):
    def __init__(self):
        super().__init__("Random Standard")

    def start(self):
        #Set up old score
        old_score = 0
        #Creates a list to control the probablitly of the random choice later
        data_list = [1]*ones_prob + [2]*twos_prob
        gameM = random.choice(data_list)
        
        #Sets goal reset disabled to 1 (True)
        disabled_goal_reset = 1
        
        
        while 1:

            # when packet available
            packet = self.wait_game_tick_packet()

            if not packet.game_info.is_round_active:
                continue
             
            
            #sets random probability depending on mode
            #2v2
            if packet.num_cars == 4:
                 data_list = [1]*ones_prob + [2]*twos_prob
            #3v3
            if packet.num_cars == 6:
                 data_list = [1]*ones_prob + [2]*twos_prob + [3] * threes_prob
            #4v4
            if packet.num_cars == 8:
                 data_list = [1]*ones_prob + [2]*twos_prob + [3] * threes_prob +[4] * fours_prob +[5] 
            #5v5
            if packet.num_cars == 10:
                 data_list = [1]*ones_prob + [2]*twos_prob + [3] * threes_prob +[4] * fours_prob +[5] * fives_prob
            
            #Check if kickoff
            if packet.game_info.is_kickoff_pause and packet.teams[0].score + packet.teams[1].score != 0:
             #kickoffs are enabled
             disabled_goal_reset = 0
            
            #Checks if goal has been scored and picks a random game mode
            if packet.teams[0].score + packet.teams[1].score != old_score:
                old_score = packet.teams[0].score + packet.teams[1].score
                
                #Check if should simulated kickoff
                if disabled_goal_reset == 1 and simulated_kickoff == 1:
                  self.setup_kickoff(packet)
                
                # gameM = random.randint(1, 3)
                gameM = random.choice(data_list)
            
            #Checks that there are 10 cars then teleports cars depending on mode
            if packet.num_cars == 10:
                 
                 if gameM == 4:  
                     #3v3 
                     car_states = {}
                     for p in range(4,5):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(9,10):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
            
                 if gameM == 3:  
                     #3v3 
                     car_states = {}
                     for p in range(3,5):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(8,10):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
                 
                 if gameM == 2:  
                     #2v2 
                     car_states = {}
                     for p in range(2,5):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(7,10):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
                 if gameM == 1:  
                     #1v1
                     car_states = {}
                     for p in range(1,5):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(6,10):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
            
            #Checks that there are 8 cars then teleports cars depending on mode
            if packet.num_cars == 8:
                 
                 if gameM == 3:  
                     #3v3 
                     car_states = {}
                     for p in range(3,4):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(7,8):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
                 
                 if gameM == 2:  
                     #2v2 
                     car_states = {}
                     for p in range(2,4):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(6,8):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
                 if gameM == 1:  
                     #1v1
                     car_states = {}
                     for p in range(1,4):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(5,8):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
            
            
            #Checks that there are 6 cars then teleports cars depending on mode
            if packet.num_cars == 6:
                 
                 if gameM == 2:  
                     #2v2 
                     car_states = {}
                     for p in range(2,3):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(5,6):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
                 if gameM == 1:  
                     #1v1
                     car_states = {}
                     for p in range(1,3):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(4,6):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
           #Checks that there are 4 cars then teleports cars depending on mode
            if packet.num_cars == 4:
                
                 if gameM == 1:  
                     #1v1
                     car_states = {}
                     for p in range(1,2):
                         car = packet.game_cars[p]
                         pos = Vector3((3000+p*150), (5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     for p in range(3,4):
                         car = packet.game_cars[p]
                         pos = Vector3(-(3000+p*150), -(5500+p*150), (80))
                         car_state = CarState(boost_amount=0, physics=Physics(location=pos, rotation=Rotator(yaw=0, pitch=0, roll=0), velocity=Vector3(0, 0, 0), angular_velocity=Vector3(0, 0, 0)))
                         car_states[p] = car_state
                     self.paused_car_states = car_states
                     self.game_state = GameState(cars=car_states)
                     self.set_game_state(self.game_state)
    
    
    
    
    def setup_kickoff(self, packet):
     if packet.num_cars == 4 or packet.num_cars == 6 or packet.num_cars == 8 or packet.num_cars == 10:
            car_states = {}
            numC = round(packet.num_cars *0.5)     # set the number to select here.
            rand_kick = random.sample(range(5), numC)
            for p in range(packet.num_cars):
                car = packet.game_cars[p]
                if car.team == 0:
                    if rand_kick[p] == 0:
                        pos = Vector3(-2048, -2560, 17)
                        yaw = np.pi * 0.25
                    elif rand_kick[p] == 1:
                        pos = Vector3(2048, -2560, 17)
                        yaw = np.pi * 0.75
                    elif rand_kick[p] == 2:
                        pos = Vector3(-256.0, -3840, 17)
                        yaw = np.pi * 0.5
                    elif rand_kick[p] == 3:
                        pos = Vector3(256.0, -3840, 17)
                        yaw = np.pi * 0.5
                    elif rand_kick[p] == 4:
                        pos = Vector3(0.0, -4608, 17)
                        yaw = np.pi * 0.5
                    car_state = CarState(boost_amount=34, physics=Physics(location=pos, rotation=Rotator(yaw=yaw, pitch=0, roll=0), velocity=Vector3(0, 0, 0),
                            angular_velocity=Vector3(0, 0, 0)))
                    car_states[p] = car_state
                elif car.team == 1:
                    if rand_kick[p-numC] == 0:
                        pos = Vector3(2048, 2560, 17)
                        yaw = np.pi * -0.75
                    elif rand_kick[p-numC] == 1:
                        pos = Vector3(-2048, 2560, 17)
                        yaw = np.pi * -0.25
                    elif rand_kick[p-numC] == 2:
                        pos = Vector3(256.0, 3840, 17)
                        yaw = np.pi * -0.5
                    elif rand_kick[p-numC] == 3:
                        pos = Vector3(-256.0, 3840, 17)
                        yaw = np.pi * -0.5
                    elif rand_kick[p-numC] == 4:
                        pos = Vector3(0.0, 4608, 17)
                        yaw = np.pi * -0.5
                    car_state = CarState(boost_amount=34, physics=Physics(location=pos, rotation=Rotator(yaw=yaw, pitch=0, roll=0), velocity=Vector3(0, 0, 0),
                            angular_velocity=Vector3(0, 0, 0)))
                    car_states[p] = car_state
            ball_state = BallState(Physics(location=Vector3(0, 0, 0), velocity=Vector3(0,0,0)))
            self.paused_car_states = car_states
            self.game_state = GameState(cars=car_states)
            self.set_game_state(self.game_state)
    
   


if __name__ == "__main__":
    random_standard = RandomStandard()
    random_standard.start()
