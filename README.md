# Hotel Room Reservation System - Group 10

## Django API Project
## BBT 3101: Application Programming For The Internet

## Group Members
1. Kungu David
2. 138930 Kiconco Cynthia
3. Gitau Mugambi
4. 145618 Mbogo Brian Karanja
5. 145756 Njoroge Mercy

# Project Description
## 1. Models
The five models used are customer, room type, room, reservation and payments.

The customer model represents a guest or customer in the system with fields first_name, last_name and email. The customer model is connected to the Reservation model where a customer can have multiple reservations.

The roomtype model represents the different types of rooms available in the hotel e.g., single, double and suite, with fields type_name and description. The RoomType model is connected to the Room model, where each room type has a specific price, room number, availability, etc.

The room model represents a specific room in the hotel with fields room_number, room_type, price_per_night and is_available. The Room model is connected to the RoomType model, where each room is of a specific type. It also relates to Reservation, where a room can have multiple reservations.

The reservation model represents a booking made by a customer for a specific room with fields customer, room, check_in and check_out. The reservation model is connected to both Customer and Room models, indicating which customer booked which room. It also has a one-to-one relationship with the payment model, where each reservation has a corresponding payment.

The payment model represents the payment details for a reservation with fields reservation, amount, payment_date and status. The payment model is connected to the reservation model where each reservation has one corresponding payment.

## 2. Views
## 3. Serialziers
## 4. URLs

# Testing
We tested the end points manually using Postman covering the HTTP methods, GET, POST, PUT and DELETE as below;
## 1. GET
The GET method is used to retrieve data from the server. In Postman, we set the method to GET and put the url of the customer 2 and the data was returned as follows;
![Code](https://github.com/CynthiaKiconco/HotelRoomReservationSystem-Group10/blob/main/GET_result.png)

## 2. POST
The POST method sends data to the server to create a resource. In Postman, we set the method to POST and put the url of the roomtypes page to add a new room type and its description and the result was as follows;
![Code](https://github.com/CynthiaKiconco/HotelRoomReservationSystem-Group10/blob/main/POST_result.png)

## 3. PUT
The PUT method is used to update an existing resource. In Postman, we set the method to POST and updated the information of customer 3 in the system as follows;

Before
![Code](https://github.com/CynthiaKiconco/HotelRoomReservationSystem-Group10/blob/main/PUT_before.png)

After
![Code](https://github.com/CynthiaKiconco/HotelRoomReservationSystem-Group10/blob/main/PUT_after.png)

## 4. DELETE
The DELETE method is used to delete a resource. In Postman, we set the method to DELETE and deleted a reservation made by a customer as shown below;

Before: this is the data in the system for the reservation for a customer before deleting
![Code](https://github.com/CynthiaKiconco/HotelRoomReservationSystem-Group10/blob/main/delete_before.png)

After: this is the result after sending the delete request is sent on Postman. There is no content in the output
![Code](https://github.com/CynthiaKiconco/HotelRoomReservationSystem-Group10/blob/main/delete_after.png)

## Conclusion







