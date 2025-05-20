class User:

    def __init__(self,first_name,last_name,email,age):
        self.firstName= first_name
        self.lastName= last_name
        self.email= email
        self.age= age
        self.is_rewards_member=False
        self.gold_card_points = 0

    def display_info(self):
        print (self.__dict__)
        for key, value in self.__dict__.items():     #self.items does not work cause .items() only works with dictionaries not class instance (self)
            print(f"{key}: {value}")    #__dict__: special built-in attribute =>stores all instance attributes in a dictionary
        return self
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return self
        self.is_rewards_member=True
        self.gold_card_points=200
        return self

    def spend_points(self, amount):
        if amount> self.gold_card_points:
            print(f"Not enough points to spend. Available: {self.gold_card_points}, Tried to spend: {amount}")
            
        else:
            self.gold_card_points -=amount
            print("available: ", self.gold_card_points)
        return self
        
user1 = User("lyna","adalet","lyna@jjj.com",21)
user1.display_info().enroll().spend_points(100) # each method should return self to enable the chaining(it is like self.method)
