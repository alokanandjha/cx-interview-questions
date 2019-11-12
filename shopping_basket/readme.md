# Shopping Basket Solution

Project has below modules:
* Cart
* Catalogue
* Offers
* Common

There is separate Unit test for all the modules (for now it is at same place, however, these can be separated across respective modules)

The definition of an Item that can be bought/sold is in Item.py which is in project Common folder for esy visibility across all teams/services.across

The Singleton class is also in project Common for easy visibility across all teams.

Catalogue is a created as a Singleton as there is going to be a single catalogue for all buyers.

Offers is created as Singleton as separate team will be maintaining the offers.

The discount should be applied at the time of checkout (which is not implemented), and corresponding calculation is in Cart class.







