'''4. Movie Ticket Booking System

Scenario:

A cinema hall wants to manage ticket bookings. Write a program to keep track of **available** and **booked seats**. Allow users to **book** or **cancel** a seat.

Requirements:

- Use functions to handle seat booking and cancellation.

- Prevent booking an already booked seat.

Input Example:

total_seats = 10

booked_seats = [2, 5, 7]

book_seat = 3

cancel_seat = 5

Expected Output:

Available seats: [1, 4, 6, 8, 9, 10]'''

class MovieTicketSystem:
    def __init__(self, total_seats, booked_seats):
        self.total_seats = total_seats
        self.booked_seats = booked_seats

    def book_seat(self, seat_number):
        if 1 <= seat_number <= self.total_seats and seat_number not in self.booked_seats:
            self.booked_seats.append(seat_number)
        else:
            print("Seat Not Available")

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
        else:
            print("Seat is Not Booked")

    def get_available_seats(self):
        all_seats = list(range(1, self.total_seats + 1))
        return [seat for seat in all_seats if seat not in self.booked_seats]

total_seats = int(input("Enter number of total seats: "))
booked_seats = list(map(int, input("Enter booked seats separated by comma: ").split(',')))
book_seat = int(input("Enter seat number to book: "))
cancel_seat = int(input("Enter seat number to cancel: "))

system = MovieTicketSystem(total_seats, booked_seats)

system.book_seat(book_seat)
system.cancel_seat(cancel_seat)

print(f"Available seats: {system.get_available_seats()}")