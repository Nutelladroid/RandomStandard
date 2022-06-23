import time
import random

from rlbot.agents.base_script import BaseScript
from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3, Rotator, GameInfoState
from rlbot.utils.structures.game_data_struct import GameTickPacket


#GameMode Probability, whole numbers only
ones_prob = 45
twos_prob = 45
threes_prob = 10



class RandomStandard(BaseScript):
    def __init__(self):
        super().__init__("Random Standard")

    def start(self):
        #Set up old score
        old_score = 0
        #Creates a list to control the probablitly of the random choice later
        data_list = [1]*ones_prob + [2]*twos_prob + [3] * threes_prob
        gameM = random.choice(data_list)
        while True:

            # when packet available
            packet = self.wait_game_tick_packet()

            if not packet.game_info.is_round_active:
                continue
            
            #Checks if goal has been scored and picks a random game mode
            if packet.teams[0].score + packet.teams[1].score != old_score:
                old_score = packet.teams[0].score + packet.teams[1].score
                # gameM = random.randint(1, 3)
                gameM = random.choice(data_list)
            
            
            #Checks that there are 6 cars then teleports cars depending on mode
            if packet.num_cars == 6:
                 if gameM == 2:  
                     #2v2 (I just copied 1v1 code)
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
   


if __name__ == "__main__":
    random_standard = RandomStandard()
    random_standard.start()
