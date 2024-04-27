from random import randint
import json
import requests
from datetime import timedelta, datetime

class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.stats = self.get_stats()
        

        self.power = randint(30, 60)
        self.hp = randint(200,400)

        self.last_feed_time = datetime.now()

        self.Pikachu : bool = False
        
        with open('achievements.json', 'r') as json_file:
            achievement = json_file.read()
            print(achievement)
            self.achievements_converted = json.loads(achievement)

        Pokemon.pokemons[pokemon_trainer] = self



    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return 'https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&amp;amp;path-prefix=ru'
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            self.Pikachu = True
            return "Pikachu"
        
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"      
        

    def achievements(self):
        if self.achievements_converted['achievements'][0]['get'] != True:
            with open('achievements.json', 'w') as json_file:
                self.achievements_converted['achievements'][0]['get'] = True
                self.New_achievements_Json = json.dumps(self.achievements_converted, indent=2)
                json_file.write(self.New_achievements_Json)
                # self.UpdateAch()
                # self.achievements()
                return self.achievements_converted['achievements'][0]['message']
        if self.pokemon_number == 6 and self.achievements_converted['achievements'][1]['get'] != True:
            with open('achievements.json', 'w') as json_file:
                self.achievements_converted['achievements'][1]['get'] = True
                self.New_achievements_Json = json.dumps(self.achievements_converted, indent=2)
                json_file.write(self.New_achievements_Json)
                # self.UpdateAch()
                # self.achievements()
                return self.achievements_converted['achievements'][1]['message']  
        if self.achievements_converted['achievements'][2]['get'] != True and self.Pikachu != False:
                self.achievements_converted['achievements'][2]['get'] = True
                self.New_achievements_Json = json.dumps(self.achievements_converted, indent=2)
                json_file.write(self.New_achievements_Json)
                # self.UpdateAch()
                # self.achievements()
                return self.achievements_converted['achievements'][2]['message']  
        else: 
            print('no achievements :"( ')    
            return


    def get_stats(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            special_attack = data['stats'][3]['base_stat']
            special_defense = data['stats'][4]['base_stat']
            speed = data['stats'][5]['base_stat']

            return f" \nhp: {hp} \nattack: {attack} \ndefense: {defense} \nspecial-attack: {special_attack} \nspecial-defense: {special_defense} \nspeed: {speed}"
        


    # Метод класса для получения информации
    def info(self):
        return f""" Имя твоего покеомона: {self.name} \nстатистика: {self.stats}
                    Сила покемона: {self.power}
                    Здоровье покемона: {self.hp}
                """

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
              return "Покемон-волшебник применил  щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f''''Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}
Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}'''
        else:
            enemy.hp = 0
            return f'''Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!'''
        



class Wizard(Pokemon):
    def feed (self):
        return super().feed(hp_increase=20)


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(1, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'\nБоец применил супер-атаку силой:{super_power}'
    
    def feed(self):
        return super().feed(feed_interval=10)
# if __name__ == '__main__':

#     wizard = Wizard("username1")
#     fighter = Fighter("username2")

#     print(wizard.info())
#     print()
#     print(fighter.info())
#     print()
#     print(fighter.attack(wizard))    