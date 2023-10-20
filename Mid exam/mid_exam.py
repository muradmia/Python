class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seat_matrix = [['0' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seat_matrix

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Show ID not found.")
            return

        for row, col in seat_list:
            if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                if self.__seats[show_id][row - 1][col - 1] == '0':
                    self.__seats[show_id][row - 1][col - 1] = '1'
                    print(f"Seat {row}-{col} booked successfully.")
                else:
                    print(f"Seat {row}-{col} is already booked.")
            else:
                print(f"Invalid seat: {row}-{col}")

    def view_show_list(self):
        print("Show List:")
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    
    def view_available_seats(self, show_id):
     if show_id not in self.__seats:
        print("Show ID not found.")
        return

     print(f"Available seats for Show ID {show_id}:")
     seat_matrix = self.__seats[show_id]
     for row in seat_matrix:
        print(row)


hall1 = Hall(5, 10, 1)
hall2 = Hall(6, 8, 2)

hall1.entry_show("111", "Jawan", "12:00 PM")
hall1.entry_show("222", "Loki season 2", "3:00 PM")
hall2.entry_show("333", "Bloody daddy", "2:00 PM")

hall1.book_seats("111", [(1, 2), (2, 3), (3, 4)])

hall1.view_available_seats("111")

for hall in Star_Cinema.get_hall_list():
    hall.view_show_list()

