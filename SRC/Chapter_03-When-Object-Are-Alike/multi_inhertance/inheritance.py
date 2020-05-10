class BaseClass(object):
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Sub Class")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on right sub class")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("Calling method on SubClass")
        self.num_sub_calls += 1


if __name__ == "__main__":
    s = SubClass()
    s.call_me()
    print(s.num_sub_calls, s.num_right_calls, s.num_left_calls, s.num_base_calls)
