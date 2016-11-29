import random
import os

class Crop(object):
    _growth_ = 0
    _days_growing_ = 0
    _type_ = 'generic'
    _status_ = 'seed'

    def __init__(self, growth_rate, light_needed, water_needed ):
        self._growth_rate_ = growth_rate
        self._light_needed_ = light_needed
        self._water_needed_ = water_needed

    @property
    def growth_rate(self):
        return self._growth_rate_

    @property
    def light_needed(self):
        return self._light_needed_

    @property
    def water_needed(self):
        return self._water_needed_

    def needs(self):
        needs_dict = {
                    'light': self.light_needed,
                    'water': self.water_needed
                     }
        return  needs_dict

    def report(self):
        report_dict = {
                    'growth': self._growth_,
                    'type': self._type_,
                    'days growing': self._days_growing_,
                    'status': self._status_
                      }
        return report_dict

    def _update_status_(self):
        if self._growth_ > 15:
            self._status_  = 'Old'
        elif self._growth_ > 10 and self._growth_ <=15:
                self._status_ =  'Mature'

        elif self._growth_ > 5 and self._growth_ <= 10:
            self._status_ = 'Young'
        elif self._growth_ > 0 and self._growth_ <= 5:
            self._status_ = 'Growing'
        else:
            self._status_ = 'Seed'

    def grow(self, water_given, light_given):
        self._days_growing_ += 1
        if water_given >= self.water_needed and light_given >= self.light_needed:
            self._growth_ += self.growth_rate


if __name__ =='__main__':
    cucumber = Crop(5, 6, 7)
    carrot = Crop(7, 7, 5)
    potato = Crop(2, 1, 1)
    carrot.grow(7,7)
    carrot._update_status_()

    def autogrow(culture, days):
        for day in range(days):
            generated_water = random.randint(0, 10)
            generated_light = random.randint(0, 10)
            culture.grow(generated_water, generated_light)

    def manual_grow(culture, given_water, given_light):
        culture.grow(given_water, given_light)

    # autogrow(potato, 8)
    manual_grow(potato, 10, 10)
    potato._update_status_()
    # testing constructor and property
    print 'I am Potato. My growth rate is {}. I want light - {}, water - {}. Moreover, i am {} and born from {}'.format(potato.growth_rate, potato.light_needed, potato.water_needed, potato._type_, potato._status_)

    # testing Crop methods
    print cucumber.report(), carrot.report(), potato.report()

    def display_menu(menu):
        os.system('cls')
        if menu == 'main':
            print 'Welcome to the Crop management system /n Make your choice:'
            print '1 - Manual crop grow'
            print '2 - Automatical crop grow'
            print '3 - Display crop report '
            print '0 - Exit '

        if menu == 'Give water':
            print 'Give some water(Grade 0-10)'

        if menu == 'Give light':
            print 'Give some light(Grade 0-10)'


    def get_menu_choice(bounder_value):
        try:
            made_choice = int(raw_input())
        except:
            print 'Not correct value. Not a int'
            manage_crop()
        if 0 < made_choice <= bounder_value:
            return made_choice
        else:
            print 'Not correct value'
            manage_crop()

    def manage_crop():
        display_menu('main')
        made_choice = get_menu_choice(3)

        if made_choice == 1 or made_choice == 2:
            display_menu('Give water')
            manual_water = get_menu_choice(10)
            display_menu('Give light')
            manual_light = get_menu_choice(10)
        if made_choice == 1:
            manual_grow(cabage, manual_water, manual_light)
        if made_choice == 2:
            autogrow(cabage, 30)
        if made_choice == 3:
            cabage._update_status_()
            print cabage.report()
        if made_choice == 0:
            quit()
        manage_crop()


    cabage = Crop(2, 5, 5)
    manage_crop()



