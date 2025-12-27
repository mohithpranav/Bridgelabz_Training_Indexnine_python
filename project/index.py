class SeatBookingSystem():
    def __init__(self, total_seats ):
        self.total_seats = total_seats
        self.booked_seats = set()

    def book_seat(self, seat_number):
        if seat_number < 1 or seat_number > self.total_seats:
            return "invalid seat number."
        if seat_number in self.booked_seats:
            return "Seat already booked."
        self.booked_seats.add(seat_number)
        return "seat booked successfully."
    

    
s1 = SeatBookingSystem(10)
print(s1.book_seat(3))  

print(s1.book_seat(3))