class Property(object):
    def __init__(self, square_feet="", beds="", baths="", **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))

    @staticmethod
    def prompt_print():
        return dict(
            square_feet=input("Enter the square feet: "),
            beds=input("Enter number of bedrooms"),
            baths=input("Enter number of baths"),
        )


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony="", laundary="", **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundary = laundary

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundary: %s " % self.laundary)
        print("has balcony: %s" % self.balcony)

        parent_init = Property.prompt_print()
        laundary = ""
        while laundary.lower() not in Apartment.valid_laundries:
            laundary = input(
                "What laundary facilitie does the property have? ({})".format(
                    ", ".join(Apartment.valid_laundries)
                )
            )

        balcony = ""
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? ({})".format(
                    ", ".join(Apartment.valid_balconies)
                )
            )
        parent_init.update({"laundary": laundary, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)
