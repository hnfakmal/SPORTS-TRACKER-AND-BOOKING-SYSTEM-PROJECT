from tkinter import *
from GenerateNewCode import random_id
from DataBase import EventDetails
from DataBase import CreateNewEvent
from Message import show_message
from tkcalendar import DateEntry
from datetime import date


def CreateEvent():
    event_ids = EventDetails()[1]

    # Main Instructions Window
    top2 = Tk()
    top2.geometry('600x600')  # Adjusted size for readability
    top2.title('Event Booking Instructions')

    # Agreement variable to track checkbox state
    agreement = IntVar(value=0)  # Start unchecked

    def proceed_to_booking():
        if agreement.get() == 0:  # Checkbox is checked
            top2.destroy()  # Close the instructions window
            open_booking_popup()  # Open the booking popup
        else:
            show_message('Error', 'Please agree to the terms and conditions before proceeding.')

    def open_booking_popup():
        booking_window = Tk()
        booking_window.geometry('400x400')
        booking_window.title('Create New Event')

        event_name = StringVar(booking_window)
        event_id = StringVar(booking_window)
        event_date = StringVar(booking_window)
        event_date.set(date.today())
        event_time = StringVar(booking_window)
        event_duration = StringVar(booking_window)

        while True:
            new_event_id = random_id()
            if new_event_id not in event_ids:
                event_id.set(new_event_id)
                break

        def CreateNow():
            if len(event_name.get()) < 5:
                show_message('Error', 'Enter valid details.')
                return
            event_status = CreateNewEvent(event_name.get(), event_id.get(), event_date.get(), event_time.get(),
                                          event_duration.get())
            if event_status == 'Success':
                show_message('Success', 'Event created successfully.')
                booking_window.destroy()
            else:
                show_message('Error', event_status)

        Label(booking_window, text='Enter Event Details', font=('Arial', 14)).pack(pady=10)

        Label(booking_window, text='Event Name', font=('Arial', 12)).pack(pady=5)
        Entry(booking_window, textvariable=event_name).pack()

        Label(booking_window, text='Event Id', font=('Arial', 12)).pack(pady=5)
        Entry(booking_window, textvariable=event_id, state='disabled').pack()

        Label(booking_window, text='Event Date', font=('Arial', 12)).pack(pady=5)
        DateEntry(booking_window, selectmode='day', year=2023, month=1, day=25, textvariable=event_date).pack()

        Label(booking_window, text='Event Time (24hrs)', font=('Arial', 12)).pack(pady=5)
        Entry(booking_window, textvariable=event_time).pack()

        Label(booking_window, text='Event Duration', font=('Arial', 12)).pack(pady=5)
        Entry(booking_window, textvariable=event_duration).pack()

        Button(booking_window, text='Submit', bg='green', fg='white', font=('Arial', 14), width=12, command=lambda: CreateNow()).pack(pady=20)

    # Instructions
    Label(top2, text='Event Booking Terms and Conditions', font=('Arial', 14, 'bold')).pack(pady=10)
    Label(top2, text='''General Rules:
1. Use of sports facilities is prioritized for students and staff of Universiti Malaysia Pahang Al-Sultan Abdullah.
2. Bookings for daily sports use must be made at least 3 days in advance.
3. Bookings for sports events (e.g., faculty tournaments) must be made at least 7 working days in advance.
4. All users are required to book through the counter or the e-community application.
5. Continuous bookings for more than 7 days are not allowed; a new booking must be made for extended usage.
6. Users must show up within 15 minutes of their booked time; otherwise, the facility will be made available to others.
7. Adhere to sports attire etiquette at all times.
8. Maintain cleanliness, safety, and turn off lights and air conditioners after use.
9. Bring a student/staff ID card to borrow sports equipment.
10. The university is not responsible for any injuries or accidents during facility use.
11. Eating or drinking inside the court is strictly prohibited.
12. Be considerate and avoid monopolizing facilities.
13. The university reserves the right to cancel approved bookings without prior notice for official events.
14. Smoking is strictly prohibited on university premises.''',
          justify=LEFT, wraplength=480, font=('Arial', 10)).pack(padx=10, pady=5)

    # Agreement checkbox
    Checkbutton(top2, text="I agree to the terms and conditions.", variable=agreement).pack(pady=10)

    # Proceed Button
    Button(top2, text='Proceed to Booking', bg='blue', fg='white', font=('Arial', 12), command=proceed_to_booking).pack(pady=20)

    top2.mainloop()
