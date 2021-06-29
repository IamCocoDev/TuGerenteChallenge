# TuGerenteChallenge
To open this project you need to clone.
Then you open a terminal inside the project directory and do `source env/bin/activate`
and now write on the shell

    cd hotel/
    cd hotelYourGerente/
    python manage.py runserver

and go to localhost: 8000

EndPoint Justification 

 We have 3 endpoints
- http: // localhost: 8000 / booking
- http: // localhost: 8000 / client
- http: // localhost: 8000 / billingdata

I did 3 because my logic was that I needed an endpoint for each new object that I added within the general object that is my Booking.
http: // localhost: 8000 / booking is an endpoint where we can add new reservations, modify data of an existing reservation and consult all the reservations and one in specific by id. Within the reservations we have two more objects called client where the client's data is stored and another object that stores the payment data because a client may stay at the hotel but pay with the card of a company or another person.
http: // localhost: 8000 / client is an endpoint to consult new clients both by id and in general this would serve both to have a list of all the people hosted and a detail of each one, as in booking you can do massive query, by id, an existing customer can be modified and a new customer can be added.
http: // localhost: 8000 / billingdata is an endpoint to consult the billing data of all customers and by id new billing data can be generated and existing data can be edited.
All this I thought following a logic that once the data enters the database from the front, the person who created it cannot delete it, just edit it, this serves not to lose any data from any client that would help us to get data and statistics about the hotel.
And if we had a hotel FrontEnd where the receptionist entered the new clients, we would have the following screens:
A screen to enter the reservation with customer data and billing information.
Another screen where all the reservations would be consulted.
Another where you could edit each data of each reservation within the hotel.
 And a final where you could download everything to an excel to be able to work with the information and the numbers
