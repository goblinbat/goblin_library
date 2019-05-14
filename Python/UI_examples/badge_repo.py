
badges = []

class Badge:
        def __init__(self, badgeid, doors):
                self.badgeid = badgeid
                self.doors = doors
        
        def __repr__(self):
                return f'{self.badgeid}'
                
               


class BadgeRepo:
        def create_badge(badgeid, doors):
                new = Badge(badgeid, doors)
                badges.append(new)

        def view_badges():
                print(badges)
                return badges
        
        def add_door(badgeid, new_door):
                # adds a door value to the instance
                for b in badges:
                        if badgeid == b.badgeid:
                                b.doors.append(new_door)
                                return True
        
        def delete_door(badgeid, dor):
                # removes a single door value from the instance
                for b in badges:
                        if badgeid == b.badgeid:
                                for d in b.doors:
                                        if dor == d:
                                                x = b.doors.index(d)
                                                b.doors.pop(x)
                                                # return True
                                                return x
                else: 
                        return 'frog'
        
        def delete_badge(badgeid):
                # deletes the instance.
                for b in badges:
                        if badgeid == b.badgeid:
                                x = badges.index(b)
                                badges.pop(x)
                                return True


