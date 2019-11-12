# Shopping Basket Solution

Project has below modules:
* Cart
* Catalogue
* Offers
* Common

There is separate Unit test for all the modules (for now it is at same place, however, these can be separated across respective modules)

The definition of an Item that can be bought/sold is in Item.py which is in project Common folder for esy visibility across all teams/services.

The Singleton class is also in project Common for easy visibility across all teams.

Catalogue is a created as a Singleton as there is going to be a single catalogue for all buyers.

The discount should be applied at the time of checkout (which is not implemented), and corresponding calculation is in Cart class.

An Offer is created as abstract class - BaseOffer, and new type of offers can be created from it.

PercentOffer and BuynGetmOffer are created as new types of offers.

Each offer has to be added to Offers list by using add_offer method for it to be applied. An offer can be removed by calling remove_offer method in offers.

Offers is created as Singleton as there is going to be only one set of offers that either be applied or not. For an offer to be applied it has to be added to list of offers.










